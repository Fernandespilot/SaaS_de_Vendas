"""
URLs para o app de pedidos
"""
from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.listar_pedidos, name='listar_pedidos'),
    path('<int:pedido_id>/', views.detalhar_pedido, name='detalhar_pedido'),
    path('lista/', views.listar_pedidos, name='lista'),
]
