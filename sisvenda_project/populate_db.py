"""
Script para popular o banco de dados com dados de exemplo
"""
import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_dev')
django.setup()

from django.contrib.auth import get_user_model
from apps.usuarios.models import User
from apps.produtos.models import Produto, GrupoProduto
from apps.pedidos.models import Pedido, ItemPedido
from decimal import Decimal
from datetime import datetime, timedelta
import random

def criar_usuarios():
    """Criar usuários de exemplo"""
    
    # Criar superusuário se não existir
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@sisvenda.com',
            password='admin123',
            first_name='Administrador',
            last_name='Sistema',
            tipo_usuario='gerente'
        )
        print("✓ Superusuário criado: admin / admin123")
    
    # Criar gerente
    if not User.objects.filter(username='gerente').exists():
        User.objects.create_user(
            username='gerente',
            email='gerente@sisvenda.com',
            password='gerente123',
            first_name='João',
            last_name='Silva',
            tipo_usuario='gerente'
        )
        print("✓ Gerente criado: gerente / gerente123")
    
    # Criar vendedor
    if not User.objects.filter(username='vendedor').exists():
        User.objects.create_user(
            username='vendedor',
            email='vendedor@sisvenda.com',
            password='vendedor123',
            first_name='Maria',
            last_name='Santos',
            tipo_usuario='vendedor'
        )
        print("✓ Vendedor criado: vendedor / vendedor123")
    
    # Criar clientes
    clientes = [
        ('cliente1', 'Ana', 'Costa', 'ana@email.com'),
        ('cliente2', 'Carlos', 'Oliveira', 'carlos@email.com'),
        ('cliente3', 'Fernanda', 'Lima', 'fernanda@email.com'),
        ('cliente4', 'Pedro', 'Sousa', 'pedro@email.com'),
        ('cliente5', 'Juliana', 'Alves', 'juliana@email.com'),
    ]
    
    for username, first_name, last_name, email in clientes:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password='cliente123',
                first_name=first_name,
                last_name=last_name,
                tipo_usuario='cliente'
            )
            print(f"✓ Cliente criado: {username} / cliente123")

def criar_produtos():
    """Criar produtos de exemplo"""
    
    # Primeiro, criar grupos de produtos
    grupos_dados = [
        ('Eletrônicos', 'Produtos eletrônicos e tecnologia'),
        ('Móveis', 'Móveis e decoração'),
        ('Roupas', 'Vestuário e acessórios'),
        ('Livros', 'Livros e material educativo'),
        ('Casa', 'Utensílios domésticos'),
    ]
    
    grupos = {}
    for nome, descricao in grupos_dados:
        grupo, created = GrupoProduto.objects.get_or_create(
            nome=nome,
            defaults={'descricao': descricao}
        )
        grupos[nome] = grupo
        if created:
            print(f"✓ Grupo criado: {nome}")
    
    produtos = [
        ('P001', 'Smartphone Samsung Galaxy S23', 'Smartphone Android premium', grupos['Eletrônicos'], Decimal('2000.00'), Decimal('2500.00'), 15),
        ('P002', 'Notebook Dell Inspiron 15', 'Notebook para uso profissional', grupos['Eletrônicos'], Decimal('2800.00'), Decimal('3500.00'), 8),
        ('P003', 'Câmera Canon EOS R6', 'Câmera mirrorless profissional', grupos['Eletrônicos'], Decimal('3600.00'), Decimal('4500.00'), 5),
        ('P004', 'Headset Gamer HyperX', 'Headset gamer com microfone', grupos['Eletrônicos'], Decimal('280.00'), Decimal('350.00'), 25),
        ('P005', 'Mouse Logitech MX Master 3', 'Mouse sem fio para produtividade', grupos['Eletrônicos'], Decimal('360.00'), Decimal('450.00'), 30),
        ('P006', 'Teclado Mecânico Corsair K95', 'Teclado mecânico gamer RGB', grupos['Eletrônicos'], Decimal('640.00'), Decimal('800.00'), 12),
        ('P007', 'Monitor LG UltraWide 34"', 'Monitor ultrawide curvo', grupos['Eletrônicos'], Decimal('1440.00'), Decimal('1800.00'), 6),
        ('P008', 'Tablet iPad Pro 12.9"', 'Tablet profissional Apple', grupos['Eletrônicos'], Decimal('3200.00'), Decimal('4000.00'), 10),
        ('P009', 'Smartwatch Apple Watch Series 9', 'Relógio inteligente Apple', grupos['Eletrônicos'], Decimal('1760.00'), Decimal('2200.00'), 18),
        ('P010', 'Console PlayStation 5', 'Console de videogame Sony', grupos['Eletrônicos'], Decimal('2240.00'), Decimal('2800.00'), 4),
        ('P011', 'Camiseta Básica Branca', 'Camiseta 100% algodão', grupos['Roupas'], Decimal('18.00'), Decimal('45.00'), 100),
        ('P012', 'Calça Jeans Azul', 'Calça jeans tradicional', grupos['Roupas'], Decimal('48.00'), Decimal('120.00'), 50),
        ('P013', 'Tênis Nike Air Max', 'Tênis esportivo premium', grupos['Roupas'], Decimal('152.00'), Decimal('380.00'), 25),
        ('P014', 'Jaqueta de Couro Preta', 'Jaqueta de couro genuíno', grupos['Roupas'], Decimal('180.00'), Decimal('450.00'), 15),
        ('P015', 'Vestido Floral Verão', 'Vestido estampado feminino', grupos['Roupas'], Decimal('34.00'), Decimal('85.00'), 35),
        ('P016', 'Livro: Python para Iniciantes', 'Guia completo de Python', grupos['Livros'], Decimal('26.00'), Decimal('65.00'), 40),
        ('P017', 'Livro: Clean Code', 'Boas práticas de programação', grupos['Livros'], Decimal('34.00'), Decimal('85.00'), 25),
        ('P018', 'Livro: O Poder do Hábito', 'Desenvolvimento pessoal', grupos['Livros'], Decimal('16.80'), Decimal('42.00'), 60),
        ('P019', 'Livro: Sapiens', 'História da humanidade', grupos['Livros'], Decimal('22.00'), Decimal('55.00'), 45),
        ('P020', 'Livro: Mindset', 'Psicologia do sucesso', grupos['Livros'], Decimal('15.20'), Decimal('38.00'), 70),
        ('P021', 'Cafeteira Elétrica Philips', 'Cafeteira automática', grupos['Casa'], Decimal('112.00'), Decimal('280.00'), 20),
        ('P022', 'Aspirador de Pó Vertical', 'Aspirador sem fio', grupos['Casa'], Decimal('168.00'), Decimal('420.00'), 12),
        ('P023', 'Panela de Pressão Elétrica', 'Panela elétrica 6L', grupos['Casa'], Decimal('128.00'), Decimal('320.00'), 18),
        ('P024', 'Conjunto de Panelas Tramontina', 'Kit 5 peças alumínio', grupos['Casa'], Decimal('180.00'), Decimal('450.00'), 15),
        ('P025', 'Liquidificador Philips Walita', 'Liquidificador 1200W', grupos['Casa'], Decimal('72.00'), Decimal('180.00'), 30),
    ]
    
    for codigo, nome, descricao, grupo, preco_custo, preco_venda, estoque in produtos:
        if not Produto.objects.filter(codigo=codigo).exists():
            Produto.objects.create(
                codigo=codigo,
                nome=nome,
                descricao=descricao,
                grupo=grupo,
                preco_custo=preco_custo,
                preco_venda=preco_venda,
                estoque=estoque,
                estoque_minimo=5,
                ativo=True
            )
            print(f"✓ Produto criado: {codigo} - {nome}")

