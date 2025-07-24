"""
Views para o app de pedidos
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Pedido, ItemPedido
from .forms import PedidoForm, ItemPedidoForm
from apps.produtos.models import Produto

@login_required
def pedidos_list(request):
    """Lista todos os pedidos"""
    try:
        pedidos = Pedido.objects.select_related('usuario').order_by('-data_criacao')
        
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
        pedidos_pendentes = pedidos.filter(status='pendente').count()
        pedidos_aprovados = pedidos.filter(status='aprovado').count()
        valor_total = sum(pedido.valor_total or 0 for pedido in pedidos)
        
        context = {
            'pedidos': pedidos,
            'total_pedidos': total_pedidos,
            'pedidos_pendentes': pedidos_pendentes,
            'pedidos_aprovados': pedidos_aprovados,
            'valor_total': valor_total,
        }
        
        return render(request, 'pedidos/lista_simple.html', context)
    
    except Exception as e:
        context = {
            'pedidos': [],
            'total_pedidos': 0,
            'pedidos_pendentes': 0,
            'pedidos_aprovados': 0,
            'valor_total': 0,
        }
        return render(request, 'pedidos/lista_simple.html', context)


@login_required
def pedido_create(request):
    """Cria um novo pedido"""
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.vendedor = request.user
            pedido.save()
            messages.success(request, 'Pedido criado com sucesso!')
            return redirect('pedidos:pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm()
    
    context = {
        'form': form,
        'title': 'Novo Pedido',
    }
    return render(request, 'pedidos/pedido_form.html', context)

@login_required
def pedido_detail(request, pk):
    """Detalhe de um pedido"""
    pedido = get_object_or_404(Pedido, pk=pk)
    itens = pedido.itens.select_related('produto').all()
    
    context = {
        'pedido': pedido,
        'itens': itens,
    }
    return render(request, 'pedidos/pedido_detail.html', context)

@login_required
def pedido_update(request, pk):
    """Atualiza um pedido"""
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido atualizado com sucesso!')
            return redirect('pedidos:pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm(instance=pedido)
    
    context = {
        'form': form,
        'pedido': pedido,
        'title': 'Editar Pedido',
    }
    return render(request, 'pedidos/pedido_form.html', context)

@login_required
def pedido_delete(request, pk):
    """Exclui um pedido"""
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido excluído com sucesso!')
        return redirect('pedidos:pedidos_list')
    
    context = {
        'pedido': pedido,
    }
    return render(request, 'pedidos/pedido_confirm_delete.html', context)

@login_required
def pedido_status(request, pk):
    """Atualiza o status de um pedido via AJAX"""
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, pk=pk)
        novo_status = request.POST.get('status')
        
        if novo_status in dict(Pedido.STATUS_CHOICES):
            pedido.status = novo_status
            pedido.save()
            
            return JsonResponse({
                'success': True,
                'message': f'Status atualizado para {pedido.get_status_display()}',
                'status': novo_status,
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Status inválido',
            })
    
    return JsonResponse({'success': False, 'message': 'Método não permitido'})

@login_required
def lista_pedidos(request):
    """Lista todos os pedidos com filtros e paginação"""
    pedidos = Pedido.objects.select_related('usuario', 'vendedor').all()
    
    # Estatísticas
    stats = {
        'pendentes': Pedido.objects.filter(status='pendente').count(),
        'em_avaliacao': Pedido.objects.filter(status__in=['avaliacao_estoque', 'avaliacao_vendas']).count(),
        'aprovados': Pedido.objects.filter(status='aprovado').count(),
        'entregues': Pedido.objects.filter(status='entregue').count(),
    }
    
    # Filtros
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    periodo = request.GET.get('periodo', '')
    
    if search:
        pedidos = pedidos.filter(
            Q(codigo__icontains=search) |
            Q(usuario__first_name__icontains=search) |
            Q(usuario__last_name__icontains=search) |
            Q(usuario__email__icontains=search)
        )
    
    if status:
        pedidos = pedidos.filter(status=status)
    
    if periodo:
        from datetime import datetime, timedelta
        hoje = datetime.now()
        if periodo == 'hoje':
            pedidos = pedidos.filter(data_criacao__date=hoje.date())
        elif periodo == '7dias':
            pedidos = pedidos.filter(data_criacao__gte=hoje - timedelta(days=7))
        elif periodo == '30dias':
            pedidos = pedidos.filter(data_criacao__gte=hoje - timedelta(days=30))
        elif periodo == '90dias':
            pedidos = pedidos.filter(data_criacao__gte=hoje - timedelta(days=90))
    
    # Ordenação
    pedidos = pedidos.order_by('-data_criacao')
    
    # Paginação
    paginator = Paginator(pedidos, 20)
    page = request.GET.get('page')
    pedidos_page = paginator.get_page(page)
    
    context = {
        'pedidos': pedidos_page,
        'stats': stats,
        'search': search,
        'status_selecionado': status,
        'periodo_selecionado': periodo,
    }
    
    return render(request, 'pedidos/lista.html', context)
