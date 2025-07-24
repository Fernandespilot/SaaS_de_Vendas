from django.contrib import admin
from .models import Produto, GrupoProduto


@admin.register(GrupoProduto)
class GrupoProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    list_filter = ['ativo']
    search_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'grupo', 'preco_venda', 'estoque', 'ativo']
    list_filter = ['grupo', 'ativo']
    search_fields = ['codigo', 'nome', 'descricao']
    readonly_fields = []
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'nome', 'descricao', 'grupo', 'ativo')
        }),
        ('Preços', {
            'fields': ('preco_custo', 'preco_venda')
        }),
        ('Estoque', {
            'fields': ('estoque', 'estoque_minimo', 'unidade')
        }),
        ('Detalhes', {
            'fields': ('peso',)
        }),
        ('Sistema', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        })
    )
