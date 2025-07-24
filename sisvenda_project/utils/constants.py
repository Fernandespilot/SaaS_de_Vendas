"""
Constantes do sistema SisVenda
"""

# Status dos pedidos
STATUS_PEDIDO = {
    'PENDENTE': 'pendente',
    'AVALIACAO_ESTOQUE': 'avaliacao_estoque',
    'AVALIACAO_VENDAS': 'avaliacao_vendas',
    'APROVADO': 'aprovado',
    'PROGRAMADO': 'programado',
    'ENTREGUE': 'entregue',
    'CANCELADO': 'cancelado',
}

# Tipos de usuário
TIPOS_USUARIO = {
    'PROMOTOR': 'promotor',
    'CLIENTE': 'cliente',
    'GERENTE_ESTOQUE': 'gerente_estoque',
    'GERENTE_VENDAS': 'gerente_vendas',
    'GERENCIADOR': 'gerenciador',
}

# Status financeiro do cliente
STATUS_FINANCEIRO = {
    'APROVADO': 'aprovado',
    'PENDENTE': 'pendente',
    'REPROVADO': 'reprovado',
}

# Status do estoque
STATUS_ESTOQUE = {
    'NORMAL': 'estoque_normal',
    'BAIXO': 'estoque_baixo',
    'SEM_ESTOQUE': 'sem_estoque',
}

# Unidades de medida
UNIDADES = [
    ('UN', 'Unidade'),
    ('KG', 'Quilograma'),
    ('G', 'Grama'),
    ('L', 'Litro'),
    ('ML', 'Mililitro'),
    ('M', 'Metro'),
    ('CM', 'Centímetro'),
    ('M2', 'Metro Quadrado'),
    ('M3', 'Metro Cúbico'),
    ('CX', 'Caixa'),
    ('PC', 'Peça'),
    ('PAR', 'Par'),
    ('DZ', 'Dúzia'),
]

# Estados brasileiros
ESTADOS = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

# Configurações padrão
CONFIGURACOES_PADRAO = {
    'COMISSAO_PADRAO': 5.0,
    'LIMITE_CREDITO_PADRAO': 1000.00,
    'ESTOQUE_MINIMO_PADRAO': 5,
    'PRAZO_ENTREGA_PADRAO': 7,
    'PERCENTUAL_MARGEM_PADRAO': 30.0,
    'DESCONTO_MAXIMO_PADRAO': 10.0,
}

# Cores para status (Bootstrap)
CORES_STATUS = {
    'pendente': 'warning',
    'avaliacao_estoque': 'info',
    'avaliacao_vendas': 'primary',
    'aprovado': 'success',
    'programado': 'info',
    'entregue': 'success',
    'cancelado': 'danger',
    'aprovado_financeiro': 'success',
    'pendente_financeiro': 'warning',
    'reprovado_financeiro': 'danger',
    'estoque_normal': 'success',
    'estoque_baixo': 'warning',
    'sem_estoque': 'danger',
}

# Ícones para status (FontAwesome)
ICONES_STATUS = {
    'pendente': 'clock',
    'avaliacao_estoque': 'boxes',
    'avaliacao_vendas': 'chart-line',
    'aprovado': 'check-circle',
    'programado': 'calendar',
    'entregue': 'truck',
    'cancelado': 'times-circle',
    'promotor': 'user-tie',
    'cliente': 'user',
    'gerente_estoque': 'boxes',
    'gerente_vendas': 'chart-line',
    'gerenciador': 'cogs',
}

# Permissões por tipo de usuário
PERMISSOES_USUARIO = {
    'promotor': [
        'view_cliente',
        'add_cliente',
        'change_cliente',
        'view_produto',
        'add_pedido',
        'change_pedido',
        'view_pedido',
    ],
    'cliente': [
        'view_produto',
        'view_pedido',
        'add_pedido',
    ],
    'gerente_estoque': [
        'view_produto',
        'add_produto',
        'change_produto',
        'view_pedido',
        'change_pedido',
        'view_cliente',
    ],
    'gerente_vendas': [
        'view_produto',
        'view_pedido',
        'change_pedido',
        'view_cliente',
        'change_cliente',
        'view_promotor',
        'add_promotor',
        'change_promotor',
    ],
    'gerenciador': [
        'all_permissions',
    ],
}
