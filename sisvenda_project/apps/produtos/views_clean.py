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
        
        return render(request, 'produtos/lista_simple.html', context)
    
    except Exception as e:
        context = {
            'produtos': [],
        }
        return render(request, 'produtos/lista_simple.html', context)


@login_required
def detalhar_produto(request, produto_id):
    """Exibe detalhes de um produto"""
    produto = get_object_or_404(Produto, id=produto_id)
    
    context = {
        'produto': produto
    }
    
    return render(request, 'produtos/detalhar_produto.html', context)


@login_required
def buscar_produtos(request):
    """API para buscar produtos (usado no autocomplete)"""
    termo = request.GET.get('q', '')
    
    produtos = Produto.objects.filter(
        Q(codigo__icontains=termo) | Q(nome__icontains=termo),
        ativo=True
    )[:10]
    
    resultados = []
    for produto in produtos:
        resultados.append({
            'id': produto.id,
            'codigo': produto.codigo,
            'nome': produto.nome,
            'preco': float(produto.preco),
            'estoque': produto.estoque,
        })
    
    return JsonResponse(resultados, safe=False)


@login_required
def get_produto_info(request, produto_id):
    """API para obter informações detalhadas de um produto"""
    produto = get_object_or_404(Produto, id=produto_id)
    
    data = {
        'id': produto.id,
        'codigo': produto.codigo,
        'nome': produto.nome,
        'preco': float(produto.preco),
        'estoque': produto.estoque,
        'unidade': produto.unidade,
    }
    
    return JsonResponse(data)
