from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.dashboard_usuarios, name='dashboard'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('promotores/', views.listar_promotores, name='listar_promotores'),
    path('promotores/cadastrar/', views.cadastrar_promotor, name='cadastrar_promotor'),
]
