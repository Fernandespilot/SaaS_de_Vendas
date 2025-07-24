#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_dev')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create admin user
try:
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_user(
            username='admin',
            email='admin@sisvenda.com',
            password='admin',
            first_name='Admin',
            last_name='Sistema'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Usuário admin criado com sucesso!")
        print("Username: admin")
        print("Password: admin")
    else:
        print("Usuário admin já existe!")
except Exception as e:
    print(f"Erro ao criar usuário: {e}")
