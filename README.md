# SisVenda - Sistema de Vendas

Sistema de Gestão de Vendas desenvolvido para facilitar a venda de produtos, gerenciar promotores e gerar relatórios. Este repositório contém toda a documentação e o desenvolvimento do sistema proposto na disciplina **Análise e Projeto de Sistemas Computacionais**, no período 2025/1.

---

## Índice

- [Visão Geral](#visão-geral)
- [Visão de Produto](#visão-de-produto)
- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos do Produto](#objetivos-do-produto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Story](#story)
- [Como executar o projeto](#como-executar-o-projeto)

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

## Story

As histórias de usuário estão organizadas no [Quadro de Projetos do GitHub](https://github.com/orgs/APS25-1/projects/3/views/1), onde é possível acompanhar visualmente o progresso, os cards de funcionalidades e o fluxo de trabalho por status.

**Perfis de usuários contemplados:**
- Promotor de vendas
- Cliente
- Gerente de vendas
- Gerente de estoque

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

# Execute o projeto
python manage.py runserver
