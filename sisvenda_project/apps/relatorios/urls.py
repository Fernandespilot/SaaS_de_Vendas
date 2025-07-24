"""
URLs para o app de relatórios
"""
from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('', views.relatorios_dashboard, name='relatorios_dashboard'),
    path('vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('produtos/', views.relatorio_produtos, name='relatorio_produtos'),
    path('usuarios/', views.relatorio_usuarios, name='relatorio_usuarios'),
    path('vendas/pdf/', views.relatorio_vendas_pdf, name='relatorio_vendas_pdf'),
    path('vendas/excel/', views.relatorio_vendas_excel, name='relatorio_vendas_excel'),
]
