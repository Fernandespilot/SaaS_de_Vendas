# SisVenda - Sistema de Vendas Django

Sistema completo de gestão de vendas desenvolvido em Django, baseado nas especificações do projeto APS (Análise e Projeto de Sistemas).

## 🚀 Funcionalidades

### 👥 Tipos de Usuário
- **Promotor de Vendas**: Visualiza clientes, registra pedidos, acompanha comissões
- **Cliente**: Acompanha pedidos, recebe notificações 
- **Gerente de Estoque**: Avalia pedidos, programa entregas, controla estoque
- **Gerente de Vendas**: Aprova pedidos, gera relatórios
- **Gerenciador**: Cadastra promotores, produtos e administra sistema

### 🛠️ Principais Recursos
- ✅ Sistema de autenticação com diferentes tipos de usuário
- ✅ Dashboard personalizado para cada tipo de usuário  
- ✅ Cadastro de clientes, produtos e pedidos
- ✅ Fluxo completo de pedidos (criação → avaliação → entrega)
- ✅ Controle de estoque automático
- ✅ Cálculo de comissões para promotores
- ✅ Interface admin completa
- ✅ Notificações por email (configurável)
- ✅ Relatórios e filtros
- ✅ Design responsivo com Bootstrap 5

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd sisvenda
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Configure o banco de dados:**
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

8. **Acesse o sistema:**
- Sistema: http://localhost:8000
- Admin: http://localhost:8000/admin

## 📁 Estrutura do Projeto

```
sisvenda_project/
├── manage.py
├── requirements.txt
├── sisvenda/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Lógica de negócios
│   ├── forms.py           # Formulários
│   ├── urls.py            # URLs da aplicação
│   ├── admin.py           # Configuração do admin
│   └── utils.py           # Funções utilitárias
└── templates/
    ├── base.html          # Template base
    ├── core/              # Templates da aplicação
    └── registration/      # Templates de autenticação
```

## 📊 Modelos de Dados

### Principais Entidades
- **User**: Usuário customizado com tipos (promotor, cliente, gerente, etc.)
- **Municipio**: Municípios para cobertura geográfica
- **PromotorVenda**: Promotores com áreas de cobertura
- **Cliente**: Clientes com informações financeiras
- **Produto**: Produtos com preços e estoque
- **Pedido**: Pedidos com status e histórico
- **ItemPedido**: Itens dos pedidos

## 🔑 Usuários Padrão

Após executar as migrações, você pode criar usuários de teste:

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()

# Criar usuário promotor
promotor = User.objects.create_user(
    username='promotor1',
    password='123456',
    first_name='João',
    last_name='Silva',
    email='promotor@exemplo.com',
    tipo_usuario='promotor'
)

# Criar usuário cliente
cliente = User.objects.create_user(
    username='cliente1',
    password='123456',
    first_name='Maria',
    last_name='Santos',
    email='cliente@exemplo.com',
    tipo_usuario='cliente'
)
```

## 🎯 Funcionalidades por Tipo de Usuário

### Promotor de Vendas
- Visualizar clientes da área de cobertura
- Registrar novos pedidos
- Acompanhar comissões
- Cadastrar novos clientes

### Cliente
- Acompanhar status dos pedidos
- Receber notificações por email
- Visualizar histórico de compras

### Gerente de Estoque
- Avaliar pedidos (verificar estoque)
- Programar entregas
- Processar entregas
- Controlar estoque

### Gerente de Vendas
- Aprovar/reprovar pedidos
- Gerar relatórios de vendas
- Acompanhar performance

### Gerenciador
- Cadastrar promotores e produtos
- Acesso ao admin Django
- Gerenciar sistema completo

## 🔧 Configurações

### Email (Desenvolvimento)
O sistema está configurado para exibir emails no console durante o desenvolvimento. Para produção, configure SMTP em `settings.py`.

### Banco de Dados
Por padrão usa SQLite. Para produção, configure PostgreSQL ou MySQL em `settings.py`.

### Arquivos Estáticos
Configure `STATIC_ROOT` e `MEDIA_ROOT` para produção.

## 🚀 Deploy

Para deploy em produção:

1. Configure `DEBUG = False` em settings.py
2. Configure banco de dados de produção
3. Configure servidor de email
4. Configure arquivos estáticos
5. Use servidor WSGI (Gunicorn + Nginx)

## 📝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Equipe

- **Análise e Projeto**: Carlos, Luiz, Pedro, Filomena
- **Gestão**: Eduardo, George, Namem  
- **Implementação**: Caroline, Mateus, Maria, Breendhon
- **Testes**: Ana Beatriz, Matheus, Pedro, Leandro

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Contate a equipe de desenvolvimento
- Consulte a documentação do Django

---

**SisVenda** - Sistema de Vendas Completo em Django 🛒
