from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo de usuário personalizado"""
    TIPO_USUARIO_CHOICES = [
        ('promotor', 'Promotor de Vendas'),
        ('cliente', 'Cliente'),
        ('gerente_estoque', 'Gerente de Estoque'),
        ('gerente_vendas', 'Gerente de Vendas'),
        ('gerenciador', 'Gerenciador'),
    ]
    
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        

class Municipio(models.Model):
    """Modelo para municípios"""
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        unique_together = ['nome', 'estado']
        
    def __str__(self):
        return f"{self.nome} - {self.estado}"


class Cliente(models.Model):
    """Modelo para clientes"""
    STATUS_CHOICES = [
        ('aprovado', 'Aprovado'),
        ('pendente', 'Pendente'),
        ('reprovado', 'Reprovado'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    promotor = models.ForeignKey('PromotorVenda', on_delete=models.SET_NULL, null=True, blank=True)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status_financeiro = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return self.user.get_full_name()


class PromotorVenda(models.Model):
    """Modelo para promotores de venda"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    comissao = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    meta_mensal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_contratacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Promotor de Venda'
        verbose_name_plural = 'Promotores de Venda'
        
    def __str__(self):
        return self.user.get_full_name()
