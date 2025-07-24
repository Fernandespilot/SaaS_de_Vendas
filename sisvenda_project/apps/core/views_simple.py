# views_simple.py - Views simplificadas para o sistema

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse

@login_required
def dashboard_view(request):
    """Dashboard principal do sistema"""
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/home_simple.html', context)

@login_required
def produtos_view(request):
    """Lista de produtos"""
    context = {
        'user': request.user,
    }
    return render(request, 'produtos/lista_produtos_simple.html', context)

@login_required
def pedidos_view(request):
    """Lista de pedidos"""
    context = {
        'user': request.user,
    }
    return render(request, 'pedidos/lista_pedidos_simple.html', context)

@login_required
def relatorios_view(request):
    """Relatórios do sistema"""
    context = {
        'user': request.user,
    }
    return render(request, 'relatorios/dashboard_simple.html', context)

def login_view(request):
    """View de login personalizada"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.first_name or user.username}!')
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'registration/login_simple.html')

# Views para operações CRUD (placeholder)
@login_required
def produto_novo(request):
    """Criar novo produto"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('/produtos/')

@login_required
def produto_editar(request, id):
    """Editar produto"""
    messages.info(request, f'Editando produto ID: {id} - Em desenvolvimento.')
    return redirect('/produtos/')

@login_required
def produto_ver(request, id):
    """Ver detalhes do produto"""
    messages.info(request, f'Visualizando produto ID: {id} - Em desenvolvimento.')
    return redirect('/produtos/')

@login_required
def pedido_novo(request):
    """Criar novo pedido"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('/pedidos/')

@login_required
def pedido_editar(request, id):
    """Editar pedido"""
    messages.info(request, f'Editando pedido ID: {id} - Em desenvolvimento.')
    return redirect('/pedidos/')

@login_required
def pedido_ver(request, id):
    """Ver detalhes do pedido"""
    messages.info(request, f'Visualizando pedido ID: {id} - Em desenvolvimento.')
    return redirect('/pedidos/')

# API para dados dinâmicos (placeholder)
@login_required
def api_dashboard_stats(request):
    """API para estatísticas do dashboard"""
    data = {
        'total_vendas': 'R$ 12.540,00',
        'pedidos_hoje': 45,
        'produtos': 1234,
        'clientes': 567
    }
    return JsonResponse(data)
