"""
Configuração do admin para o app de pedidos
"""
from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    """Inline para itens do pedido"""
    model = ItemPedido
    extra = 0
    readonly_fields = ('subtotal',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para pedidos"""
    list_display = ('id', 'usuario', 'vendedor', 'status', 'valor_total', 'data_criacao')
    list_filter = ('status', 'data_criacao', 'vendedor')
    search_fields = ('usuario__username', 'usuario__email', 'vendedor__username')
    readonly_fields = ('data_criacao', 'data_atualizacao', 'valor_total')
    inlines = [ItemPedidoInline]
    
    fieldsets = (
        ('Informações do Pedido', {
            'fields': ('usuario', 'vendedor', 'status')
        }),
        ('Valores', {
            'fields': ('valor_total',)
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para itens de pedido"""
    list_display = ('pedido', 'produto', 'quantidade', 'preco_unitario', 'subtotal')
    list_filter = ('pedido__status',)
    search_fields = ('pedido__id', 'produto__nome')
    readonly_fields = ('subtotal',)
