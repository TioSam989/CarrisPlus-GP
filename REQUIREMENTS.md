# CarrisPlus - Requisitos do Projeto
## Project Requirements Documentation

---

**Projeto:** CarrisPlus - Sistema de Gestão de Documentos Online da Carris

**Equipa:** Davi (2024301), Iago (2024195), Ana (2024184)

**Instituição:** [Nome da Instituição]

**Curso:** Engenharia Informática

**Ano Letivo:** 2024/2025

---

## 1. RESUMO DO PROJETO / PROJECT SUMMARY

### Problema / Problem
As pessoas perdem muito tempo à espera nos balcões da Carris para resolver questões simples relacionadas com passes e documentação. O processo atual exige:
- Deslocação física obrigatória aos balcões
- Longas filas de espera
- Dificuldade para pessoas com mobilidade reduzida ou falta de tempo
- Processamento manual lento de documentos

### Solução / Solution
Plataforma web que permite submeter documentos, criar e renovar passes da Carris totalmente online, com validação automática usando Inteligência Artificial para verificar:
- Correspondência de nomes nos documentos vs. base de dados
- Validação de NIF (Número de Identificação Fiscal)
- Extração automática de dados de documentos (OCR)
- Verificação de autenticidade de documentos

### Objetivo / Objective
Eliminar 90% das deslocações físicas desnecessárias aos balcões da Carris, disponibilizando um serviço 24/7 que processa pedidos automaticamente através de validação inteligente.

---

## 2. REQUISITOS FUNCIONAIS / FUNCTIONAL REQUIREMENTS

### RF-001: Registo e Autenticação de Utilizadores

#### RF-001.1 - Registo de Novo Utilizador
**Descrição:** O sistema permite que cidadãos criem uma conta na plataforma CarrisPlus.

**Entradas:**
- Nome completo
- Email válido
- NIF (Número de Identificação Fiscal - 9 dígitos)
- Palavra-passe (mínimo 8 caracteres)
- Confirmação de palavra-passe

**Processamento:**
1. Validar formato do email
2. Verificar se email já existe no sistema
3. Validar formato do NIF português (9 dígitos numéricos)
4. Verificar força da palavra-passe
5. Hash seguro da palavra-passe (bcrypt)
6. Criar conta com status "Ativa"
7. Enviar email de confirmação

**Saídas:**
- Conta criada com sucesso
- Email de boas-vindas
- Redirecionamento para login

**Critérios de Aceitação:**
- ✓ Sistema aceita emails únicos e válidos
- ✓ NIF é validado segundo formato português
- ✓ Palavra-passe é armazenada com hash seguro
- ✓ Utilizador recebe email de confirmação em menos de 1 minuto

**Prioridade:** Alta

---

#### RF-001.2 - Login de Utilizador
**Descrição:** Utilizadores registados podem aceder ao sistema.

**Entradas:**
- Email
- Palavra-passe

**Processamento:**
1. Verificar se email existe
2. Validar palavra-passe (comparação de hash)
3. Criar sessão segura
4. Registar acesso no histórico

**Saídas:**
- Sessão iniciada
- Acesso ao painel pessoal
- Token de autenticação JWT (válido 24 horas)

**Regras de Segurança:**
- Máximo 5 tentativas de login incorretas
- Bloqueio temporário de 15 minutos após 5 falhas
- Sessão expira após 24 horas ou logout manual

**Critérios de Aceitação:**
- ✓ Login bem-sucedido com credenciais corretas
- ✓ Mensagem de erro clara para credenciais inválidas
- ✓ Proteção contra ataques de força bruta

**Prioridade:** Alta

---

#### RF-001.3 - Recuperação de Palavra-passe
**Descrição:** Utilizador pode recuperar acesso via email.

**Processamento:**
1. Utilizador introduz email
2. Sistema envia link de recuperação (válido 1 hora)
3. Utilizador acede ao link e define nova palavra-passe
4. Sistema valida e atualiza palavra-passe

**Prioridade:** Média

---

### RF-002: Submissão de Documentos

