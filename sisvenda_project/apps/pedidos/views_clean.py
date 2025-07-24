from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count
from django.http import JsonResponse
from .models import Pedido


@login_required
def listar_pedidos(request):
    """Lista todos os pedidos"""
    try:
        pedidos = Pedido.objects.select_related('usuario').all()
        
        # Adicionar cores de status para cada pedido
        for pedido in pedidos:
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
        
        # Estatísticas
        total_pedidos = pedidos.count()
        pedidos_aprovados = pedidos.filter(status='aprovado').count()
        pedidos_pendentes = pedidos.filter(status='pendente').count()
        valor_total = pedidos.aggregate(total=Sum('valor_total'))['total'] or 0
        
        context = {
            'pedidos': pedidos,
            'total_pedidos': total_pedidos,
            'pedidos_aprovados': pedidos_aprovados,
            'pedidos_pendentes': pedidos_pendentes,
            'valor_total': valor_total,
        }
        
        return render(request, 'pedidos/lista_simple.html', context)
    
    except Exception as e:
        context = {
            'pedidos': [],
            'total_pedidos': 0,
            'pedidos_aprovados': 0,
            'pedidos_pendentes': 0,
            'valor_total': 0,
        }
        return render(request, 'pedidos/lista_simple.html', context)


@login_required
def detalhar_pedido(request, pedido_id):
    """Exibe detalhes de um pedido"""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    context = {
        'pedido': pedido
    }
    
    return render(request, 'pedidos/detalhar_pedido.html', context)
