@echo off
REM Script para setup inicial do projeto SisVenda no Windows

echo 🚀 Iniciando setup do SisVenda...

REM Criar ambiente virtual
echo 📦 Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual (Windows)
echo ⚡ Ativando ambiente virtual...
call venv\Scripts\activate

REM Instalar dependências
echo 📋 Instalando dependências...
pip install -r requirements.txt

REM Fazer migrações
echo 🗄️ Configurando banco de dados...
python manage.py makemigrations
python manage.py migrate

REM Criar superusuário
echo 👤 Criando superusuário...
echo Digite as informações do administrador:
python manage.py createsuperuser

REM Executar servidor
echo 🎉 Setup concluído! Executando servidor...
python manage.py runserver

pause