#### RF-002.1 - Upload de Documento
**Descrição:** Utilizadores podem submeter documentos digitalizados necessários para criação/renovação de passes.

**Entradas:**
- Ficheiro digital (PDF, JPG, JPEG, PNG)
- Tipo de documento (seleção dropdown):
  - Cartão de Cidadão
  - Passaporte
  - Certificado Escolar (para passes estudante)
  - Declaração de Entidade Patronal (para passes sociais)
  - Comprovativo de Rendimentos
  - Atestado Médico
- Notas adicionais (opcional, máximo 500 caracteres)

**Processamento:**
1. Validar formato do ficheiro (magic bytes, não apenas extensão)
2. Verificar tamanho (máximo 5 MB)
3. Scan antivírus do ficheiro
4. Gerar nome único e seguro
5. Armazenar em diretório protegido
6. Criar registo na base de dados com status "Pendente"
7. Gerar número de protocolo único

**Saídas:**
- Confirmação de upload bem-sucedido
- Número de protocolo (ex: CP2024-001234)
- Data e hora de submissão
- Status inicial: "Pendente Validação"

**Regras de Negócio:**
- Tamanho máximo por ficheiro: 5 MB
- Formatos aceites: PDF, JPG, JPEG, PNG
- Resolução mínima recomendada: 300 DPI
- Máximo de 5 ficheiros por submissão
- Nome de ficheiro não pode conter caracteres especiais perigosos

**Critérios de Aceitação:**
- ✓ Upload aceita todos os formatos válidos
- ✓ Sistema rejeita ficheiros muito grandes com mensagem clara
- ✓ Sistema rejeita formatos não permitidos
- ✓ Protocolo único é gerado automaticamente
- ✓ Feedback visual do progresso de upload

**Prioridade:** Alta

---

#### RF-002.2 - Validação Automática com IA
**Descrição:** Sistema valida automaticamente documentos submetidos usando tecnologias de IA e OCR.

**Entradas:**
- Ficheiro de documento submetido
- Tipo de documento declarado pelo utilizador
- Dados pessoais do utilizador (nome, NIF)

**Processamento:**

**Etapa 1 - Extração OCR:**
1. Aplicar OCR (Optical Character Recognition) ao documento
2. Extrair texto estruturado
3. Identificar e extrair campos-chave:
   - Nome completo
   - Número de Identificação Fiscal (NIF)
   - Data de nascimento
   - Data de validade do documento
   - Número do documento

**Etapa 2 - Validação de Dados:**
1. Comparar nome extraído vs. nome registado na conta
   - Aceitar variações (ex: "João Silva" = "Joao Silva")
   - Tolerar diferenças de maiúsculas/minúsculas
2. Validar NIF extraído vs. NIF do utilizador
   - Verificação exata (9 dígitos)
3. Verificar data de validade do documento
   - Documento não pode estar vencido
4. Validar estrutura e formato do documento

**Etapa 3 - Verificação de Autenticidade:**
1. Analisar qualidade da imagem
2. Detetar possíveis adulterações digitais
3. Verificar elementos de segurança visíveis (se aplicável)
4. Detetar se imagem é cópia de ecrã ou scan original

**Etapa 4 - Scoring de Confiança:**
- Calcular score de confiança (0-100%)
- Atribuir pesos aos critérios validados
- Determinar classificação final

**Saídas:**
- Status do documento:
  - **Aprovado Automaticamente** (score > 90%)
  - **Revisão Manual Necessária** (score 70-90%)
  - **Rejeitado Automaticamente** (score < 70%)
- Score de confiança (0-100%)
- Lista detalhada de discrepâncias encontradas
- Dados extraídos estruturados (JSON)
- Tempo de processamento

**Regras de Decisão:**
- Score > 90%: Aprovação automática imediata
- Score 70-90%: Enviar para fila de revisão manual por administrador
- Score < 70%: Rejeição automática com motivo claro
- Documentos vencidos: Rejeição automática independente do score

**Critérios de Aceitação:**
- ✓ OCR extrai dados com precisão mínima de 95%
- ✓ Validação de NIF funciona corretamente
- ✓ Sistema aceita variações normais de nomes
- ✓ Identifica documentos vencidos corretamente
- ✓ Processamento completo em menos de 15 segundos
- ✓ Utilizador recebe email com resultado da validação

