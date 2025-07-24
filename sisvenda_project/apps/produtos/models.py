from django.db import models
from decimal import Decimal


class GrupoProduto(models.Model):
    """Modelo para grupos de produtos"""
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Grupo de Produto'
        verbose_name_plural = 'Grupos de Produtos'
        
    def __str__(self):
        return self.nome


class Produto(models.Model):
    """Modelo para produtos"""
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)  # Alias para estoque_atual
    estoque_minimo = models.IntegerField(default=0)
    unidade = models.CharField(max_length=10, default='UN')
    peso = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    dimensoes = models.CharField(max_length=50, blank=True)
    ativo = models.BooleanField(default=True)
    promocao = models.BooleanField(default=False)
    preco_promocao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    @property
    def preco_final(self):
        """Retorna o preço final considerando promoção"""
        if self.promocao and self.preco_promocao:
            return self.preco_promocao
        return self.preco_venda
    
    @property
    def margem_lucro(self):
        """Calcula a margem de lucro"""
        if self.preco_custo > 0:
            return ((self.preco_final - self.preco_custo) / self.preco_custo) * 100
        return 0
    
    @property
    def estoque_status(self):
        """Retorna o status do estoque"""
        if self.estoque_atual <= 0:
            return 'sem_estoque'
        elif self.estoque_atual <= self.estoque_minimo:
            return 'estoque_baixo'
        return 'estoque_normal'
