from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decimal import Decimal
from core.models import (
    Municipio, GrupoProduto, Produto, PromotorVenda, Cliente
)

User = get_user_model()


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais para demonstração'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando população do banco de dados...'))
        
        # Criar municípios
        self.criar_municipios()
        
        # Criar grupos de produtos
        self.criar_grupos_produtos()
        
        # Criar produtos
        self.criar_produtos()
        
        # Criar usuários e perfis
        self.criar_usuarios()
        
        self.stdout.write(self.style.SUCCESS('✅ Banco de dados populado com sucesso!'))
        self.stdout.write(self.style.WARNING('🔑 Usuários criados:'))
        self.stdout.write('   - admin / admin123 (Administrador)')
        self.stdout.write('   - promotor1 / 123456 (Promotor)')
        self.stdout.write('   - cliente1 / 123456 (Cliente)')
        self.stdout.write('   - estoque1 / 123456 (Gerente Estoque)')
        self.stdout.write('   - vendas1 / 123456 (Gerente Vendas)')

    def criar_municipios(self):
        """Cria municípios de exemplo"""
        municipios = [
            {'nome': 'São Paulo', 'estado': 'SP', 'codigo_ibge': '3550308'},
            {'nome': 'Rio de Janeiro', 'estado': 'RJ', 'codigo_ibge': '3304557'},
            {'nome': 'Belo Horizonte', 'estado': 'MG', 'codigo_ibge': '3106200'},
            {'nome': 'Salvador', 'estado': 'BA', 'codigo_ibge': '2927408'},
            {'nome': 'Brasília', 'estado': 'DF', 'codigo_ibge': '5300108'},
            {'nome': 'Fortaleza', 'estado': 'CE', 'codigo_ibge': '2304400'},
            {'nome': 'Recife', 'estado': 'PE', 'codigo_ibge': '2611606'},
            {'nome': 'Porto Alegre', 'estado': 'RS', 'codigo_ibge': '4314902'},
            {'nome': 'Curitiba', 'estado': 'PR', 'codigo_ibge': '4106902'},
            {'nome': 'Goiânia', 'estado': 'GO', 'codigo_ibge': '5208707'},
        ]
        
        for municipio_data in municipios:
            municipio, created = Municipio.objects.get_or_create(
                codigo_ibge=municipio_data['codigo_ibge'],
                defaults=municipio_data
            )
            if created:
                self.stdout.write(f'  📍 Município criado: {municipio.nome} - {municipio.estado}')

    def criar_grupos_produtos(self):
        """Cria grupos de produtos"""
        grupos = [
            {'nome': 'Eletrônicos', 'descricao': 'Produtos eletrônicos em geral'},
            {'nome': 'Informática', 'descricao': 'Computadores, notebooks, acessórios'},
            {'nome': 'Celulares', 'descricao': 'Smartphones e acessórios'},
            {'nome': 'Áudio e Vídeo', 'descricao': 'Fones, caixas de som, TVs'},
            {'nome': 'Games', 'descricao': 'Consoles e jogos'},
            {'nome': 'Casa Inteligente', 'descricao': 'Automação residencial'},
        ]
        
        for grupo_data in grupos:
            grupo, created = GrupoProduto.objects.get_or_create(
                nome=grupo_data['nome'],
                defaults=grupo_data
            )
            if created:
                self.stdout.write(f'  📦 Grupo criado: {grupo.nome}')

    def criar_produtos(self):
        """Cria produtos de exemplo"""
        produtos = [
            # Eletrônicos
            {'codigo': 'ELE001', 'nome': 'Smartphone Samsung Galaxy S24', 'grupo': 'Celulares', 'custo': 1200, 'margem': 25, 'estoque': 50},
            {'codigo': 'ELE002', 'nome': 'iPhone 15 Pro', 'grupo': 'Celulares', 'custo': 2500, 'margem': 20, 'estoque': 30},
            {'codigo': 'ELE003', 'nome': 'Fone Bluetooth JBL', 'grupo': 'Áudio e Vídeo', 'custo': 150, 'margem': 40, 'estoque': 100},
            
            # Informática
            {'codigo': 'INF001', 'nome': 'Notebook Dell Inspiron 15', 'grupo': 'Informática', 'custo': 2000, 'margem': 30, 'estoque': 25},
            {'codigo': 'INF002', 'nome': 'Mouse Logitech MX Master 3', 'grupo': 'Informática', 'custo': 80, 'margem': 50, 'estoque': 75},
            {'codigo': 'INF003', 'nome': 'Teclado Mecânico Razer', 'grupo': 'Informática', 'custo': 200, 'margem': 35, 'estoque': 40},
            
            # Áudio e Vídeo
            {'codigo': 'AUD001', 'nome': 'Caixa de Som Bluetooth Sony', 'grupo': 'Áudio e Vídeo', 'custo': 300, 'margem': 30, 'estoque': 60},
            {'codigo': 'AUD002', 'nome': 'Smart TV 55" LG', 'grupo': 'Áudio e Vídeo', 'custo': 1500, 'margem': 25, 'estoque': 20},
            {'codigo': 'AUD003', 'nome': 'Soundbar Samsung', 'grupo': 'Áudio e Vídeo', 'custo': 400, 'margem': 35, 'estoque': 35},
            
            # Games
            {'codigo': 'GAM001', 'nome': 'PlayStation 5', 'grupo': 'Games', 'custo': 2000, 'margem': 15, 'estoque': 15},
            {'codigo': 'GAM002', 'nome': 'Xbox Series X', 'grupo': 'Games', 'custo': 1800, 'margem': 18, 'estoque': 20},
            {'codigo': 'GAM003', 'nome': 'Nintendo Switch', 'grupo': 'Games', 'custo': 1200, 'margem': 25, 'estoque': 30},
            
            # Casa Inteligente
            {'codigo': 'CAS001', 'nome': 'Alexa Echo Dot', 'grupo': 'Casa Inteligente', 'custo': 120, 'margem': 45, 'estoque': 80},
            {'codigo': 'CAS002', 'nome': 'Lâmpada Inteligente Philips', 'grupo': 'Casa Inteligente', 'custo': 50, 'margem': 60, 'estoque': 120},
            {'codigo': 'CAS003', 'nome': 'Câmera de Segurança Wi-Fi', 'grupo': 'Casa Inteligente', 'custo': 200, 'margem': 40, 'estoque': 45},
        ]
        
        for produto_data in produtos:
            grupo = GrupoProduto.objects.get(nome=produto_data['grupo'])
            produto, created = Produto.objects.get_or_create(
                codigo=produto_data['codigo'],
                defaults={
                    'nome': produto_data['nome'],
                    'grupo': grupo,
                    'custo': Decimal(str(produto_data['custo'])),
                    'margem_lucro': Decimal(str(produto_data['margem'])),
                    'estoque': produto_data['estoque'],
                    'impostos': Decimal('10.00'),
                    'ativo': True
                }
            )
            if created:
                self.stdout.write(f'  📱 Produto criado: {produto.codigo} - {produto.nome}')

    def criar_usuarios(self):
        """Cria usuários de exemplo"""
        # Administrador
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                password='admin123',
                email='admin@sisvenda.com',
                first_name='Administrador',
                last_name='Sistema',
                tipo_usuario='gerenciador'
            )
            self.stdout.write(f'  👤 Admin criado: {admin.username}')

        # Promotor
        if not User.objects.filter(username='promotor1').exists():
            promotor_user = User.objects.create_user(
                username='promotor1',
                password='123456',
                email='promotor1@sisvenda.com',
                first_name='João',
                last_name='Silva',
                tipo_usuario='promotor',
                telefone='(11) 99999-1111',
                cpf='123.456.789-01'
            )
            
            # Criar perfil do promotor
            municipios = Municipio.objects.filter(estado__in=['SP', 'RJ'])[:3]
            promotor = PromotorVenda.objects.create(
                user=promotor_user,
                comissao_percentual=Decimal('5.00')
            )
            promotor.municipios_cobertura.set(municipios)
            self.stdout.write(f'  👨‍💼 Promotor criado: {promotor_user.username}')

        # Cliente
        if not User.objects.filter(username='cliente1').exists():
            cliente_user = User.objects.create_user(
                username='cliente1',
                password='123456',
                email='cliente1@sisvenda.com',
                first_name='Maria',
                last_name='Santos',
                tipo_usuario='cliente',
                telefone='(11) 99999-2222',
                cpf='987.654.321-00'
            )
            
            # Criar perfil do cliente
            municipio = Municipio.objects.filter(nome='São Paulo').first()
            promotor = PromotorVenda.objects.first()
            
            cliente = Cliente.objects.create(
                user=cliente_user,
                municipio=municipio,
                endereco='Rua das Flores, 123 - Centro',
                promotor=promotor,
                limite_credito=Decimal('5000.00'),
                status_financeiro='aprovado'
            )
            self.stdout.write(f'  👤 Cliente criado: {cliente_user.username}')

        # Gerente de Estoque
        if not User.objects.filter(username='estoque1').exists():
            estoque_user = User.objects.create_user(
                username='estoque1',
                password='123456',
                email='estoque1@sisvenda.com',
                first_name='Carlos',
                last_name='Oliveira',
                tipo_usuario='gerente_estoque',
                telefone='(11) 99999-3333'
            )
            self.stdout.write(f'  📦 Gerente Estoque criado: {estoque_user.username}')

        # Gerente de Vendas
        if not User.objects.filter(username='vendas1').exists():
            vendas_user = User.objects.create_user(
                username='vendas1',
                password='123456',
                email='vendas1@sisvenda.com',
                first_name='Ana',
                last_name='Costa',
                tipo_usuario='gerente_vendas',
                telefone='(11) 99999-4444'
            )
            self.stdout.write(f'  📊 Gerente Vendas criado: {vendas_user.username}')
