# Guia de Instalação e Configuração - SisVenda

Este documento fornece instruções detalhadas para instalação, configuração e execução do sistema SisVenda.

## Pré-requisitos

* Python 3.8 ou superior
* pip (gerenciador de pacotes Python)
* PostgreSQL 12 ou superior (recomendado, mas SQLite pode ser usado para desenvolvimento)
* Git

## Passos para Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/APS25-1/sisvenda.git
cd sisvenda
```

### 2. Criar e Ativar o Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

Por padrão, o sistema está configurado para usar SQLite em desenvolvimento. Para usar PostgreSQL, edite o arquivo `sisvenda_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sisvenda',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Aplicar Migrações

```bash
python manage.py migrate
```

### 6. Criar Superusuário

```bash
python manage.py createsuperuser
```

### 7. Carregar Dados Iniciais (Opcional)

```bash
python manage.py loaddata initial_data.json
```

### 8. Executar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

O sistema estará disponível em: http://localhost:8000/

## Configurações Adicionais

### Configuração de Email

Edite o arquivo `sisvenda_project/settings.py` para configurar o envio de emails:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seu_provedor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@exemplo.com'
EMAIL_HOST_PASSWORD = 'sua_senha'
DEFAULT_FROM_EMAIL = 'SisVenda <seu_email@exemplo.com>'
```

### Configuração de Armazenamento de Arquivos

Para armazenar arquivos em produção, é recomendável usar Amazon S3 ou similar. Configure no arquivo `sisvenda_project/settings.py`:

```python
# Configuração para Amazon S3
AWS_ACCESS_KEY_ID = 'sua_chave'
AWS_SECRET_ACCESS_KEY = 'seu_segredo'
AWS_STORAGE_BUCKET_NAME = 'seu_bucket'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

## Implantação em Produção

### Usando Gunicorn e Nginx

1. Instale o Gunicorn:
```bash
pip install gunicorn
```

2. Execute o Gunicorn:
```bash
gunicorn sisvenda_project.wsgi:application --bind 0.0.0.0:8000
```

3. Configure o Nginx como proxy reverso (exemplo de configuração):
```nginx
server {
    listen 80;
    server_name seudominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /caminho/para/sisvenda;
    }

    location /media/ {
        root /caminho/para/sisvenda;
    }

    location / {
        include proxy_params;
        proxy_pass http://localhost:8000;
    }
}
```

### Usando Docker

Um arquivo `Dockerfile` e `docker-compose.yml` estão incluídos no repositório para facilitar a implantação usando Docker.

```bash
docker-compose up -d
```

## Solução de Problemas

### Erro de conexão com o banco de dados

Verifique se o serviço PostgreSQL está em execução e se as credenciais estão corretas no arquivo de configuração.

### Erro de permissão ao fazer upload de arquivos

Verifique as permissões do diretório `media/` e certifique-se de que o usuário que executa o servidor web tem permissões de escrita.

### Erros de migração

Se encontrar erros durante a migração, tente:
```bash
python manage.py makemigrations
python manage.py migrate --fake-initial
python manage.py migrate
```

## Suporte

Para obter suporte ou reportar problemas, abra uma issue no repositório do GitHub: https://github.com/APS25-1/sisvenda/issues
