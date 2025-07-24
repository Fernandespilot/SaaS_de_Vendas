from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home e autenticação
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    
    # Produtos
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/buscar/', views.buscar_produtos, name='buscar_produtos'),
    path('produtos/<int:produto_id>/info/', views.get_produto_info, name='get_produto_info'),
    
    # Pedidos
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/criar/', views.criar_pedido, name='criar_pedido'),
    path('pedidos/<int:pedido_id>/', views.detalhar_pedido, name='detalhar_pedido'),
    path('pedidos/<int:pedido_id>/avaliar-estoque/', views.avaliar_pedido_estoque, name='avaliar_pedido_estoque'),
    path('pedidos/<int:pedido_id>/avaliar-vendas/', views.avaliar_pedido_vendas, name='avaliar_pedido_vendas'),
    path('pedidos/<int:pedido_id>/programar-entrega/', views.programar_entrega, name='programar_entrega'),
    path('pedidos/<int:pedido_id>/processar-entrega/', views.processar_entrega, name='processar_entrega'),
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),
    
    # Perfil
    path('perfil/', views.perfil, name='perfil'),
    
    # API
    path('api/municipios/', views.listar_municipios, name='listar_municipios'),
]