**Tecnologias Utilizadas:**
- pytesseract: OCR engine
- OpenCV: Processamento de imagem
- TensorFlow/PyTorch: Modelos de classificação (opcional)
- Algoritmos de matching de strings (Levenshtein distance)

**Prioridade:** Alta (Funcionalidade Core)

---

#### RF-002.3 - Histórico de Documentos Submetidos
**Descrição:** Utilizador pode visualizar todos os documentos que submeteu.

**Visualização Inclui:**
- Lista de todos os documentos
- Tipo de documento
- Data de submissão
- Status atual (Pendente / Aprovado / Rejeitado / Em Revisão)
- Número de protocolo
- Opções: Visualizar / Resubmeter (se rejeitado)

**Prioridade:** Média

---

### RF-003: Gestão de Passes

#### RF-003.1 - Criação de Novo Passe
**Descrição:** Utilizadores podem solicitar criação de novo passe da Carris online.

**Entradas:**
- Tipo de passe:
  - **Passe Normal** - Tarifa completa
  - **Passe Estudante** - Descontos para estudantes
  - **Passe Sénior** - Para maiores de 65 anos
  - **Passe Social** - Para cidadãos com rendimentos baixos
- Zona tarifária (Lisboa, Lisboa + Cascais, etc.)
- Documentos comprovativos (submetidos previamente)
- Fotografia tipo passe (opcional)

**Processamento:**
1. Verificar se utilizador tem documentos aprovados
2. Validar requisitos específicos do tipo de passe selecionado
3. Calcular preço baseado em tipo e zona
4. Verificar condições especiais (idade para sénior, certificado para estudante)
5. Criar passe provisório com status "Pendente Aprovação"
6. Gerar número do passe
7. Criar PDF com comprovante provisório

**Saídas:**
- Passe criado com status "Pendente"
- Número único do passe (ex: PS2024-123456)
- Data estimada de ativação (5 dias úteis)
- Comprovante em PDF para download
- Email de confirmação

**Regras de Negócio por Tipo de Passe:**

**Passe Estudante:**
- Requisito: Certificado de matrícula válido (ano letivo atual)
- Idade: 4 a 23 anos
- Renovação: Anual obrigatória
- Desconto: 40% sobre tarifa normal

**Passe Sénior:**
- Requisito: Cartão de Cidadão
- Idade: 65+ anos (validação automática via data de nascimento)
- Desconto: 50% sobre tarifa normal
- Validade: Até 1 ano

**Passe Social:**
- Requisito: Declaração de rendimentos ou comprovativo de beneficiário de apoios sociais
- Rendimento máximo: 1.5x IAS (Indexante dos Apoios Sociais)
- Renovação: Semestral
- Desconto: 60% sobre tarifa normal

**Passe Normal:**
- Requisito: Apenas Cartão de Cidadão ou Passaporte
- Sem restrições de idade ou rendimento
- Validade: Até 1 ano

**Critérios de Aceitação:**
- ✓ Sistema valida automaticamente requisitos por tipo de passe
- ✓ Cálculo de preço está correto
- ✓ PDF é gerado automaticamente
- ✓ Utilizador recebe email com próximos passos

**Prioridade:** Alta

---

#### RF-003.2 - Renovação de Passe Existente
**Descrição:** Utilizador pode renovar passe antes do vencimento.

**Processamento:**
1. Sistema envia lembrete automático 30 dias antes do vencimento
2. Utilizador acede à área de renovação
3. Sistema pré-preenche dados do passe anterior
4. Utilizador confirma ou atualiza documentos
5. Sistema valida e processa renovação
6. Novo período de validade é aplicado

**Facilidades:**
- Dados pré-preenchidos
- Documentos anteriores reutilizados se ainda válidos
- Processo mais rápido que criação nova

**Prioridade:** Alta

---

#### RF-003.3 - Consulta de Passe Ativo
**Descrição:** Visualizar detalhes do passe ativo.

