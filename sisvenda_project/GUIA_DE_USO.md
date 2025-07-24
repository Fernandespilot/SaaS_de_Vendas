# 🚀 Guia de Uso do SisVenda

## 📋 Resumo do Sistema

O SisVenda é um sistema completo de gestão de vendas desenvolvido em Django, implementando todas as funcionalidades especificadas nas user stories do projeto APS.

## 🛠️ Instalação Rápida

### Windows
```bash
cd sisvenda_project
setup.bat
```

### Linux/Mac
```bash
cd sisvenda_project
chmod +x setup.sh
./setup.sh
```

### Instalação Manual
```bash
cd sisvenda_project
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py popular_banco
python manage.py runserver
```

## 👥 Usuários de Demonstração

Após executar `python manage.py popular_banco`, você terá:

| Usuário | Senha | Tipo | Funcionalidades |
|---------|-------|------|-----------------|
| admin | admin123 | Administrador | Acesso completo ao sistema |
| promotor1 | 123456 | Promotor | Gerenciar clientes e pedidos |
| cliente1 | 123456 | Cliente | Acompanhar pedidos |
| estoque1 | 123456 | Gerente Estoque | Controlar estoque e entregas |
| vendas1 | 123456 | Gerente Vendas | Aprovar pedidos e relatórios |

## 📱 Principais Funcionalidades

### 1. Sistema de Autenticação
- ✅ Login/logout
- ✅ Registro de novos usuários
- ✅ Diferentes tipos de usuário
- ✅ Controle de acesso por funcionalidade

### 2. Dashboard Personalizado
- ✅ Interface específica para cada tipo de usuário
- ✅ Métricas e estatísticas relevantes
- ✅ Ações rápidas contextuais

### 3. Gestão de Clientes (Promotores)
- ✅ Listar clientes da área de cobertura
- ✅ Filtros por nome, endereço, município
- ✅ Cadastrar novos clientes
- ✅ Visualizar informações detalhadas

### 4. Catálogo de Produtos
- ✅ Produtos organizados por grupos
- ✅ Preços com margem de lucro e impostos
- ✅ Sistema de promoções
- ✅ Controle de estoque
- ✅ Busca e filtros

### 5. Gestão de Pedidos
- ✅ Fluxo completo: Criação → Avaliação → Entrega
- ✅ Status tracking automático
- ✅ Histórico de mudanças
- ✅ Cálculo automático de valores

### 6. Controle de Estoque
- ✅ Atualização automática com pedidos
- ✅ Verificação de disponibilidade
- ✅ Alertas de estoque baixo

### 7. Sistema de Comissões
- ✅ Cálculo automático para promotores
- ✅ Percentual configurável
- ✅ Relatórios de comissões

### 8. Notificações
- ✅ Email para mudanças de status
- ✅ Notificações para clientes e promotores
- ✅ Templates personalizados

### 9. Interface Admin
- ✅ Django Admin customizado
- ✅ Gestão completa de dados
- ✅ Filtros e busca avançada

### 10. Design Responsivo
- ✅ Bootstrap 5
- ✅ Interface moderna e intuitiva
- ✅ Compatível com dispositivos móveis

## 🔄 Fluxo de Pedidos

### 1. Criação (Promotor)
- Promotor acessa lista de clientes
- Seleciona cliente e produtos
- Cria pedido com status "pendente"

### 2. Avaliação de Estoque
- Gerente de estoque verifica disponibilidade
- Aprova ou reprova baseado no estoque
- Status: "aprovado_estoque" ou "reprovado_estoque"

### 3. Avaliação Financeira
- Gerente de vendas analisa cliente
- Verifica limite de crédito e histórico
- Status: "aprovado_vendas" ou "reprovado_vendas"

### 4. Programação de Entrega
- Gerente de estoque programa data de entrega
- Estoque é reservado/baixado
- Status: "programado"

### 5. Processamento
- No dia da entrega, pedido é processado
- Status: "processado" → "concluido"

### 6. Comissão
- Comissão calculada automaticamente
- Baseada no percentual do promotor

## 🎯 Casos de Uso Implementados

### Promotor de Vendas
- [x] Visualizar clientes da área (US1)
- [x] Registrar pedidos (US2)
- [x] Acompanhar comissões

### Cliente
- [x] Acompanhar pedidos (US3)
- [x] Receber notificações por email
- [x] Visualizar histórico

### Gerenciador
- [x] Cadastrar promotores (US4)
- [x] Cadastrar produtos (US5)
- [x] Gerenciar sistema

### Gerente de Estoque
- [x] Avaliar pedidos (US6)
- [x] Programar entregas (US7)
- [x] Processar entregas (US8)
- [x] Relatórios de produtos (US9)

### Gerente de Vendas
- [x] Aprovar pedidos financeiramente
- [x] Acompanhar vendas
- [x] Gerar relatórios

## 🧪 Testes

Execute os testes automatizados:
```bash
python manage.py test
```

## 🚀 Próximos Passos

### Melhorias Futuras
- [ ] Relatórios avançados com gráficos
- [ ] API REST para integração mobile
- [ ] Sistema de chat interno
- [ ] Integração com pagamentos
- [ ] Geolocalização para promotores
- [ ] App mobile React Native

### Deploy em Produção
- [ ] Configurar PostgreSQL
- [ ] Configurar Redis para cache
- [ ] Configurar Celery para tarefas
- [ ] Configurar servidor de email
- [ ] Configurar HTTPS
- [ ] Configurar monitoramento

## 📊 Estrutura Técnica

### Tecnologias Utilizadas
- **Backend**: Django 4.2, Python 3.8+
- **Frontend**: Bootstrap 5, JavaScript
- **Banco**: SQLite (dev), PostgreSQL (prod)
- **Autenticação**: Django Auth customizado
- **Email**: Django Email Framework
- **Testes**: Django TestCase

### Arquitetura
- **Model**: Modelos de dados (core/models.py)
- **View**: Lógica de negócio (core/views.py)
- **Template**: Interface usuário (templates/)
- **Forms**: Validação de dados (core/forms.py)
- **Utils**: Funções auxiliares (core/utils.py)

### Padrões Implementados
- MVT (Model-View-Template)
- DRY (Don't Repeat Yourself)
- SOLID principles
- Django Best Practices
- Responsive Design

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Execute os testes
5. Faça um Pull Request

## 📞 Suporte

- **Email**: suporte@sisvenda.com
- **Documentação**: `/docs/`
- **Issues**: GitHub Issues
- **Wiki**: GitHub Wiki

---

**SisVenda v1.0** - Sistema completo de gestão de vendas implementado com Django 🛒
