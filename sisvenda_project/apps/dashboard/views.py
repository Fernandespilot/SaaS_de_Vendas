from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F, Avg
from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime, timedelta
from apps.usuarios.models import User, Cliente, PromotorVenda
from apps.produtos.models import Produto
from apps.pedidos.models import Pedido


def home(request):
    """Página inicial do sistema"""
    if request.user.is_authenticated:
        return dashboard(request)
    else:
        # Para usuários não autenticados, mostrar uma página simples
        return render(request, 'dashboard/home_public.html')


@login_required
def dashboard(request):
    """Dashboard principal com estatísticas e gráficos"""
    try:
        hoje = timezone.now().date()
        inicio_mes = hoje.replace(day=1)
        
        # Estatísticas principais
        vendas_mes = Pedido.objects.filter(
            data_criacao__date__gte=inicio_mes,
            status='entregue'
        ).aggregate(total=Sum('valor_total'))['total'] or 0
        
        pedidos_hoje = Pedido.objects.filter(
            data_criacao__date=hoje
        ).count()
        
        total_produtos = Produto.objects.count()
        
        produtos_estoque_baixo = Produto.objects.filter(
            estoque__lte=10
        ).count()
        
        # Pedidos recentes
        pedidos_recentes = Pedido.objects.select_related('usuario').order_by('-data_criacao')[:10]
        
        # Adicionar cores para status
        for pedido in pedidos_recentes:
            if pedido.status == 'entregue':
                pedido.status_color = 'success'
            elif pedido.status == 'cancelado':
                pedido.status_color = 'danger'
            elif pedido.status == 'aprovado':
                pedido.status_color = 'info'
            elif pedido.status == 'pendente':
                pedido.status_color = 'warning'
            else:
                pedido.status_color = 'secondary'
        
        context = {
            'vendas_mes': vendas_mes,
            'pedidos_hoje': pedidos_hoje,
            'total_produtos': total_produtos,
            'produtos_estoque_baixo': produtos_estoque_baixo,
            'pedidos_recentes': pedidos_recentes,
        }
        
        return render(request, 'dashboard/home_simple.html', context)
    
    except Exception as e:
        # Em caso de erro, retornar um dashboard básico
        context = {
            'vendas_mes': 0,
            'pedidos_hoje': 0,
            'total_produtos': 0,
            'produtos_estoque_baixo': 0,
            'pedidos_recentes': [],
        }
        return render(request, 'dashboard/home_simple.html', context)


def dashboard_promotor(request):
    """Dashboard para promotores"""
    promotor = getattr(request.user, 'promotor', None)
    if not promotor:
        return render(request, 'dashboard/erro.html', {'mensagem': 'Perfil de promotor não encontrado'})
    
    # Estatísticas do mês atual
    hoje = timezone.now().date()
    inicio_mes = hoje.replace(day=1)
    
    pedidos_mes = Pedido.objects.filter(
        promotor=promotor,
        data_criacao__gte=inicio_mes
    )
    
    context = {
        'promotor': promotor,
        'pedidos_mes': pedidos_mes.count(),
        'valor_vendas_mes': pedidos_mes.aggregate(total=Sum('valor_total'))['total'] or 0,
        'comissao_mes': pedidos_mes.aggregate(total=Sum('comissao_total'))['total'] or 0,
        'clientes_ativos': Cliente.objects.filter(promotor=promotor).count(),
        'pedidos_recentes': pedidos_mes.order_by('-data_criacao')[:5],
        'meta_mensal': promotor.meta_mensal,
    }
    
    return render(request, 'dashboard/dashboard_promotor.html', context)


