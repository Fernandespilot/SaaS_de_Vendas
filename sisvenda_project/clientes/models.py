from django.db import models
from django.core.validators import EmailValidator
from decimal import Decimal


class Cliente(models.Model):
    """Modelo para clientes"""
    TIPO_PESSOA_CHOICES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('bloqueado', 'Bloqueado'),
    ]
    
    # Dados básicos
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200, blank=True)
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES, default='F')
    documento = models.CharField(max_length=18, unique=True)  # CPF ou CNPJ
    rg_ie = models.CharField(max_length=20, blank=True)  # RG ou Inscrição Estadual
    
    # Contato
    email = models.EmailField(validators=[EmailValidator()])
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15, blank=True)
    
    # Endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    # Dados comerciais
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    desconto_padrao = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    observacoes = models.TextField(blank=True)
    
    # Status e controle
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    data_nascimento = models.DateField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
        
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    @property
    def tipo_pessoa_display(self):
        return 'Pessoa Física' if self.tipo_pessoa == 'F' else 'Pessoa Jurídica'
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            # Gerar código automático
            ultimo_codigo = Cliente.objects.all().count() + 1
            self.codigo = f'CLI{ultimo_codigo:05d}'
        super().save(*args, **kwargs)