**Informações Exibidas:**
- Número do passe
- Tipo de passe
- Zona tarifária
- Data de início
- Data de validade
- Status (Ativo / Expirado / Pendente)
- QR Code para validação (futuro)

**Prioridade:** Média

---

### RF-004: Painel de Administração

#### RF-004.1 - Dashboard Administrativo
**Descrição:** Painel para administradores da Carris visualizarem estatísticas e métricas.

**Informações Exibidas:**
- Documentos pendentes de revisão manual (número)
- Total de documentos processados (hoje / semana / mês)
- Taxa de aprovação automática vs. manual
- Total de passes ativos
- Total de utilizadores registados
- Passes criados por tipo (gráfico)
- Documentos por status (gráfico)
- Tendências temporais

**Prioridade:** Média

---

#### RF-004.2 - Revisão Manual de Documentos
**Descrição:** Interface para administradores revisarem documentos que o sistema sinalizou para revisão manual (score 70-90%).

**Funcionalidades:**
- Visualização lado a lado:
  - Documento original (imagem)
  - Dados extraídos pelo OCR
- Informações apresentadas:
  - Score de confiança da IA
  - Discrepâncias identificadas
  - Histórico do utilizador
  - Razão da sinalização
- Ações disponíveis:
  - **Aprovar** - Documento é válido
  - **Rejeitar** - Documento inválido ou fraudulento
  - **Solicitar Resubmissão** - Documento ilegível ou incompleto
- Campo para comentários/feedback ao utilizador

**Critérios de Aceitação:**
- ✓ Admin pode visualizar documento em alta resolução
- ✓ Dados extraídos são apresentados claramente
- ✓ Utilizador recebe email após decisão do admin

**Prioridade:** Alta (necessário para sistema funcionar completamente)

---

#### RF-004.3 - Gestão de Utilizadores
**Descrição:** Administradores podem gerir contas de utilizadores.

**Funcionalidades:**
- Listar todos os utilizadores
- Buscar por nome, email ou NIF
- Filtros (ativos, inativos, data de registo)
- Ver histórico de atividades do utilizador
- Ações:
  - Desativar conta (suspender temporariamente)
  - Reativar conta
  - Resetar palavra-passe (enviar link de recuperação)
  - Ver documentos submetidos
  - Ver passes criados

**Prioridade:** Baixa

---

### RF-005: Sistema de Notificações

#### RF-005.1 - Notificações Automáticas por Email
**Descrição:** Sistema envia emails automáticos para eventos importantes.

**Eventos de Notificação:**

1. **Registo Completo:**
   - Assunto: "Bem-vindo ao CarrisPlus"
   - Conteúdo: Instruções de como usar o sistema

2. **Documento Submetido:**
   - Assunto: "Documento recebido - Protocolo #[número]"
   - Conteúdo: Confirmação, protocolo, tempo estimado de processamento

3. **Documento Aprovado:**
   - Assunto: "Documento aprovado ✓"
   - Conteúdo: Informação de que pode prosseguir com criação de passe

4. **Documento Rejeitado:**
   - Assunto: "Documento não aprovado - Ação necessária"
   - Conteúdo: Motivo da rejeição, instruções para resubmissão

5. **Passe Criado:**
   - Assunto: "Novo passe CarrisPlus ativado"
   - Conteúdo: Número do passe, validade, PDF em anexo

6. **Passe Próximo do Vencimento:**
   - Assunto: "Seu passe vence em 30 dias"
   - Conteúdo: Link direto para renovação
   - Enviado: 30 dias antes do vencimento

7. **Documento em Revisão Manual:**
   - Assunto: "Documento em análise"
   - Conteúdo: Informar que requer revisão adicional

**Template de Email:**
- Cabeçalho com logo da Carris
- Mensagem personalizada (nome do utilizador)
- Call-to-action (botão para ação relevante)
- Footer com informações de contato e links úteis

**Prioridade:** Alta

---

### RF-006: Relatórios e Estatísticas

#### RF-006.1 - Geração de Relatórios (Admin)
**Descrição:** Administradores podem gerar relatórios para análise.

