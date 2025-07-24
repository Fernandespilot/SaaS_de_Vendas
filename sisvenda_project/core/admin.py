from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import (
    User, Municipio, PromotorVenda, Cliente, GrupoProduto, 
    Produto, Pedido, ItemPedido, HistoricoStatusPedido, Relatorio
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'is_active']
    list_filter = ['tipo_usuario', 'is_active', 'is_staff']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'cpf']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'telefone', 'cpf')
        }),
    )


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'codigo_ibge']
    list_filter = ['estado']
    search_fields = ['nome', 'codigo_ibge']
    ordering = ['estado', 'nome']


@admin.register(PromotorVenda)
class PromotorVendaAdmin(admin.ModelAdmin):
    list_display = ['user', 'comissao_percentual', 'get_municipios']
    list_filter = ['comissao_percentual']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    filter_horizontal = ['municipios_cobertura']
    
    def get_municipios(self, obj):
        return ', '.join([str(m) for m in obj.municipios_cobertura.all()[:3]])
    get_municipios.short_description = 'Municípios de Cobertura'


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user', 'municipio', 'promotor', 'limite_credito', 'status_financeiro']
    list_filter = ['municipio', 'status_financeiro', 'promotor']
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'endereco']
    raw_id_fields = ['user', 'promotor']


@admin.register(GrupoProduto)
class GrupoProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    search_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'grupo', 'custo', 'preco_venda', 'estoque', 'ativo']
    list_filter = ['grupo', 'ativo']
    search_fields = ['codigo', 'nome']
    list_editable = ['estoque', 'ativo']
    
    def preco_venda(self, obj):
        return f'R$ {obj.preco_venda:.2f}'
    preco_venda.short_description = 'Preço de Venda'


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ['subtotal']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'cliente', 'promotor', 'data_pedido', 'status', 'valor_total']
    list_filter = ['status', 'data_pedido', 'promotor']
    search_fields = ['codigo', 'cliente__user__first_name', 'cliente__user__last_name']
    readonly_fields = ['codigo', 'valor_total', 'comissao_total']
    inlines = [ItemPedidoInline]
    
    def valor_total(self, obj):
        return f'R$ {obj.valor_total:.2f}'
    valor_total.short_description = 'Valor Total'


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'produto', 'quantidade', 'preco_unitario', 'subtotal']
    list_filter = ['pedido__status', 'produto__grupo']
    search_fields = ['pedido__codigo', 'produto__nome']
    
    def subtotal(self, obj):
        return f'R$ {obj.subtotal:.2f}'
    subtotal.short_description = 'Subtotal'


@admin.register(HistoricoStatusPedido)
class HistoricoStatusPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'status_anterior', 'status_novo', 'data_mudanca', 'usuario']
    list_filter = ['status_novo', 'data_mudanca']
    search_fields = ['pedido__codigo']
    readonly_fields = ['data_mudanca']


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'data_geracao', 'usuario']
    list_filter = ['tipo', 'data_geracao']
    search_fields = ['titulo']
    readonly_fields = ['data_geracao']


# Configuração do título do admin
admin.site.site_header = "SisVenda - Administração"
admin.site.site_title = "SisVenda Admin"
admin.site.index_title = "Bem-vindo ao Sistema de Vendas"
