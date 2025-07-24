from django.urls import path
from . import views_simple as views

app_name = 'relatorios'

urlpatterns = [
    path('', views.dashboard_relatorios, name='dashboard'),
    path('vendas/', views.relatorio_vendas, name='vendas'),
    path('produtos/', views.relatorio_produtos, name='produtos'),
    path('test/', views.relatorio_test, name='test'),
]