**Tipos de Relatórios:**
- Documentos processados por período (diário, semanal, mensal)
- Taxa de aprovação automática vs. manual vs. rejeição
- Tempo médio de processamento
- Passes criados por tipo
- Utilizadores ativos vs. inativos
- Documentos por tipo mais submetidos

**Formatos de Exportação:**
- PDF (para apresentações)
- Excel (XLSX) para análise
- CSV para processamento externo

**Prioridade:** Baixa

---

## 3. REQUISITOS NÃO-FUNCIONAIS / NON-FUNCTIONAL REQUIREMENTS

### RNF-001: Performance e Desempenho

#### RNF-001.1 - Tempo de Resposta
**Descrição:** O sistema deve responder rapidamente para garantir boa experiência do utilizador.

**Requisitos de Tempo:**
- Carregamento de página web: **< 2 segundos**
- Upload de documento (5MB): **< 5 segundos**
- Processamento OCR completo: **< 15 segundos**
- Consultas à base de dados: **< 500 milissegundos**
- Login de utilizador: **< 1 segundo**

**Métricas de Avaliação:**
- 95% das requisições devem cumprir os tempos especificados
- Medição: Google Lighthouse, Apache JMeter

**Justificação:**
Tempos de resposta rápidos são críticos para adoção do sistema. Se o processo online for lento, utilizadores preferirão métodos tradicionais.

**Prioridade:** Alta

---

#### RNF-001.2 - Escalabilidade
**Descrição:** Sistema deve suportar crescimento de utilizadores sem degradação de performance.

**Requisitos:**
- Suportar **1.000 utilizadores simultâneos** sem degradação
- Processar **10.000 documentos por dia**
- Crescimento horizontal via containerização (Docker)
- Arquitetura preparada para load balancing

**Estratégias Técnicas:**
- Docker Compose para múltiplas instâncias da aplicação
- Redis para cache de sessões e dados frequentes
- CDN para assets estáticos (CSS, JS, imagens)
- Database connection pooling
- Queue system para processamento assíncrono (Celery)

**Justificação:**
Carris tem milhares de utilizadores potenciais em Lisboa. Sistema deve crescer com a demanda.

**Prioridade:** Média

---

#### RNF-001.3 - Disponibilidade
**Descrição:** Sistema deve estar disponível 24 horas por dia, 7 dias por semana.

**Requisitos:**
- **Uptime mínimo: 99.5%** (downtime máximo: 3.65 horas por mês)
- Backup automático diário da base de dados
- Plano de recuperação de desastres documentado
- Monitorização contínua com alertas

**Manutenção Planeada:**
- Janelas de manutenção: Madrugada (02:00-04:00)
- Notificação prévia aos utilizadores (48 horas)

**Justificação:**
Principal vantagem sobre balcões físicos é disponibilidade 24/7.

**Prioridade:** Alta

---

### RNF-002: Segurança e Privacidade

#### RNF-002.1 - Autenticação e Autorização
**Descrição:** Acesso ao sistema deve ser seguro e controlado.

**Requisitos:**
- Autenticação via email e palavra-passe
- **Hash de passwords:** bcrypt com salt rounds = 12
- **Tokens JWT** com expiração de 24 horas
- Renovação automática de tokens
- Sistema de roles:
  - **User** - Utilizador comum
  - **Admin** - Administrador da Carris
  - **SuperAdmin** - Administrador do sistema

**Proteções:**
- **Rate limiting:** Máximo 5 tentativas de login incorretas
- **Bloqueio temporário:** 15 minutos após 5 falhas consecutivas
- **Logout automático:** Após 30 minutos de inatividade
- **Password strength:** Mínimo 8 caracteres com números

**Justificação:**
Dados pessoais sensíveis (NIF, documentos) exigem segurança robusta.

**Prioridade:** Crítica

---

#### RNF-002.2 - Proteção de Dados (RGPD/GDPR)
**Descrição:** Sistema deve proteger dados pessoais dos utilizadores conforme RGPD.

**Requisitos de Comunicação:**
- **HTTPS obrigatório** com TLS 1.3
- Certificado SSL válido

