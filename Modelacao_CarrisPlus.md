# CarrisPlus - Modelação do Projeto

**Desenvolvimento de Software B | Ano Letivo 2024/2025**

**Equipa:** Davi (2024301), Iago (2024195), Ana (2024184)

---

## 1. VISÃO GERAL

Plataforma web para digitalizar a submissão de documentos e gestão de passes da Carris com validação automática por IA.

**Objetivos:** Reduzir tempo de processamento, eliminar deslocações físicas, disponibilizar serviço 24/7, processar documentos com precisão de 95%+ através de IA.

---

## 2. REQUISITOS FUNCIONAIS

### RF-001: Gestão de Utilizadores
- **Registo:** Nome, email, NIF, password (validação de formato, hash bcrypt)
- **Login:** Autenticação segura com proteção contra força bruta
- **Recuperação de password:** Via email
- **Gestão de perfil:** Visualização e edição de dados pessoais

### RF-002: Submissão de Documentos
- **Upload:** PDF, JPG, PNG (máx. 5MB)
- **Validação automática por IA:**
  - OCR para extração de dados
  - Validação de NIF, nome, data de validade
  - Score de confiança (>90%: aprovação automática, 70-90%: revisão manual, <70%: rejeição)
  - Tempo de processamento <10 segundos
- **Histórico:** Consulta de documentos submetidos com status

### RF-003: Gestão de Passes
- **Tipos de passe:**
  - **Estudante:** Certificado de matrícula, 4-23 anos
  - **Sénior:** 65+ anos, 40% desconto
  - **Normal:** Sem requisitos especiais
- **Funcionalidades:** Criação, renovação, consulta de passe ativo

### RF-004: Painel de Administração
- **Dashboard:** Documentos pendentes, estatísticas, gráficos
- **Revisão manual:** Aprovação/rejeição de documentos com score 70-90%
- **Gestão de utilizadores:** Ativar/desativar contas, resetar passwords

### RF-005: Notificações
- **Emails automáticos:** Confirmação de registo, documento submetido/aprovado/rejeitado, passe ativado, passe próximo do vencimento (30 dias)

---

## 3. REQUISITOS NÃO-FUNCIONAIS

### RNF-001: Performance
- Suportar múltiplos utilizadores simultâneos
- Processamento eficiente de documentos

### RNF-002: Segurança
- HTTPS obrigatório (TLS 1.3)
- Hash de passwords com bcrypt
- Tokens JWT (expiração 24h)
- Rate limiting (máx. 5 tentativas de login)
- Proteção contra SQL Injection, XSS, CSRF
- Validação de ficheiros via magic bytes
- Logs de auditoria (login, submissões, alterações)
- Conformidade com RGPD

### RNF-003: Usabilidade
- Design responsivo (Desktop, Tablet, Mobile)
- Navegação intuitiva
- Feedback visual para todas as ações
- Mensagens de erro claras

### RNF-004: Manutenibilidade
- Código limpo (PEP 8)
- Cobertura de testes: mínimo 70%
- Documentação completa (README, API docs)

### RNF-005: Disponibilidade
- Alta disponibilidade do sistema
- Monitorização contínua

---

## 4. ARQUITETURA DO SISTEMA

O sistema utiliza uma base de dados relacional para armazenar informações de utilizadores, documentos, passes e logs de auditoria.

---

## 5. TECNOLOGIAS

### Backend
- Python 3.11
- Flask 2.3.3
- bcrypt
- PyJWT

### AI/ML
- pytesseract (OCR)
- OpenCV
- Pillow
- TensorFlow

### Base de Dados
- MySQL

### Frontend
- React
- Redux
- HTML5
- CSS3
- JavaScript

### Versionamento
- Git
- Docker

---

**Data:** 2025-11-05