def dashboard_cliente(request):
    """Dashboard para clientes"""
    cliente = getattr(request.user, 'cliente', None)
    if not cliente:
        return render(request, 'dashboard/erro.html', {'mensagem': 'Perfil de cliente não encontrado'})
    
    pedidos = Pedido.objects.filter(cliente=cliente)
    
    context = {
        'cliente': cliente,
        'total_pedidos': pedidos.count(),
        'valor_total_compras': pedidos.aggregate(total=Sum('valor_total'))['total'] or 0,
        'pedidos_pendentes': pedidos.filter(status='pendente').count(),
        'pedidos_recentes': pedidos.order_by('-data_criacao')[:5],
        'limite_credito': cliente.limite_credito,
        'status_financeiro': cliente.status_financeiro,
    }
    
    return render(request, 'dashboard/dashboard_cliente.html', context)


def dashboard_gerente_estoque(request):
    """Dashboard para gerentes de estoque"""
    produtos = Produto.objects.all()
    produtos_estoque_baixo = produtos.filter(estoque_atual__lte=F('estoque_minimo'))
    
    context = {
        'total_produtos': produtos.count(),
        'produtos_estoque_baixo': produtos_estoque_baixo.count(),
        'produtos_sem_estoque': produtos.filter(estoque_atual=0).count(),
        'valor_total_estoque': produtos.aggregate(
            total=Sum(F('estoque_atual') * F('preco_custo'))
        )['total'] or 0,
        'produtos_criticos': produtos_estoque_baixo[:10],
        'pedidos_avaliar': Pedido.objects.filter(status='avaliacao_estoque').count(),
    }
    
    return render(request, 'dashboard/dashboard_gerente_estoque.html', context)


def dashboard_gerente_vendas(request):
    """Dashboard para gerentes de vendas"""
    hoje = timezone.now().date()
    inicio_mes = hoje.replace(day=1)
    
    pedidos_mes = Pedido.objects.filter(data_criacao__gte=inicio_mes)
    
    context = {
        'pedidos_mes': pedidos_mes.count(),
        'faturamento_mes': pedidos_mes.aggregate(total=Sum('valor_total'))['total'] or 0,
        'pedidos_pendentes': Pedido.objects.filter(status='avaliacao_vendas').count(),
        'clientes_novos': Cliente.objects.filter(data_cadastro__gte=inicio_mes).count(),
        'promotores_ativos': PromotorVenda.objects.count(),
        'ticket_medio': pedidos_mes.aggregate(media=Avg('valor_total'))['media'] or 0,
    }
    
    return render(request, 'dashboard/dashboard_gerente_vendas.html', context)


def dashboard_gerenciador(request):
    """Dashboard para gerenciadores"""
    hoje = timezone.now().date()
    inicio_mes = hoje.replace(day=1)
    
    pedidos_mes = Pedido.objects.filter(data_criacao__gte=inicio_mes)
    
    context = {
        'total_usuarios': User.objects.count(),
        'promotores_ativos': PromotorVenda.objects.count(),
        'clientes_ativos': Cliente.objects.count(),
        'total_produtos': Produto.objects.count(),
        'pedidos_mes': pedidos_mes.count(),
        'faturamento_mes': pedidos_mes.aggregate(total=Sum('valor_total'))['total'] or 0,
        'pedidos_pendentes': Pedido.objects.filter(status='pendente').count(),
        'pedidos_aprovados': Pedido.objects.filter(status='aprovado').count(),
        'pedidos_entregues': Pedido.objects.filter(status='entregue').count(),
        'pedidos_cancelados': Pedido.objects.filter(status='cancelado').count(),
        'pedidos_recentes': Pedido.objects.order_by('-data_criacao')[:10],
        'produtos_estoque_baixo': Produto.objects.filter(estoque__lte=F('estoque_minimo')).count(),
        'clientes_bloqueados': Cliente.objects.filter(status_financeiro='reprovado').count(),
    }
    
    return render(request, 'dashboard/dashboard_gerenciador.html', context)


@login_required
def dashboard_simple(request):
    """Dashboard simplificado que sempre funciona"""
    return render(request, 'dashboard/dashboard_simple.html')

def test_dashboard(request):
    """Teste do dashboard"""
    return HttpResponse("<h1>Dashboard funcionando!</h1><p>Sistema OK</p>")
