from django.core.management.base import BaseCommand
from apps.usuarios.models import Municipio, User, PromotorVenda


class Command(BaseCommand):
    help = 'Popula o banco com dados iniciais para desenvolvimento'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando população do banco...'))
        
        # Criar municípios
        municipios_data = [
            {'nome': 'São Paulo', 'estado': 'SP'},
            {'nome': 'Rio de Janeiro', 'estado': 'RJ'},
            {'nome': 'Belo Horizonte', 'estado': 'MG'},
            {'nome': 'Salvador', 'estado': 'BA'},
            {'nome': 'Brasília', 'estado': 'DF'},
            {'nome': 'Fortaleza', 'estado': 'CE'},
            {'nome': 'Recife', 'estado': 'PE'},
            {'nome': 'Porto Alegre', 'estado': 'RS'},
            {'nome': 'Curitiba', 'estado': 'PR'},
            {'nome': 'Goiânia', 'estado': 'GO'},
        ]
        
        for municipio_data in municipios_data:
            municipio, created = Municipio.objects.get_or_create(
                nome=municipio_data['nome'],
                estado=municipio_data['estado']
            )
            if created:
                self.stdout.write(f'Município criado: {municipio}')
        
        # Criar usuários promotores se não existirem
        promotores_data = [
            {
                'username': 'promotor1',
                'email': 'promotor1@sisvenda.com',
                'first_name': 'João',
                'last_name': 'Silva',
                'municipio': 'São Paulo',
                'comissao': 5.00,
                'meta_mensal': 10000.00
            },
            {
                'username': 'promotor2', 
                'email': 'promotor2@sisvenda.com',
                'first_name': 'Maria',
                'last_name': 'Santos',
                'municipio': 'Rio de Janeiro',
                'comissao': 4.50,
                'meta_mensal': 8000.00
            },
            {
                'username': 'promotor3',
                'email': 'promotor3@sisvenda.com', 
                'first_name': 'Carlos',
                'last_name': 'Oliveira',
                'municipio': 'Belo Horizonte',
                'comissao': 6.00,
                'meta_mensal': 12000.00
            }
        ]
        
        for promotor_data in promotores_data:
            # Verificar se o usuário já existe
            if not User.objects.filter(username=promotor_data['username']).exists():
                # Criar usuário
                user = User.objects.create_user(
                    username=promotor_data['username'],
                    email=promotor_data['email'],
                    first_name=promotor_data['first_name'],
                    last_name=promotor_data['last_name'],
                    password='senha123',
                    tipo_usuario='promotor'
                )
                
                # Buscar município
                municipio = Municipio.objects.get(nome=promotor_data['municipio'])
                
                # Criar promotor
                promotor = PromotorVenda.objects.create(
                    user=user,
                    municipio=municipio,
                    comissao=promotor_data['comissao'],
                    meta_mensal=promotor_data['meta_mensal']
                )
                
                self.stdout.write(f'Promotor criado: {promotor}')
            else:
                self.stdout.write(f'Promotor {promotor_data["username"]} já existe')
        
        # Criar superusuário se não existir
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@sisvenda.com',
                password='admin123',
                first_name='Administrador',
                last_name='Sistema',
                tipo_usuario='gerenciador'
            )
            self.stdout.write(self.style.SUCCESS('Superusuário criado: admin/admin123'))
        
        self.stdout.write(self.style.SUCCESS('População do banco concluída!'))
