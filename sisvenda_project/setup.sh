#!/bin/bash

# Script para setup inicial do projeto SisVenda

echo "🚀 Iniciando setup do SisVenda..."

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python -m venv venv

# Ativar ambiente virtual (Linux/Mac)
echo "⚡ Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📋 Instalando dependências..."
pip install -r requirements.txt

# Fazer migrações
echo "🗄️ Configurando banco de dados..."
python manage.py makemigrations
python manage.py migrate

# Criar superusuário
echo "👤 Criando superusuário..."
echo "Digite as informações do administrador:"
python manage.py createsuperuser

# Executar servidor
echo "🎉 Setup concluído! Executando servidor..."
python manage.py runserver
