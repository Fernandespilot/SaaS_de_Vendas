from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal
from core.models import (
    Municipio, GrupoProduto, Produto, PromotorVenda, Cliente, Pedido, ItemPedido
)

User = get_user_model()


class ModelTestCase(TestCase):
    """Testes para os modelos"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.municipio = Municipio.objects.create(
            nome='São Paulo',
            estado='SP',
            codigo_ibge='3550308'
        )
        
        self.grupo = GrupoProduto.objects.create(
            nome='Eletrônicos',
            descricao='Produtos eletrônicos'
        )
        
        self.produto = Produto.objects.create(
            codigo='ELE001',
            nome='Smartphone',
            grupo=self.grupo,
            custo=Decimal('1000.00'),
            margem_lucro=Decimal('25.00'),
            estoque=100,
            impostos=Decimal('10.00')
        )
        
        self.user_promotor = User.objects.create_user(
            username='promotor_test',
            password='123456',
            first_name='João',
            last_name='Silva',
            email='promotor@test.com',
            tipo_usuario='promotor'
        )
        
        self.promotor = PromotorVenda.objects.create(
            user=self.user_promotor,
            comissao_percentual=Decimal('5.00')
        )
        self.promotor.municipios_cobertura.add(self.municipio)
        
        self.user_cliente = User.objects.create_user(
            username='cliente_test',
            password='123456',
            first_name='Maria',
            last_name='Santos',
            email='cliente@test.com',
            tipo_usuario='cliente'
        )
        
        self.cliente = Cliente.objects.create(
            user=self.user_cliente,
            municipio=self.municipio,
            endereco='Rua das Flores, 123',
            promotor=self.promotor,
            limite_credito=Decimal('5000.00'),
            status_financeiro='aprovado'
        )
    
    def test_produto_preco_venda(self):
        """Testa cálculo do preço de venda"""
        # Custo: R$ 1000,00
        # Margem: 25%
        # Impostos: 10%
        # Preço base: 1000 * 1.25 = 1250
        # Preço com impostos: 1250 * 1.10 = 1375
        expected_price = Decimal('1375.00')
        self.assertEqual(self.produto.preco_venda, expected_price)
    
    def test_produto_preco_promocional(self):
        """Testa cálculo do preço promocional"""
        self.produto.percentual_promocao = Decimal('10.00')
        self.produto.save()
        
        # Preço normal: 1375
        # Desconto: 10%
        # Preço promocional: 1375 * 0.90 = 1237.50
        expected_price = Decimal('1237.50')
        self.assertEqual(self.produto.preco_promocional, expected_price)
    
    def test_pedido_creation(self):
        """Testa criação de pedido"""
        pedido = Pedido.objects.create(
            codigo='PED-001',
            cliente=self.cliente,
            promotor=self.promotor,
            status='pendente'
        )
        
        item = ItemPedido.objects.create(
            pedido=pedido,
            produto=self.produto,
            quantidade=2,
            preco_unitario=self.produto.preco_final
        )
        
        self.assertEqual(pedido.valor_total, item.subtotal)
        self.assertEqual(pedido.comissao_total, pedido.valor_total * (Decimal('5.00') / 100))
    
    def test_municipio_str(self):
        """Testa representação string do município"""
        self.assertEqual(str(self.municipio), 'São Paulo - SP')
    
    def test_produto_str(self):
        """Testa representação string do produto"""
        self.assertEqual(str(self.produto), 'ELE001 - Smartphone')


class ViewTestCase(TestCase):
    """Testes para as views"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.user = User.objects.create_user(
            username='testuser',
            password='123456',
            first_name='Test',
            last_name='User',
            email='test@test.com',
            tipo_usuario='promotor'
        )
    
    def test_home_view(self):
        """Testa a página inicial"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SisVenda')
    
    def test_login_required_dashboard(self):
        """Testa que o dashboard requer login"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect para login
    
    def test_dashboard_after_login(self):
        """Testa acesso ao dashboard após login"""
        self.client.login(username='testuser', password='123456')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard')
    
    def test_register_view(self):
        """Testa a página de registro"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Criar Conta')
    
    def test_login_view(self):
        """Testa a página de login"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')


class UserTestCase(TestCase):
    """Testes para o modelo de usuário customizado"""
    
    def test_create_user(self):
        """Testa criação de usuário"""
        user = User.objects.create_user(
            username='testuser',
            password='123456',
            first_name='Test',
            last_name='User',
            email='test@test.com',
            tipo_usuario='cliente'
        )
        
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.tipo_usuario, 'cliente')
        self.assertTrue(user.check_password('123456'))
    
    def test_create_superuser(self):
        """Testa criação de superusuário"""
        user = User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@test.com'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.tipo_usuario, 'cliente')  # Valor padrão