**Requisitos de Armazenamento:**
- Encriptação de dados sensíveis em repouso (AES-256)
- Passwords nunca armazenadas em texto plano
- NIFs armazenados com encriptação

**Requisitos de Aplicação:**
- Sanitização de todos os inputs
- Proteção contra SQL Injection (uso de ORM)
- Proteção contra XSS (Cross-Site Scripting)
- CSRF tokens em todos os formulários
- Content Security Policy headers configurados

**Compliance RGPD:**
- Política de privacidade clara e acessível
- Consentimento explícito para recolha de dados
- Direito ao esquecimento (utilizador pode apagar conta)
- Direito à portabilidade de dados
- Notificação de violações em 72 horas

**Justificação:**
RGPD é lei obrigatória na UE. Violações podem resultar em multas pesadas.

**Prioridade:** Crítica

---

#### RNF-002.3 - Segurança de Ficheiros
**Descrição:** Upload de ficheiros deve ser seguro para prevenir malware e exploits.

**Requisitos:**
- Validação de tipo via **magic bytes** (não confiar apenas na extensão)
- Scan antivírus automático de todos os uploads (ClamAV)
- Armazenamento fora do webroot
- Nomes de ficheiro sanitizados (remover caracteres especiais)
- Limites de tamanho enforçados (5MB máximo)
- Isolamento de ficheiros por utilizador (permissões)

**Validações:**
```
1. Check magic bytes (primeiros bytes do ficheiro)
2. Verificar extensão permitida
3. Verificar tamanho < 5MB
4. Scan antivírus
5. Sanitizar nome do ficheiro
6. Armazenar com nome único (UUID)
```

**Justificação:**
Upload de ficheiros é vetor comum de ataques. Proteção é essencial.

**Prioridade:** Alta

---

#### RNF-002.4 - Auditoria e Logs
**Descrição:** Todas as ações importantes devem ser registadas para auditoria.

**Eventos Logged:**
- Login / Logout (incluindo IPs)
- Submissão de documentos
- Aprovação / Rejeição de documentos
- Criação / Renovação de passes
- Alterações por administradores
- Tentativas de acesso não autorizadas
- Erros críticos do sistema

**Informações Registadas:**
- Timestamp (ISO 8601)
- User ID
- IP Address
- User Agent
- Ação realizada
- Resultado (sucesso / falha)
- Detalhes relevantes (JSON)

**Retenção:** Logs mantidos por 1 ano

**Justificação:**
Logs são essenciais para investigação de incidentes e compliance.

**Prioridade:** Média

---

### RNF-003: Usabilidade e Experiência do Utilizador

#### RNF-003.1 - Interface Intuitiva
**Descrição:** Interface deve ser fácil de usar para todos os públicos, incluindo idosos.

**Requisitos:**
- Design limpo e minimalista (sem sobrecarga visual)
- Navegação clara (máximo 3 cliques para qualquer função)
- Feedback visual para todas as ações
- Mensagens de erro claras e acionáveis
- Ajuda contextual disponível (tooltips)
- Linguagem simples e objetiva

**Acessibilidade (WCAG 2.1 Level AA):**
- Suporte a leitores de tela (screen readers)
- Contraste adequado (mínimo 4.5:1 para texto normal)
- Navegação completa por teclado (sem mouse)
- Tamanhos de fonte ajustáveis
- Alt text em todas as imagens
- Labels descritivos em formulários

**Justificação:**
Público-alvo inclui idosos e pessoas com baixa literacia digital.

**Prioridade:** Alta

---

#### RNF-003.2 - Responsividade Multi-Dispositivo
**Descrição:** Sistema deve funcionar perfeitamente em todos os dispositivos.

**Dispositivos Suportados:**
- **Desktop:** 1920x1080 e superiores
- **Tablet:** 768x1024 (iPad, Android tablets)
- **Mobile:** 375x667 e superiores (smartphones)

**Requisitos de Design:**
- Layout responsivo (CSS Grid / Flexbox)
- Touch-friendly (botões mínimo 44x44 pixels)
- Imagens otimizadas por resolução
- Fontes legíveis em telas pequenas

