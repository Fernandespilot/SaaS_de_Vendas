# urls_simple.py - URLs simplificadas para o sistema

from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.core.views_simple import (
    dashboard_view, login_view, api_dashboard_stats
)

urlpatterns = [
    # Páginas principais
    path('', dashboard_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard_simple'),
    
    # Autenticação
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # Apps
    path('produtos/', include('apps.produtos.urls_simple')),
    path('pedidos/', include('apps.pedidos.urls_simple')),
    path('relatorios/', include('apps.relatorios.urls_simple')),
    path('clientes/', include('clientes.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    
    # API
    path('api/dashboard/stats/', api_dashboard_stats, name='api_dashboard_stats'),
]
