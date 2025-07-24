# SisVenda - Sistema de Vendas

Sistema de vendas desenvolvido em Django com arquitetura modular profissional.

## Estrutura do Projeto

```
sisvenda_project/
├── apps/                    # Aplicações Django
│   ├── dashboard/           # Dashboard e página inicial
│   ├── usuarios/            # Gerenciamento de usuários
│   ├── produtos/            # Gerenciamento de produtos
│   ├── pedidos/             # Gerenciamento de pedidos
│   └── relatorios/          # Relatórios e exportações
├── config/                  # Configurações do projeto
│   ├── settings.py          # Configurações base
│   ├── settings_dev.py      # Configurações de desenvolvimento
│   ├── settings_prod.py     # Configurações de produção
│   ├── urls.py              # URLs principais
│   ├── wsgi.py              # WSGI para produção
│   └── asgi.py              # ASGI para suporte assíncrono
├── utils/                   # Utilitários
│   ├── helpers.py           # Funções auxiliares
│   └── constants.py         # Constantes do sistema
├── services/                # Serviços de negócio
│   └── email_service.py     # Serviço de email
├── templates/               # Templates HTML
├── static/                  # Arquivos estáticos
├── media/                   # Arquivos de mídia
├── logs/                    # Logs do sistema
├── requirements.txt         # Dependências
├── manage.py               # Script de gerenciamento
└── README.md               # Este arquivo
```

## Funcionalidades

### 👥 Gerenciamento de Usuários
- Autenticação e autorização
- Perfis de usuário (Cliente, Vendedor, Gerente)
- Registro e login
- Recuperação de senha

### 📦 Gerenciamento de Produtos
- Cadastro de produtos
- Controle de estoque
- Categorização
- Imagens de produtos

### 🛒 Gerenciamento de Pedidos
- Criação de pedidos
- Acompanhamento de status
- Histórico de pedidos
- Cálculo de totais

### 📊 Dashboard e Relatórios
- Dashboard diferenciado por perfil
- Relatórios de vendas
- Exportação para PDF/Excel
- Gráficos e estatísticas

## Configuração do Ambiente

### Pré-requisitos
- Python 3.8+
- Django 4.2.7
- PostgreSQL (produção)
- Redis (cache)

### Instalação

1. **Clone o repositório:**
```bash
git clone [url-do-repositorio]
cd sisvenda_project
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute as migrações:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário:**
```bash
python manage.py createsuperuser
```

7. **Execute o servidor:**
```bash
python manage.py runserver
```

## Comandos Úteis

### Desenvolvimento
```bash
# Executar servidor de desenvolvimento
python manage.py runserver

# Executar migrações
python manage.py makemigrations
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic

# Criar superusuário
python manage.py createsuperuser

# Shell interativo
python manage.py shell
```

### Produção
```bash
# Usar configurações de produção
export DJANGO_SETTINGS_MODULE=config.settings_prod

# Executar com Gunicorn
gunicorn config.wsgi:application
```

## Estrutura de Aplicações

### Apps/Dashboard
- Página inicial
- Dashboards diferenciados
- Handlers de erro

### Apps/Usuários
- Modelo de usuário customizado
- Autenticação
- Perfis e permissões

### Apps/Produtos
- Modelo de produto
- Controle de estoque
- Categorias

### Apps/Pedidos
- Modelo de pedido
- Itens de pedido
- Status de pedido

### Apps/Relatórios
- Relatórios de vendas
- Exportação de dados
- Gráficos

## Configurações

### Desenvolvimento
- Debug habilitado
- SQLite como banco de dados
- Email via console
- Debug toolbar (opcional)

### Produção
- Debug desabilitado
- PostgreSQL como banco de dados
- Email via SMTP
- Cache Redis
- Configurações de segurança

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.

## Contato

Para dúvidas ou sugestões, entre em contato através do email: [seu-email@exemplo.com]
