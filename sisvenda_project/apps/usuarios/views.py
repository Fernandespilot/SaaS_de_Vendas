from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User, Cliente, PromotorVenda, Municipio
from .forms import ClienteForm, PromotorForm


@login_required
def dashboard_usuarios(request):
    """Dashboard principal de usuários"""
    total_clientes = Cliente.objects.count()
    total_promotores = PromotorVenda.objects.count()
    total_usuarios = User.objects.count()
    
    context = {
        'total_clientes': total_clientes,
        'total_promotores': total_promotores,
        'total_usuarios': total_usuarios,
    }
    return render(request, 'usuarios/dashboard.html', context)


@login_required
def listar_clientes(request):
    """Lista todos os clientes"""
    busca = request.GET.get('busca', '')
    municipio_id = request.GET.get('municipio', '')
    
    clientes = Cliente.objects.select_related('user', 'municipio', 'promotor__user').all().order_by('user__first_name')
    
    if busca:
        clientes = clientes.filter(
            Q(user__first_name__icontains=busca) |
            Q(user__last_name__icontains=busca) |
            Q(user__email__icontains=busca)
        )
    
    if municipio_id:
        clientes = clientes.filter(municipio_id=municipio_id)
    
    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    clientes_paginados = paginator.get_page(page)
    
    municipios = Municipio.objects.all().order_by('nome')
    
    context = {
        'clientes': clientes_paginados,
        'municipios': municipios,
        'busca': busca,
        'municipio_selecionado': municipio_id
    }
    
    return render(request, 'usuarios/listar_clientes.html', context)


@login_required
def cadastrar_cliente(request):
    """Cadastra um novo cliente"""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente {cliente.user.get_full_name()} cadastrado com sucesso!')
            return redirect('usuarios:listar_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'usuarios/cadastrar_cliente.html', {'form': form})


@login_required
def listar_promotores(request):
    """Lista todos os promotores"""
    promotores = PromotorVenda.objects.select_related('user', 'municipio').all().order_by('user__first_name')
    
    paginator = Paginator(promotores, 10)
    page = request.GET.get('page')
    promotores_paginados = paginator.get_page(page)
    
    return render(request, 'usuarios/listar_promotores.html', {'promotores': promotores_paginados})


@login_required
def cadastrar_promotor(request):
    """Cadastra um novo promotor"""
    if request.method == 'POST':
        form = PromotorForm(request.POST)
        if form.is_valid():
            promotor = form.save()
            messages.success(request, f'Promotor {promotor.user.get_full_name()} cadastrado com sucesso!')
            return redirect('usuarios:listar_promotores')
    else:
        form = PromotorForm()
    
    return render(request, 'usuarios/cadastrar_promotor.html', {'form': form})
