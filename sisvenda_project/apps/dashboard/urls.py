from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('promotor/', views.dashboard_promotor, name='promotor'),
    path('cliente/', views.dashboard_cliente, name='cliente'),
    path('gerente-estoque/', views.dashboard_gerente_estoque, name='gerente_estoque'),
    path('gerente-vendas/', views.dashboard_gerente_vendas, name='gerente_vendas'),
    path('gerenciador/', views.dashboard_gerenciador, name='gerenciador'),
]
