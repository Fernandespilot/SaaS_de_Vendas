from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import JsonResponse
from .models import Produto, GrupoProduto


@login_required
def listar_produtos(request):
    """Lista todos os produtos"""
    try:
        produtos = Produto.objects.all()
        
        # Adicionar cores de status para cada produto
        for produto in produtos:
            if hasattr(produto, 'categoria') and produto.categoria:
                produto.status_color = 'primary'
            else:
                produto.status_color = 'secondary'
        
        context = {
            'produtos': produtos,
        }
        
        return render(request, 'produtos/lista_produtos.html', context)
    
    except Exception as e:
        context = {
            'produtos': [],
        }
        return render(request, 'produtos/lista_produtos.html', context)


@login_required
def detalhar_produto(request, produto_id):
    """Exibe detalhes de um produto específico"""
    try:
        produto = get_object_or_404(Produto, id=produto_id)
        context = {
            'produto': produto,
        }
        return render(request, 'produtos/detalhe.html', context)
    except Exception as e:
        return render(request, 'produtos/erro.html', {'erro': str(e)})


@login_required
def buscar_produtos(request):
    """API para buscar produtos via AJAX"""
    try:
        query = request.GET.get('q', '')
        produtos = Produto.objects.filter(nome__icontains=query)[:10]
        
        data = []
        for produto in produtos:
            data.append({
                'id': produto.id,
                'nome': produto.nome,
                'preco': str(produto.preco),
                'estoque': produto.estoque,
            })
        
        return JsonResponse({'produtos': data})
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=500)


@login_required
def get_produto_info(request, produto_id):
    """Retorna informações de um produto específico via AJAX"""
    try:
        produto = get_object_or_404(Produto, id=produto_id)
        data = {
            'id': produto.id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': str(produto.preco),
            'estoque': produto.estoque,
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=500)