def criar_pedidos():
    """Criar pedidos de exemplo"""
    
    clientes = User.objects.filter(tipo_usuario='cliente')
    vendedores = User.objects.filter(tipo_usuario='vendedor')
    produtos = list(Produto.objects.all())
    
    if not clientes.exists() or not vendedores.exists() or not produtos:
        print("⚠️  Necessário ter clientes, vendedores e produtos para criar pedidos")
        return
    
    vendedor = vendedores.first()
    status_options = ['pendente', 'avaliacao_estoque', 'avaliacao_vendas', 'aprovado', 'entregue']
    
    # Criar pedidos dos últimos 30 dias
    for i in range(25):
        cliente = random.choice(clientes)
        status = random.choice(status_options)
        
        pedido = Pedido.objects.create(
            codigo=f'PED{str(i+1).zfill(4)}',
            usuario=cliente,
            vendedor=vendedor,
            status=status,
            observacoes=f'Pedido de exemplo {i+1}'
        )
        
        # Adicionar itens ao pedido
        num_itens = random.randint(1, 5)
        produtos_pedido = random.sample(produtos, num_itens)
        
        total_pedido = Decimal('0.00')
        
        for produto in produtos_pedido:
            quantidade = random.randint(1, 3)
            preco_unitario = produto.preco_venda
            subtotal = preco_unitario * quantidade
            total_pedido += subtotal
            
            ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                subtotal=subtotal
            )
        
        # Atualizar total do pedido
        pedido.valor_total = total_pedido
        pedido.save()
        
        print(f"✓ Pedido criado: {pedido.codigo} - Cliente: {cliente.username}")
    
    print(f"✓ {25} pedidos criados com sucesso!")

def main():
    """Função principal para popular o banco de dados"""
    print("🚀 Iniciando população do banco de dados...\n")
    
    try:
        print("1. Criando usuários...")
        criar_usuarios()
        
        print("\n2. Criando produtos...")
        criar_produtos()
        
        print("\n3. Criando pedidos...")
        criar_pedidos()
        
        print("\n✅ Banco de dados populado com sucesso!")
        print("\n📋 Usuários criados:")
        print("   - admin / admin123 (Administrador)")
        print("   - gerente / gerente123 (Gerente)")
        print("   - vendedor / vendedor123 (Vendedor)")
        print("   - cliente1 / cliente123 (Cliente)")
        print("   - cliente2 / cliente123 (Cliente)")
        print("   - cliente3 / cliente123 (Cliente)")
        print("   - cliente4 / cliente123 (Cliente)")
        print("   - cliente5 / cliente123 (Cliente)")
        
    except Exception as e:
        print(f"❌ Erro ao popular banco de dados: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
