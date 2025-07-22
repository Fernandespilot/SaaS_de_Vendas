# 🧪 Cenários de Teste – Sistema de Gestão de Vendas

## 📋 Índice
1. [Cenários de Autenticação e Autorização](#autenticação)
2. [Cenários para Promotor de Vendas](#promotor)
3. [Cenários para Cliente](#cliente)
4. [Cenários para Gerenciador](#gerenciador)
5. [Cenários para Gerente de Estoque](#estoque)
6. [Cenários para Gerente de Vendas](#vendas)
7. [Cenários de Integração](#integração)
8. [Cenários de Performance](#performance)

---

## 🔐 Cenários de Autenticação e Autorização {#autenticação}

### CT001 - Login com credenciais válidas
**Objetivo:** Verificar se o usuário consegue fazer login com credenciais corretas  
**Pré-condições:** Usuário cadastrado no sistema  
**Passos:**
1. Acessar a página de login
2. Inserir username: "admin"
3. Inserir senha: "123456"
4. Clicar em "Entrar"

**Resultado Esperado:** Usuário redirecionado para o dashboard correspondente ao seu perfil

### CT002 - Login com credenciais inválidas
**Objetivo:** Verificar se o sistema impede login com credenciais incorretas  
**Pré-condições:** Sistema operacional  
**Passos:**
1. Acessar a página de login
2. Inserir username: "usuario_inexistente"
3. Inserir senha: "senha_errada"
4. Clicar em "Entrar"

**Resultado Esperado:** Mensagem de erro "Credenciais inválidas" e usuário permanece na tela de login

### CT003 - Acesso negado a área restrita
**Objetivo:** Verificar se usuários não autorizados são bloqueados  
**Pré-condições:** Usuário logado como cliente  
**Passos:**
1. Tentar acessar diretamente URL do dashboard administrativo
2. Verificar resposta do sistema

**Resultado Esperado:** Redirecionamento para página de erro 403 ou login

---

## 🛒 Cenários para Promotor de Vendas {#promotor}

### CT004 - Visualizar lista de clientes
**Objetivo:** Verificar se promotor visualiza apenas seus clientes  
**Pré-condições:** Promotor logado, clientes cadastrados na sua área  
**Passos:**
1. Acessar menu "Meus Clientes"
2. Verificar lista exibida
3. Testar filtros por ordem alfabética
4. Testar filtro por status de visita

**Resultado Esperado:** 
- Lista exibe apenas clientes da área do promotor
- Filtros funcionam corretamente
- Dados exibidos: nome, endereço, telefone

### CT005 - Cadastrar novo cliente
**Objetivo:** Verificar cadastro de cliente pelo promotor  
**Pré-condições:** Promotor logado  
**Passos:**
1. Acessar "Cadastrar Cliente"
2. Preencher campos obrigatórios:
   - Nome: "Cliente Teste LTDA"
   - CNPJ: "12.345.678/0001-90"
   - Telefone: "(11) 99999-9999"
   - Endereço completo
3. Clicar em "Salvar"

**Resultado Esperado:** 
- Cliente criado com sucesso
- Mensagem de confirmação exibida
- Cliente aparece na lista do promotor

### CT006 - Registrar pedido - Fluxo completo
**Objetivo:** Verificar registro completo de pedido  
**Pré-condições:** Promotor logado, cliente e produtos cadastrados  
**Passos:**
1. Acessar "Novo Pedido"
2. Selecionar cliente existente
3. Adicionar produto: "Produto A", quantidade: 5
4. Adicionar produto: "Produto B", quantidade: 3
5. Verificar cálculo do total
6. Verificar cálculo da comissão
7. Salvar pedido

**Resultado Esperado:**
- Pedido salvo com status "Pendente"
- Total calculado corretamente
- Comissão calculada corretamente
- Mensagem de sucesso exibida

### CT007 - Registrar pedido - Cliente inexistente
**Objetivo:** Verificar criação de cliente durante pedido  
**Pré-condições:** Promotor logado  
**Passos:**
1. Acessar "Novo Pedido"
2. Selecionar "Novo Cliente"
3. Preencher dados do cliente
4. Adicionar produtos ao pedido
5. Salvar

**Resultado Esperado:**
- Cliente criado automaticamente
- Pedido associado ao novo cliente
- Ambos salvos com sucesso

---

## 👤 Cenários para Cliente {#cliente}

### CT008 - Acompanhar pedido próprio
**Objetivo:** Verificar se cliente vê apenas seus pedidos  
**Pré-condições:** Cliente logado, pedidos existentes  
**Passos:**
1. Acessar "Meus Pedidos"
2. Verificar lista de pedidos
3. Clicar em um pedido específico
4. Verificar detalhes exibidos

**Resultado Esperado:**
- Cliente vê apenas seus próprios pedidos
- Detalhes completos: código, data, produtos, quantidades, valores, status
- Status atualizados corretamente

### CT009 - Visualizar catálogo de produtos
**Objetivo:** Verificar acesso ao catálogo  
**Pré-condições:** Cliente logado, produtos cadastrados  
**Passos:**
1. Acessar "Catálogo de Produtos"
2. Navegar pelos produtos
3. Testar filtros por categoria
4. Verificar informações exibidas

**Resultado Esperado:**
- Todos os produtos ativos são exibidos
- Informações: nome, descrição, preço, disponibilidade
- Filtros funcionam corretamente

---

## ⚙️ Cenários para Gerenciador {#gerenciador}

### CT010 - Cadastrar promotor com região
**Objetivo:** Verificar cadastro completo de promotor  
**Pré-condições:** Gerenciador logado, regiões cadastradas  
**Passos:**
1. Acessar "Cadastrar Promotor"
2. Preencher dados pessoais:
   - Nome: "João Silva"
   - CPF: "123.456.789-00"
   - Telefone: "(11) 98765-4321"
   - Email: "joao@email.com"
3. Selecionar região: "São Paulo - Centro"
4. Salvar

**Resultado Esperado:**
- Promotor criado com sucesso
- Região associada corretamente
- Aparece na listagem com cidades atribuídas

### CT011 - Cadastrar promotor - CPF duplicado
**Objetivo:** Verificar validação de CPF único  
**Pré-condições:** Promotor já existe com CPF específico  
**Passos:**
1. Tentar cadastrar novo promotor
2. Usar CPF já cadastrado
3. Tentar salvar

**Resultado Esperado:**
- Erro de validação exibido
- Cadastro não permitido
- Mensagem clara sobre CPF duplicado

### CT012 - Cadastrar produto completo
**Objetivo:** Verificar cadastro de produto com todos os campos  
**Pré-condições:** Gerenciador logado  
**Passos:**
1. Acessar "Cadastrar Produto"
2. Preencher dados obrigatórios:
   - Código: "PROD001"
   - Nome: "Produto Teste"
   - Grupo: "Eletrônicos"
   - Custo: R$ 100,00
   - Margem: 30%
   - Estoque: 50 unidades
3. Configurar promoção: 10%
4. Selecionar impostos aplicáveis
5. Salvar

**Resultado Esperado:**
- Produto criado com preço calculado automaticamente
- Aparece na lista com grupo e estoque
- Disponível para pedidos

### CT013 - Cadastrar produto - Código duplicado
**Objetivo:** Verificar validação de código único  
**Pré-condições:** Produto existe com código específico  
**Passos:**
1. Tentar cadastrar produto com código existente
2. Verificar validação

**Resultado Esperado:**
- Erro de validação
- Cadastro bloqueado
- Sugestão de código alternativo

---

## 📦 Cenários para Gerente de Estoque {#estoque}

### CT014 - Avaliar pedido com estoque suficiente
**Objetivo:** Verificar aprovação de pedido com produtos disponíveis  
**Pré-condições:** Gerente logado, pedido pendente, estoque suficiente  
**Passos:**
1. Acessar "Pedidos Pendentes"
2. Selecionar pedido para avaliação
3. Verificar disponibilidade dos produtos
4. Clicar em "Aprovar"

**Resultado Esperado:**
- Status alterado para "Aprovado"
- Notificação enviada ao promotor
- Pedido disponível para programação de entrega

### CT015 - Avaliar pedido com estoque insuficiente
**Objetivo:** Verificar tratamento de estoque insuficiente  
**Pré-condições:** Pedido com produtos sem estoque  
**Passos:**
1. Acessar pedido pendente
2. Verificar produtos destacados em vermelho
3. Clicar em "Marcar como Insuficiente"
4. Adicionar observações

**Resultado Esperado:**
- Produtos sem estoque destacados visualmente
- Status alterado para "Estoque Insuficiente"
- Notificações enviadas
- Observações salvas

### CT016 - Programar entrega
**Objetivo:** Verificar agendamento de entrega  
**Pré-condições:** Pedido aprovado, estoque disponível  
**Passos:**
1. Acessar "Pedidos Aprovados"
2. Selecionar pedido
3. Escolher data de entrega: "25/07/2025"
4. Confirmar programação

**Resultado Esperado:**
- Data de entrega definida
- Estoque automaticamente reservado
- Status alterado para "Programado"
- Cliente e promotor notificados

### CT017 - Impedir agendamento sem estoque
**Objetivo:** Verificar bloqueio quando não há produtos  
**Pré-condições:** Pedido aprovado, estoque zerado após aprovação  
**Passos:**
1. Tentar programar entrega
2. Verificar validação de estoque

**Resultado Esperado:**
- Sistema impede agendamento
- Mensagem de erro clara
- Sugestão de reavaliação do pedido

### CT018 - Processar entrega no dia
**Objetivo:** Verificar processamento de entrega na data correta  
**Pré-condições:** Data atual = data de entrega programada  
**Passos:**
1. Acessar "Entregas do Dia"
2. Verificar pedidos listados
3. Selecionar pedido
4. Clicar em "Processar Entrega"

**Resultado Esperado:**
- Apenas pedidos do dia aparecem
- Status alterado para "Processado"
- Pedido removido da lista
- Notificações enviadas

### CT019 - Relatório de produtos por categoria
**Objetivo:** Verificar geração de relatório de estoque  
**Pré-condições:** Produtos cadastrados em diferentes categorias  
**Passos:**
1. Acessar "Relatórios de Produtos"
2. Selecionar tipo: "Por Grupo"
3. Escolher grupo: "Eletrônicos"
4. Gerar relatório
5. Testar download em PDF

**Resultado Esperado:**
- Relatório gerado com produtos do grupo selecionado
- Colunas: produto, estoque, preço
- Download PDF funcional
- Dados corretos e atualizados

### CT020 - Relatório de estoque baixo
**Objetivo:** Verificar identificação de produtos com estoque baixo  
**Pré-condições:** Produtos com estoque variado  
**Passos:**
1. Definir limite de estoque baixo (ex: 10 unidades)
2. Gerar relatório de "Estoque Baixo"
3. Verificar produtos listados

**Resultado Esperado:**
- Apenas produtos abaixo do limite aparecem
- Destacados em cor de alerta
- Possibilidade de reposição rápida

---

## 💰 Cenários para Gerente de Vendas {#vendas}

### CT021 - Analisar cliente com boa situação
**Objetivo:** Verificar aprovação de pedido para cliente com bom histórico  
**Pré-condições:** Cliente com histórico positivo, pedido pendente  
**Passos:**
1. Acessar "Análise de Clientes"
2. Selecionar pedido para análise
3. Verificar dados do cliente:
   - Nome/CNPJ
   - Valor total do pedido
   - Histórico de pagamentos
4. Clicar em "Aprovar"

**Resultado Esperado:**
- Informações do cliente exibidas claramente
- Status alterado para "Aprovado pelo Vendas"
- Notificações enviadas ao promotor e estoque

### CT022 - Cancelar pedido de cliente problemático
**Objetivo:** Verificar cancelamento com justificativa  
**Pré-condições:** Cliente com restrições, pedido pendente  
**Passos:**
1. Analisar pedido de cliente com histórico ruim
2. Clicar em "Cancelar"
3. Preencher justificativa obrigatória: "Cliente em débito"
4. Confirmar cancelamento

**Resultado Esperado:**
- Campo de justificativa obrigatório
- Pedido cancelado com motivo registrado
- Notificações enviadas
- Histórico mantido para auditoria

### CT023 - Relatório de maiores compradores
**Objetivo:** Verificar relatório de vendas por cliente  
**Pré-condições:** Histórico de vendas existente  
**Passos:**
1. Acessar "Relatórios de Vendas"
2. Selecionar "Maiores Compradores"
3. Definir período: "01/01/2025 a 31/12/2025"
4. Gerar relatório
5. Testar download Excel

**Resultado Esperado:**
- Lista ordenada por valor total de compras
- Colunas: cliente, total de pedidos, valor total, última compra
- Download Excel funcional

### CT024 - Relatório por promotor
**Objetivo:** Verificar performance individual dos promotores  
**Pré-condições:** Múltiplos promotores com vendas  
**Passos:**
1. Selecionar relatório "Por Promotor"
2. Escolher promotor específico ou "Todos"
3. Definir período mensal
4. Gerar relatório

**Resultado Esperado:**
- Dados de vendas por promotor
- Colunas: data, cliente, total, impostos, comissão
- Totalizadores por promotor

### CT025 - Relatório por município
**Objetivo:** Verificar distribuição geográfica das vendas  
**Pré-condições:** Vendas em diferentes municípios  
**Passos:**
1. Selecionar "Relatório por Município"
2. Escolher estado/região
3. Gerar relatório com mapa de calor

**Resultado Esperado:**
- Vendas agrupadas por cidade
- Visualização geográfica
- Identificação de regiões com potencial

---

## 🔗 Cenários de Integração {#integração}

### CT026 - Fluxo completo de pedido
**Objetivo:** Testar todo o ciclo de vida de um pedido  
**Pré-condições:** Todos os perfis configurados  
**Passos:**
1. **Promotor:** Criar pedido para cliente
2. **Estoque:** Avaliar e aprovar pedido
3. **Vendas:** Analisar cliente e aprovar
4. **Estoque:** Programar entrega
5. **Estoque:** Processar entrega no dia
6. **Cliente:** Verificar status atualizado

**Resultado Esperado:**
- Cada etapa funciona corretamente
- Notificações enviadas em todas as transições
- Status sempre atualizado
- Dados consistentes entre todas as telas

### CT027 - Notificações por email
**Objetivo:** Verificar envio de notificações automáticas  
**Pré-condições:** Configuração de email ativa  
**Passos:**
1. Realizar mudança de status de pedido
2. Verificar envio de emails
3. Verificar conteúdo dos emails
4. Testar diferentes tipos de notificação

**Resultado Esperado:**
- Emails enviados automaticamente
- Conteúdo personalizado por tipo de mudança
- Destinatários corretos (cliente, promotor, gerentes)

### CT028 - Sincronização de estoque
**Objetivo:** Verificar atualização automática do estoque  
**Pré-condições:** Produtos com estoque definido  
**Passos:**
1. Verificar estoque inicial
2. Aprovar pedido que consome estoque
3. Programar entrega (reservar estoque)
4. Processar entrega (baixar estoque)
5. Verificar estoque final

**Resultado Esperado:**
- Estoque reservado na programação
- Estoque baixado na entrega
- Valores sempre corretos
- Histórico de movimentação mantido

---

## ⚡ Cenários de Performance {#performance}

### CT029 - Carga de dados massiva
**Objetivo:** Testar sistema com grande volume de dados  
**Pré-condições:** Base de dados com 10.000+ registros  
**Passos:**
1. Acessar listagem de clientes
2. Aplicar filtros
3. Medir tempo de resposta
4. Testar paginação

**Resultado Esperado:**
- Tempo de resposta < 3 segundos
- Paginação eficiente
- Filtros responsivos
- Interface não trava

### CT030 - Acesso simultâneo
**Objetivo:** Verificar comportamento com múltiplos usuários  
**Pré-condições:** 5+ usuários diferentes  
**Passos:**
1. Fazer login simultâneo de múltiplos usuários
2. Executar operações concorrentes
3. Verificar conflitos de dados
4. Testar locks otimistas

**Resultado Esperado:**
- Sistema mantém performance
- Não há corrupção de dados
- Conflitos tratados adequadamente
- Sessões independentes

---

## 🚨 Cenários de Erro

### CT031 - Falha na conexão com banco
**Objetivo:** Verificar tratamento de erro de banco  
**Pré-condições:** Simular falha de conectividade  
**Passos:**
1. Desconectar banco de dados
2. Tentar realizar operação
3. Verificar mensagem de erro
4. Reconnectar e verificar recuperação

**Resultado Esperado:**
- Mensagem de erro amigável
- Sistema não quebra
- Recuperação automática quando possível

### CT032 - Validação de campos obrigatórios
**Objetivo:** Verificar validações front-end e back-end  
**Pré-condições:** Formulários diversos  
**Passos:**
1. Tentar submeter formulário vazio
2. Preencher parcialmente
3. Usar dados inválidos
4. Testar caracteres especiais

**Resultado Esperado:**
- Validação front-end impede submissão
- Back-end valida novamente
- Mensagens claras de erro
- Dados não corrompidos

---

## 📊 Métricas de Sucesso

### Critérios de Aceitação Geral:
- ✅ 100% dos cenários principais passam
- ✅ Tempo de resposta < 3 segundos para 95% das operações
- ✅ 0 erros críticos ou perda de dados
- ✅ Interface responsiva em dispositivos móveis
- ✅ Compatibilidade com principais navegadores
- ✅ Segurança: nenhum acesso não autorizado possível

### Cobertura de Testes:
- **Funcional:** 100% das user stories cobertas
- **Integração:** Todos os fluxos principais testados
- **Performance:** Carga normal e picos testados
- **Segurança:** Autenticação e autorização validadas
- **Usabilidade:** Interface testada com usuários reais

---

## 📝 Observações para Execução

### Ambiente de Teste:
- Base de dados isolada com dados de teste
- Configuração de email para ambiente de teste
- Logs detalhados habilitados
- Backup antes dos testes destrutivos

### Dados de Teste Necessários:
- Usuários de cada perfil (admin, promotor, cliente, gerentes)
- Produtos variados com diferentes estoques
- Clientes com históricos diversos
- Regiões e municípios cadastrados
- Pedidos em diferentes status

### Ferramentas Recomendadas:
- Selenium para testes automatizados
- Postman para testes de API
- JMeter para testes de performance
- Checklist manual para validação final

---

*Documento criado em: Julho 2025*  
*Versão: 1.0*  
*Última atualização: {{ today|date:"d/m/Y" }}*
