from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import models
from .models import Cliente
import re


@login_required
def lista_clientes(request):
    """Lista todos os clientes com filtros e paginação"""
    clientes = Cliente.objects.all()
    
    # Filtros
    search = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    tipo_filter = request.GET.get('tipo', '')
    
    if search:
        clientes = clientes.filter(
            models.Q(nome__icontains=search) |
            models.Q(documento__icontains=search) |
            models.Q(email__icontains=search)
        )
    
    if status_filter:
        clientes = clientes.filter(status=status_filter)
        
    if tipo_filter:
        clientes = clientes.filter(tipo_pessoa=tipo_filter)
    
    # Paginação
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'clientes/lista_clientes.html', {
        'clientes': page_obj,
        'search': search,
        'status_filter': status_filter,
        'tipo_filter': tipo_filter,
    })


@login_required
def ver_cliente(request, cliente_id):
    """Visualizar detalhes de um cliente"""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/ver_cliente.html', {
        'cliente': cliente
    })


@login_required
def novo_cliente(request):
    """Cadastrar novo cliente"""
    if request.method == 'POST':
        try:
            # Validar documento
            documento = request.POST.get('documento', '').strip()
            documento = re.sub(r'[^0-9]', '', documento)  # Remove caracteres não numéricos
            
            if len(documento) not in [11, 14]:
                messages.error(request, 'Documento deve ter 11 dígitos (CPF) ou 14 dígitos (CNPJ)')
                return render(request, 'clientes/novo_cliente.html')
            
            # Criar cliente
            cliente = Cliente.objects.create(
                nome=request.POST.get('nome'),
                nome_fantasia=request.POST.get('nome_fantasia', ''),
                tipo_pessoa=request.POST.get('tipo_pessoa', 'F'),
                documento=documento,
                rg_ie=request.POST.get('rg_ie', ''),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
                celular=request.POST.get('celular', ''),
                cep=request.POST.get('cep'),
                endereco=request.POST.get('endereco'),
                numero=request.POST.get('numero'),
                complemento=request.POST.get('complemento', ''),
                bairro=request.POST.get('bairro'),
                cidade=request.POST.get('cidade'),
                estado=request.POST.get('estado'),
                limite_credito=float(request.POST.get('limite_credito', 0)),
                desconto_padrao=float(request.POST.get('desconto_padrao', 0)),
                observacoes=request.POST.get('observacoes', ''),
                data_nascimento=request.POST.get('data_nascimento') or None
            )
            
            messages.success(request, f'Cliente "{cliente.nome}" criado com sucesso!')
            return redirect('clientes:lista')
            
        except Exception as e:
            messages.error(request, f'Erro ao criar cliente: {str(e)}')
    
    return render(request, 'clientes/novo_cliente.html')


@login_required
def editar_cliente(request, cliente_id):
    """Editar cliente existente"""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        try:
            # Validar documento
            documento = request.POST.get('documento', '').strip()
            documento = re.sub(r'[^0-9]', '', documento)
            
            if len(documento) not in [11, 14]:
                messages.error(request, 'Documento deve ter 11 dígitos (CPF) ou 14 dígitos (CNPJ)')
                return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})
            
            # Atualizar cliente
            cliente.nome = request.POST.get('nome', cliente.nome)
            cliente.nome_fantasia = request.POST.get('nome_fantasia', cliente.nome_fantasia)
            cliente.tipo_pessoa = request.POST.get('tipo_pessoa', cliente.tipo_pessoa)
            cliente.documento = documento
            cliente.rg_ie = request.POST.get('rg_ie', cliente.rg_ie)
            cliente.email = request.POST.get('email', cliente.email)
            cliente.telefone = request.POST.get('telefone', cliente.telefone)
            cliente.celular = request.POST.get('celular', cliente.celular)
            cliente.cep = request.POST.get('cep', cliente.cep)
            cliente.endereco = request.POST.get('endereco', cliente.endereco)
            cliente.numero = request.POST.get('numero', cliente.numero)
            cliente.complemento = request.POST.get('complemento', cliente.complemento)
            cliente.bairro = request.POST.get('bairro', cliente.bairro)
            cliente.cidade = request.POST.get('cidade', cliente.cidade)
            cliente.estado = request.POST.get('estado', cliente.estado)
            cliente.limite_credito = float(request.POST.get('limite_credito', cliente.limite_credito))
            cliente.desconto_padrao = float(request.POST.get('desconto_padrao', cliente.desconto_padrao))
            cliente.observacoes = request.POST.get('observacoes', cliente.observacoes)
            cliente.status = request.POST.get('status', cliente.status)
            
            data_nascimento = request.POST.get('data_nascimento')
            if data_nascimento:
                cliente.data_nascimento = data_nascimento
            
            cliente.save()
            
            messages.success(request, f'Cliente "{cliente.nome}" atualizado com sucesso!')
            return redirect('clientes:ver', cliente_id=cliente.id)
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar cliente: {str(e)}')
    
    return render(request, 'clientes/editar_cliente.html', {
        'cliente': cliente
    })


@login_required
def excluir_cliente(request, cliente_id):
    """Excluir cliente"""
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id=cliente_id)
            nome = cliente.nome
            cliente.delete()
            return JsonResponse({'success': True, 'message': f'Cliente "{nome}" excluído com sucesso!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})


@login_required
def buscar_cep(request):
    """API para buscar CEP via ViaCEP"""
    cep = request.GET.get('cep', '').strip()
    cep = re.sub(r'[^0-9]', '', cep)
    
    if len(cep) != 8:
        return JsonResponse({'success': False, 'error': 'CEP deve ter 8 dígitos'})
    
    try:
        import urllib.request
        import json
        
        with urllib.request.urlopen(f'https://viacep.com.br/ws/{cep}/json/') as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if 'erro' in data:
            return JsonResponse({'success': False, 'error': 'CEP não encontrado'})
        
        return JsonResponse({
            'success': True,
            'endereco': data.get('logradouro', ''),
            'bairro': data.get('bairro', ''),
            'cidade': data.get('localidade', ''),
            'estado': data.get('uf', '')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'Erro ao buscar CEP'})
