from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class User(AbstractUser):
    """
    Modelo de usuário customizado que estende o User padrão do Django
    """
    TIPO_CHOICES = [
        ('promotor', 'Promotor de Vendas'),
        ('cliente', 'Cliente'),
        ('gerente_estoque', 'Gerente de Estoque'),
        ('gerente_vendas', 'Gerente de Vendas'),
        ('gerenciador', 'Gerenciador'),
    ]
    
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES, default='cliente')
    telefone = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Municipio(models.Model):
    """
    Modelo para representar os municípios
    """
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    codigo_ibge = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.nome} - {self.estado}"
    
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        unique_together = ['nome', 'estado']


class PromotorVenda(models.Model):
    """
    Modelo para representar um promotor de vendas
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipios_cobertura = models.ManyToManyField(Municipio, related_name='promotores')
    comissao_percentual = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=Decimal('5.00'),
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))]
    )
    
    def __str__(self):
        return f"Promotor: {self.user.get_full_name()}"
    
    class Meta:
        verbose_name = 'Promotor de Vendas'
        verbose_name_plural = 'Promotores de Vendas'


class Cliente(models.Model):
    """
    Modelo para representar um cliente
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    endereco = models.TextField()
    promotor = models.ForeignKey(PromotorVenda, on_delete=models.SET_NULL, null=True, blank=True)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status_financeiro = models.CharField(
        max_length=20, 
        choices=[
            ('aprovado', 'Aprovado'),
            ('pendente', 'Pendente'),
            ('reprovado', 'Reprovado'),
        ],
        default='pendente'
    )
    
    def __str__(self):
        return f"Cliente: {self.user.get_full_name()}"
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class GrupoProduto(models.Model):
    """
    Modelo para representar grupos de produtos
    """
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Grupo de Produto'
        verbose_name_plural = 'Grupos de Produtos'


class Produto(models.Model):
    """
    Modelo para representar um produto
    """
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.PROTECT)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    margem_lucro = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))]
    )
    estoque = models.PositiveIntegerField(default=0)
    percentual_promocao = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))]
    )
    impostos = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))]
    )
    ativo = models.BooleanField(default=True)
    
    @property
    def preco_venda(self):
        """Calcula o preço de venda com base no custo, margem e impostos"""
        preco_base = self.custo * (1 + self.margem_lucro / 100)
        preco_com_impostos = preco_base * (1 + self.impostos / 100)
        return preco_com_impostos
    
    @property
    def preco_promocional(self):
        """Calcula o preço promocional se há promoção"""
        if self.percentual_promocao > 0:
            return self.preco_venda * (1 - self.percentual_promocao / 100)
        return self.preco_venda
    
    @property
    def preco_final(self):
        """Retorna o preço final (promocional se existe, senão o preço normal)"""
        return self.preco_promocional if self.percentual_promocao > 0 else self.preco_venda
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Pedido(models.Model):
    """
    Modelo para representar um pedido
    """
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado_estoque', 'Aprovado pelo Estoque'),
        ('reprovado_estoque', 'Reprovado pelo Estoque'),
        ('aprovado_vendas', 'Aprovado pelas Vendas'),
        ('reprovado_vendas', 'Reprovado pelas Vendas'),
        ('programado', 'Programado para Entrega'),
        ('processado', 'Processado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    promotor = models.ForeignKey(PromotorVenda, on_delete=models.SET_NULL, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_entrega_programada = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    
    @property
    def valor_total(self):
        """Calcula o valor total do pedido"""
        return sum(item.subtotal for item in self.itens.all())
    
    @property
    def comissao_total(self):
        """Calcula a comissão total do pedido"""
        if self.promotor:
            return self.valor_total * (self.promotor.comissao_percentual / 100)
        return Decimal('0.00')
    
    def __str__(self):
        return f"Pedido {self.codigo} - {self.cliente.user.get_full_name()}"
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-data_pedido']


class ItemPedido(models.Model):
    """
    Modelo para representar os itens de um pedido
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        """Calcula o subtotal do item"""
        return self.quantidade * self.preco_unitario
    
    def save(self, *args, **kwargs):
        """Salva o preço unitário atual do produto"""
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco_final
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.produto.nome} - Qty: {self.quantidade}"
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'
        unique_together = ['pedido', 'produto']


class HistoricoStatusPedido(models.Model):
    """
    Modelo para rastrear o histórico de mudanças de status dos pedidos
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='historico_status')
    status_anterior = models.CharField(max_length=20, choices=Pedido.STATUS_CHOICES, null=True, blank=True)
    status_novo = models.CharField(max_length=20, choices=Pedido.STATUS_CHOICES)
    data_mudanca = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Pedido {self.pedido.codigo}: {self.status_anterior} → {self.status_novo}"
    
    class Meta:
        verbose_name = 'Histórico de Status'
        verbose_name_plural = 'Históricos de Status'
        ordering = ['-data_mudanca']


class Relatorio(models.Model):
    """
    Modelo para armazenar relatórios gerados
    """
    TIPO_CHOICES = [
        ('produtos_estoque_baixo', 'Produtos com Estoque Baixo'),
        ('produtos_promocao', 'Produtos em Promoção'),
        ('produtos_por_grupo', 'Produtos por Grupo'),
        ('vendas_promotor', 'Vendas por Promotor'),
        ('comissoes', 'Relatório de Comissões'),
        ('pedidos_periodo', 'Pedidos por Período'),
    ]
    
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    data_geracao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    parametros = models.JSONField(default=dict)
    arquivo = models.FileField(upload_to='relatorios/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.data_geracao.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        ordering = ['-data_geracao']
