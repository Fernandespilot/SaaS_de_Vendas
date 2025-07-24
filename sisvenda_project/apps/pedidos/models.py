from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth import get_user_model
from apps.produtos.models import Produto

User = get_user_model()


class Pedido(models.Model):
    """Modelo para pedidos"""
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('avaliacao_estoque', 'Avaliação de Estoque'),
        ('avaliacao_vendas', 'Avaliação de Vendas'),
        ('aprovado', 'Aprovado'),
        ('programado', 'Programado para Entrega'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_vendedor')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-data_criacao']
        
    def __str__(self):
        return f"Pedido {self.codigo}"
    
    def calcular_totais(self):
        """Calcula os totais do pedido"""
        itens = self.itens.all()
        self.valor_total = sum(item.subtotal for item in itens)
        self.save()
    
    def pode_ser_cancelado(self):
        """Verifica se o pedido pode ser cancelado"""
        return self.status in ['pendente', 'avaliacao_estoque', 'avaliacao_vendas']
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            # Gerar código único
            ultimo_pedido = Pedido.objects.order_by('-id').first()
            if ultimo_pedido:
                numero = int(ultimo_pedido.codigo[3:]) + 1
            else:
                numero = 1
            self.codigo = f"PED{numero:06d}"
        super().save(*args, **kwargs)


class ItemPedido(models.Model):
    """Modelo para itens do pedido"""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
        unique_together = ['pedido', 'produto']
        
    def __str__(self):
        return f"{self.pedido.codigo} - {self.produto.nome}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)


class HistoricoStatusPedido(models.Model):
    """Modelo para histórico de status do pedido"""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='historico')
    status_anterior = models.CharField(max_length=20, blank=True)
    status_novo = models.CharField(max_length=20)
    data_mudanca = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Histórico de Status'
        verbose_name_plural = 'Históricos de Status'
        ordering = ['-data_mudanca']
        
    def __str__(self):
        return f"{self.pedido.codigo} - {self.status_novo}"
