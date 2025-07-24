# SisVenda - Sistema de Gestão de Vendas

<p align="center">
  <img src="documents/img/logo-sisvenda.png" alt="SisVenda Logo" width="300"/>
</p>

Sistema completo de Gestão de Vendas desenvolvido para facilitar a venda de produtos, gerenciar promotores e gerar relatórios. Este repositório contém toda a documentação e o desenvolvimento do sistema proposto na disciplina **Análise e Projeto de Sistemas Computacionais**, no período 2025/1.

![Dashboard](documents/img/dashboard-screenshot.png)

---

## Índice

- [Visão Geral](#visão-geral)
- [Visão de Produto](#visão-de-produto)
- [Interfaces e Screenshots](#interfaces-e-screenshots)
- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos do Produto](#objetivos-do-produto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [User Stories](#user-stories)
- [Como executar o projeto](#como-executar-o-projeto)
- [Testes](#testes)

---

## Visão Geral

A **Empresa X** atua no setor de vendas de materiais eletroeletrônicos por meio de **catálogos impressos**, distribuídos via correio com o apoio de uma equipe de **promotores de venda**.

O sistema visa **automatizar e gerenciar** esse processo, do cadastro ao acompanhamento dos pedidos, promovendo maior eficiência operacional.

---

## Visão de Produto

O **SisVenda** é um sistema de vendas completo, desenvolvido para lojas que desejam gerenciar operações de forma digital, com foco em eficiência e controle.

Principais recursos:
- Gerenciamento de produtos, clientes e vendedores
- Registro e acompanhamento de pedidos
- Controle de estoques e comissões
- Geração de relatórios financeiros
- Interface simples e intuitiva para diferentes usuários

---

## Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina **Análise e Projeto de Sistemas Computacionais (2025/1)** com o objetivo de consolidar conceitos de modelagem de sistemas, UML, padrões de projeto e implementação web.

---

## Interfaces e Screenshots

### Dashboard Principal
![Dashboard](documents/img/dashboard-screenshot.png)

### Gestão de Produtos
![Produtos](documents/img/produtos-screenshot.png)

### Relatórios e Gráficos
![Relatórios](documents/img/relatorios-screenshot.png)

### Gestão de Pedidos
![Pedidos](documents/img/pedidos-screenshot.png)

### Interface Mobile
<p align="center">
  <img src="documents/img/mobile-screenshot.png" alt="Versão Mobile" width="300"/>
</p>

---

## Objetivos do Produto

- Automatizar o controle de entrada e saída de produtos
- Gerenciar clientes e vendedores de forma eficiente
- Facilitar a geração de relatórios financeiros e operacionais
- Oferecer interface simples e interativa para diferentes perfis de usuário

---

## Tecnologias Utilizadas

| Ferramenta           | Finalidade                                              |
|-----------------------|--------------------------------------------------------|
| Python 3.11           | Linguagem principal                                     |
| Django 4.2            | Framework web principal                                 |
| PostgreSQL            | Banco de dados principal                                |
| HTML + CSS            | Interface administrativa                                |
| Mermaid Chart         | Diagrama de Entidade Relacionamento (DER)               |
| Lucidchart            | Diagrama de casos de uso e modelos orientados a objetos |
| pip                   | Gerenciador de pacotes Python                           |
| Virtualenv            | Isolamento de ambiente                                  |
| Git/GitHub            | Controle de versão                                      |
| VSCode                | Editor de código recomendado                            |
| Docker (planejado)    | Containerização futura para implantação                 |

---

## User Stories

As histórias de usuário estão organizadas no [Quadro de Projetos do GitHub](https://github.com/orgs/APS25-1/projects/3/views/1), onde é possível acompanhar visualmente o progresso, os cards de funcionalidades e o fluxo de trabalho por status.

**Perfis de usuários contemplados:**
- Promotor de vendas
- Cliente
- Gerente de vendas
- Gerente de estoque

### Exemplos de user stories implementadas:

1. **Como gerente**, quero visualizar relatórios de vendas para acompanhar o desempenho da equipe
2. **Como promotor**, quero registrar pedidos de clientes rapidamente para otimizar meu tempo
3. **Como cliente**, quero acessar meu histórico de pedidos para verificar meus gastos
4. **Como gerente de estoque**, quero visualizar alertas de produtos com estoque baixo para programar reposições

A documentação completa das user stories está disponível em [documents/user-story.md](documents/user-story.md).

---

## Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/usuario/sisvenda.git

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Execute o servidor de desenvolvimento
python manage.py runserver

# Para gerar as imagens para o README (opcional)
cd scripts

# Instalar dependências para capturas de tela (se necessário)
install_dependencies.bat  # Windows
# OU
./install_dependencies.sh  # Linux/Mac

# Gerar screenshots (requer servidor rodando)
python capture_screenshots.py
```

## Testes

O sistema conta com testes automatizados para garantir a qualidade e funcionamento correto das funcionalidades. Os cenários de teste foram cuidadosamente elaborados para cobrir os principais casos de uso do sistema.

### Executando os testes

```bash
# Executa todos os testes
python manage.py test

# Executa testes de uma aplicação específica
python manage.py test pedidos
```

### Cobertura de testes

A documentação completa dos cenários de teste está disponível em [documents/cenarios-teste.md](documents/cenarios-teste.md).

![Testes](documents/img/testes-screenshot.png)

# Execute o projeto
python manage.py runserver
