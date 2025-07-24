from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard_relatorios(request):
    """Dashboard de relatórios"""
    return render(request, 'relatorios/dashboard_simple.html')

@login_required
def relatorio_vendas(request):
    """Relatório de vendas"""
    return render(request, 'relatorios/vendas.html')

@login_required
def relatorio_produtos(request):
    """Relatório de produtos"""
    return render(request, 'relatorios/produtos.html')

@login_required
def relatorio_test(request):
    """Teste de relatórios"""
    return HttpResponse("<h1>Relatórios funcionando!</h1><p>Sistema OK</p>")
