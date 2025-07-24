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
            if produto.categoria:
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
            'preco': float(produto.preco_final),
            'estoque': produto.estoque_atual,
            'status': produto.estoque_status
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
        'preco': float(produto.preco_final),
        'estoque': produto.estoque_atual,
        'unidade': produto.unidade,
        'promocao': produto.promocao,
        'preco_promocao': float(produto.preco_promocao) if produto.preco_promocao else None,
        'status': produto.estoque_status
    }
    
    return JsonResponse(data)


@login_required
def lista_produtos(request):
    """Lista todos os produtos com filtros e paginação"""
    produtos = Produto.objects.select_related('grupo').all()
    grupos = GrupoProduto.objects.filter(ativo=True)
    
    # Filtros
    search = request.GET.get('search', '')
    grupo_id = request.GET.get('grupo', '')
    status = request.GET.get('status', '')
    
    if search:
        produtos = produtos.filter(
            Q(nome__icontains=search) | 
            Q(codigo__icontains=search) |
            Q(descricao__icontains=search)
        )
    
    if grupo_id:
        produtos = produtos.filter(grupo_id=grupo_id)
    
    if status == 'ativo':
        produtos = produtos.filter(ativo=True)
    elif status == 'inativo':
        produtos = produtos.filter(ativo=False)
    
    # Ordenação
    produtos = produtos.order_by('nome')
    
    # Paginação
    paginator = Paginator(produtos, 20)
    page = request.GET.get('page')
    produtos_page = paginator.get_page(page)
    
    context = {
        'produtos': produtos_page,
        'grupos': grupos,
        'search': search,
        'grupo_selecionado': grupo_id,
        'status_selecionado': status,
    }
    
    return render(request, 'produtos/lista.html', context)
