from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Pedido

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-data_criacao')
    return render(request, 'pedidos/lista_pedidos_simple.html', {
        'pedidos': pedidos
    })

@login_required
def ver_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/ver_pedido.html', {
        'pedido': pedido
    })

@login_required
def novo_pedido(request):
    if request.method == 'POST':
        try:
            from datetime import datetime
            import json
            
            # Criar pedido principal
            pedido = Pedido.objects.create(
                usuario=request.user,
                vendedor=request.user,
                cliente_nome=request.POST.get('cliente_nome', ''),
                cliente_email=request.POST.get('cliente_email', ''),
                cliente_telefone=request.POST.get('cliente_telefone', ''),
                status='pendente',
                observacoes=request.POST.get('observacoes', '')
            )
            
            # Processar data de entrega se fornecida
            data_entrega = request.POST.get('data_entrega')
            if data_entrega:
                pedido.data_entrega = datetime.strptime(data_entrega, '%Y-%m-%d').date()
                pedido.save()
            
            # Processar produtos do pedido
            produtos_adicionados = 0
            for key, value in request.POST.items():
                if key.startswith('produtos[') and key.endswith(']'):
                    try:
                        produto_data = json.loads(value)
                        from apps.produtos.models import Produto
                        
                        produto = Produto.objects.get(id=produto_data['id'])
                        
                        # Criar item do pedido
                        from .models import ItemPedido
                        ItemPedido.objects.create(
                            pedido=pedido,
                            produto=produto,
                            quantidade=produto_data['quantidade'],
                            preco_unitario=produto_data['preco']
                        )
                        produtos_adicionados += 1
                        
                    except (json.JSONDecodeError, Produto.DoesNotExist, KeyError) as e:
                        print(f"Erro ao processar produto: {e}")
                        continue
            
            # Recalcular totais
            pedido.calcular_totais()
            
            if produtos_adicionados > 0:
                messages.success(request, f'Pedido {pedido.codigo} criado com sucesso com {produtos_adicionados} produtos!')
                return redirect('pedidos:ver', pedido_id=pedido.id)
            else:
                pedido.delete()
                messages.error(request, 'Erro: Nenhum produto válido foi adicionado ao pedido.')
                
        except Exception as e:
            messages.error(request, f'Erro ao criar pedido: {str(e)}')
    
    # Buscar dados para o formulário
    from apps.produtos.models import Produto
    produtos = Produto.objects.filter(ativo=True).order_by('nome')
    
    context = {
        'produtos': produtos,
        'clientes': [],
    }
    
    # Se temos clientes disponíveis, incluir também
    try:
        from clientes.models import Cliente
        clientes = Cliente.objects.filter(status='ativo').order_by('nome')
        context['clientes'] = clientes
    except ImportError:
        # Se a app clientes não estiver disponível
        context['clientes'] = []
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")
        context['clientes'] = []
    
    return render(request, 'pedidos/novo_pedido.html', context)

@login_required
def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        # Processar edição
        pedido.cliente_nome = request.POST.get('cliente_nome', pedido.cliente_nome)
        pedido.cliente_email = request.POST.get('cliente_email', pedido.cliente_email)
        pedido.status = request.POST.get('status', pedido.status)
        
        try:
            pedido.save()
            messages.success(request, 'Pedido atualizado com sucesso!')
            return redirect('pedidos:ver', pedido_id=pedido.id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar pedido: {str(e)}')
    
    return render(request, 'pedidos/editar_pedido.html', {
        'pedido': pedido
    })

@login_required
def imprimir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/imprimir_pedido.html', {
        'pedido': pedido
    })