**Browsers Suportados:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Justificação:**
Cada vez mais pessoas usam smartphones como dispositivo principal.

**Prioridade:** Alta

---

#### RNF-003.3 - Multilíngue
**Descrição:** Sistema deve suportar múltiplos idiomas.

**Idiomas:**
- **Português (PT-PT)** - Idioma principal
- **Inglês (EN-GB)** - Idioma secundário (para turistas/expats)

**Implementação:**
- Seletor de idioma visível
- Preferência salva por utilizador
- Emails enviados no idioma do utilizador

**Prioridade:** Baixa (pode ser implementado futuramente)

---

### RNF-004: Manutenibilidade e Qualidade de Código

#### RNF-004.1 - Código Limpo e Documentado
**Descrição:** Código deve ser fácil de entender e manter.

**Requisitos:**
- Seguir padrões **PEP 8** (Python)
- Comentários em código complexo
- Docstrings em todas as funções
- Nomes de variáveis descritivos (não abreviar desnecessariamente)
- Funções pequenas e focadas (< 50 linhas idealmente)
- Princípio DRY (Don't Repeat Yourself)

**Exemplo:**
```python
def validate_nif(nif: str) -> bool:
    """
    Valida se NIF português é válido.

    Args:
        nif: String com 9 dígitos numéricos

    Returns:
        True se NIF válido, False caso contrário
    """
    # Implementation
```

**Justificação:**
Projeto académico deve demonstrar boas práticas de engenharia de software.

**Prioridade:** Média

---

#### RNF-004.2 - Testes Automatizados
**Descrição:** Código deve ter cobertura de testes para garantir qualidade.

**Requisitos:**
- **Cobertura mínima: 80%**
- **Testes unitários** (pytest) - Funções individuais
- **Testes de integração** - Componentes interagindo
- **Testes end-to-end** (Selenium) - Fluxos completos
- CI/CD pipeline (GitHub Actions) - Testes automáticos em cada commit

**Casos de Teste Prioritários:**
- Registo de utilizador
- Login
- Upload de documento
- Validação OCR
- Criação de passe

**Justificação:**
Testes previnem bugs e facilitam refactoring.

**Prioridade:** Média (essencial antes de produção)

---

### RNF-005: Tecnologias e Compatibilidade

#### RNF-005.1 - Containerização
**Descrição:** Aplicação deve rodar em containers para facilitar deployment.

**Requisitos:**
- Docker image otimizada (< 500MB idealmente)
- Docker Compose para orquestração
- Variáveis de ambiente configuráveis (.env)
- Volumes para persistência de dados
- Network isolation entre serviços

**Justificação:**
Containers garantem ambiente consistente (desenvolvimento = produção).

**Prioridade:** Alta (já implementado)

---

#### RNF-005.2 - Base de Dados
**Descrição:** Sistema de persistência de dados.

**Requisitos:**
- **PostgreSQL 15+** para produção (robustez, ACID)
- SQLite para desenvolvimento local (simplicidade)
- Migrations com Alembic (controlo de versões do schema)
- Backup automático diário
- Índices em campos frequentemente consultados

**Justificação:**
PostgreSQL é robusto, gratuito e amplamente suportado.

**Prioridade:** Alta

---

### RNF-006: Compliance Legal

#### RNF-006.1 - Conformidade RGPD
**Descrição:** Sistema deve cumprir Regulamento Geral de Proteção de Dados.

**Requisitos Obrigatórios:**
- **Consentimento explícito** para recolha de dados
- **Política de privacidade** visível e compreensível
- **Direito ao esquecimento** - Utilizador pode apagar conta
- **Direito à portabilidade** - Utilizador pode exportar dados
- **Notificação de violações** em 72 horas às autoridades

**Dados Recolhidos:**
- Nome (necessário - identificação)
- Email (necessário - comunicação)
- NIF (necessário - validação de documentos)
- Documentos (necessário - criação de passes)

**Dados NÃO Recolhidos:**
- Localização GPS
- Comportamento de navegação (sem analytics intrusivos)
- Dados desnecessários

**Justificação:**
RGPD é lei obrigatória na União Europeia.

**Prioridade:** Crítica

---

#### RNF-006.2 - Termos de Serviço
**Descrição:** Termos claros de utilização do sistema.

**Conteúdo Necessário:**
- Condições de uso do sistema
- Responsabilidades do utilizador
- Responsabilidades da Carris
- Limitações de responsabilidade
- Política de cookies (se aplicável)

**Aceitação:**
- Utilizador deve aceitar termos ao registar-se
- Checkbox obrigatório "Li e aceito os Termos de Serviço"

**Prioridade:** Média

---

## 4. TECNOLOGIAS UTILIZADAS / TECHNOLOGIES USED

### Stack Tecnológico

**Backend:**
- Python 3.11
- Flask 2.3.3 (Web framework)
- SQLAlchemy (ORM)
- Flask-Login (Autenticação)
- bcrypt (Password hashing)
- PyJWT (Tokens)

**IA e Processamento:**
- pytesseract (OCR)
- OpenCV (Processamento de imagem)
- Pillow (Manipulação de imagem)

**Frontend:**
- HTML5 + CSS3 + JavaScript
- Jinja2 (Template engine)

**Database:**
- PostgreSQL 15+

**DevOps:**
- Docker + Docker Compose
- Git + GitHub

**Segurança:**
- ClamAV (Antivírus)
- python-dotenv (Environment variables)

---

## 5. PRIORIZAÇÃO DE REQUISITOS / REQUIREMENTS PRIORITIZATION

### Funcionalidades Críticas (Fase 1 - MVP)
1. ✅ RF-001.1 - Registo de utilizador
2. ✅ RF-001.2 - Login
3. ✅ RF-002.1 - Upload de documento
4. ✅ RF-002.2 - Validação IA/OCR
5. ✅ RF-003.1 - Criação de passe
6. ✅ RF-004.2 - Revisão manual (Admin)
7. ✅ RF-005.1 - Notificações por email

### Funcionalidades Importantes (Fase 2)
8. RF-003.2 - Renovação de passe
9. RF-004.1 - Dashboard admin
10. RF-002.3 - Histórico de documentos
11. RF-001.3 - Recuperação de password

### Funcionalidades Desejáveis (Fase 3)
12. RF-004.3 - Gestão de utilizadores
13. RF-006.1 - Relatórios
14. RF-003.3 - Consulta de passe

---

## 6. CRITÉRIOS DE SUCESSO / SUCCESS CRITERIA

O projeto será considerado bem-sucedido se:

✅ **Funcionalidades Core implementadas:**
- Utilizadores podem registar-se e fazer login
- Utilizadores podem submeter documentos
- Sistema valida documentos automaticamente (OCR)
- Utilizadores podem criar passes online
- Admins podem revisar documentos manualmente

✅ **Requisitos Não-Funcionais cumpridos:**
- Sistema responde em < 2 segundos
- Segurança implementada (HTTPS, hash passwords)
- Interface responsiva funciona em mobile
- RGPD compliant

✅ **Métricas de Impacto:**
- Redução de 70%+ no tempo de processamento
- Taxa de aprovação automática > 80%
- Satisfação do utilizador > 4/5 estrelas

---

## ANEXO A: GLOSSÁRIO / GLOSSARY

- **NIF:** Número de Identificação Fiscal (9 dígitos, Portugal)
- **OCR:** Optical Character Recognition (reconhecimento de texto em imagens)
- **RGPD/GDPR:** Regulamento Geral de Proteção de Dados
- **JWT:** JSON Web Token (token de autenticação)
- **IAS:** Indexante dos Apoios Sociais (referência para cálculos sociais)
- **Magic Bytes:** Primeiros bytes de um ficheiro que identificam seu tipo real
- **Hash:** Função criptográfica irreversível para proteger passwords
- **ORM:** Object-Relational Mapping (abstração de base de dados)

---

**FIM DO DOCUMENTO / END OF DOCUMENT**

---

**Versão:** 1.0
**Data:** 2025-11-05
**Autores:** Davi (2024301), Iago (2024195), Ana (2024184)
