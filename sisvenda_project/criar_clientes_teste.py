#!/usr/bin/env python
"""
Script para criar dados de teste para clientes
Executar: python manage.py shell < criar_clientes_teste.py
"""

from clientes.models import Cliente
from django.db import transaction

def criar_clientes_teste():
    """Criar clientes de teste"""
    
    # Limpar clientes existentes
    Cliente.objects.all().delete()
    
    clientes_teste = [
        {
            'nome': 'João Silva Santos',
            'tipo_pessoa': 'F',
            'documento': '12345678901',
            'rg_ie': '123456789',
            'email': 'joao.silva@email.com',
            'telefone': '(11) 3456-7890',
            'celular': '(11) 99876-5432',
            'cep': '01310-100',
            'endereco': 'Avenida Paulista',
            'numero': '1000',
            'complemento': 'Apto 101',
            'bairro': 'Bela Vista',
            'cidade': 'São Paulo',
            'estado': 'SP',
            'limite_credito': 5000.00,
            'desconto_padrao': 5.0,
            'observacoes': 'Cliente VIP - Pagamento sempre em dia'
        },
        {
            'nome': 'Empresa ABC Ltda',
            'nome_fantasia': 'ABC Comércio',
            'tipo_pessoa': 'J',
            'documento': '12345678000199',
            'rg_ie': '123456789',
            'email': 'contato@abccomercio.com.br',
            'telefone': '(11) 3333-4444',
            'celular': '(11) 99999-8888',
            'cep': '04567-890',
            'endereco': 'Rua das Empresas',
            'numero': '500',
            'bairro': 'Vila Olimpia',
            'cidade': 'São Paulo',
            'estado': 'SP',
            'limite_credito': 15000.00,
            'desconto_padrao': 10.0,
            'observacoes': 'Empresa parceira - Pedidos grandes'
        },
        {
            'nome': 'Maria Oliveira Costa',
            'tipo_pessoa': 'F',
            'documento': '98765432100',
            'rg_ie': '987654321',
            'email': 'maria.costa@gmail.com',
            'telefone': '(21) 2222-3333',
            'celular': '(21) 98765-4321',
            'cep': '22070-900',
            'endereco': 'Avenida Copacabana',
            'numero': '1500',
            'bairro': 'Copacabana',
            'cidade': 'Rio de Janeiro',
            'estado': 'RJ',
            'limite_credito': 3000.00,
            'desconto_padrao': 3.0,
            'observacoes': 'Cliente desde 2020'
        },
        {
            'nome': 'TechSol Soluções Ltda',
            'nome_fantasia': 'TechSol',
            'tipo_pessoa': 'J',
            'documento': '87654321000177',
            'rg_ie': '876543210',
            'email': 'vendas@techsol.com.br',
            'telefone': '(85) 3456-7890',
            'celular': '(85) 99876-5432',
            'cep': '60115-000',
            'endereco': 'Rua da Tecnologia',
            'numero': '300',
            'bairro': 'Meireles',
            'cidade': 'Fortaleza',
            'estado': 'CE',
            'limite_credito': 20000.00,
            'desconto_padrao': 15.0,
            'status': 'ativo',
            'observacoes': 'Empresa de tecnologia - Compras recorrentes'
        },
        {
            'nome': 'Carlos Eduardo Lima',
            'tipo_pessoa': 'F',
            'documento': '11122233344',
            'rg_ie': '111222333',
            'email': 'carlos.lima@hotmail.com',
            'telefone': '(31) 3333-4444',
            'cep': '30112-000',
            'endereco': 'Rua das Flores',
            'numero': '200',
            'bairro': 'Centro',
            'cidade': 'Belo Horizonte',
            'estado': 'MG',
            'limite_credito': 2000.00,
            'desconto_padrao': 2.0,
            'status': 'inativo',
            'observacoes': 'Cliente temporariamente inativo'
        }
    ]
    
    with transaction.atomic():
        for cliente_data in clientes_teste:
            cliente = Cliente.objects.create(**cliente_data)
            print(f"Cliente criado: {cliente.codigo} - {cliente.nome}")

if __name__ == '__main__':
    criar_clientes_teste()
    print(f"\nTotal de clientes criados: {Cliente.objects.count()}")
    print("Dados de teste criados com sucesso!")
