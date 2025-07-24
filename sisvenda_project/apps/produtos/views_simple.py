from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Produto, GrupoProduto

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos_simple.html', {
        'produtos': produtos
    })

@login_required
def ver_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/ver_produto.html', {
        'produto': produto
    })

@login_required
def novo_produto(request):
    if request.method == 'POST':
        try:
            # Buscar ou criar grupo padrão
            grupo, created = GrupoProduto.objects.get_or_create(
                nome='Geral',
                defaults={'descricao': 'Grupo padrão para produtos'}
            )
            
            # Criar produto
            produto = Produto.objects.create(
                codigo=request.POST.get('codigo', f'PROD{Produto.objects.count() + 1:04d}'),
                nome=request.POST.get('nome'),
                descricao=request.POST.get('descricao', ''),
                grupo=grupo,
                preco_custo=float(request.POST.get('preco', 0)),
                preco_venda=float(request.POST.get('preco', 0)),
                estoque=int(request.POST.get('estoque', 0)),
                estoque_minimo=0,
                ativo=request.POST.get('ativo') == 'on'
            )
            
            messages.success(request, f'Produto "{produto.nome}" criado com sucesso!')
            return redirect('produtos:lista')
            
        except Exception as e:
            messages.error(request, f'Erro ao criar produto: {str(e)}')
    
    return render(request, 'produtos/novo_produto.html')

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        try:
            produto.nome = request.POST.get('nome', produto.nome)
            produto.descricao = request.POST.get('descricao', produto.descricao)
            produto.preco_custo = float(request.POST.get('preco', produto.preco_custo))
            produto.preco_venda = float(request.POST.get('preco', produto.preco_venda))
            produto.estoque = int(request.POST.get('estoque', produto.estoque))
            produto.ativo = request.POST.get('ativo') == 'on'
            produto.save()
            
            messages.success(request, f'Produto "{produto.nome}" atualizado com sucesso!')
            return redirect('produtos:ver', produto_id=produto.id)
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar produto: {str(e)}')
    
    return render(request, 'produtos/editar_produto.html', {
        'produto': produto
    })

@login_required
def excluir_produto(request, produto_id):
    if request.method == 'POST':
        try:
            produto = get_object_or_404(Produto, id=produto_id)
            nome = produto.nome
            produto.delete()
            return JsonResponse({'success': True, 'message': f'Produto "{nome}" excluído com sucesso!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})
