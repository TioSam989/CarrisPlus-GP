# CarrisPlus - Sistema de Gestão de Documentos Online / Online Document Management System

> **Eliminando Deslocações Desnecessárias com Inovação Digital**
> **Eliminating Unnecessary Travel Through Digital Innovation**

Uma aplicação web moderna desenvolvida em Flask para digitalizar o processo de submissão de documentos e pedidos de passes da Carris (empresa de autocarros de Lisboa). O CarrisPlus permite que os cidadãos submetam documentos, renovem passes e criem novos passes totalmente online, com validação inteligente de dados usando IA.

A modern Flask-based web application designed to digitize the document submission and pass request process for Carris (Lisbon bus company). CarrisPlus enables citizens to submit documents, renew passes, and create new passes entirely online, with intelligent AI-powered data validation.

---

## 👥 Equipa / Team

- **Davi** - 2024301
- **Iago** - 2024195
- **Ana** - 2024184

---

## 🎯 Declaração do Problema / Problem Statement

### Problema Atual / Current Problem:
As pessoas perdem muito tempo à espera para resolver questões simples que poderiam facilmente ser tratadas de forma online. O processo atual exige:

- **Deslocação física obrigatória** aos balcões da Carris
- **Longas filas de espera** para tarefas administrativas simples
- **Dificuldade para pessoas** com constrangimentos de tempo e mobilidade
- **Processamento manual** de documentos com validação demorada

People waste considerable time waiting to resolve simple issues that could easily be handled online. The current process requires:

- **Mandatory physical travel** to Carris offices
- **Long waiting queues** for simple administrative tasks
- **Challenges for people** with time and mobility constraints
- **Manual document processing** with time-consuming validation

### Nossa Solução / Our Solution:
Uma plataforma online abrangente que digitaliza todo o processo de submissão de documentos da Carris, tornando os serviços acessíveis de qualquer lugar, a qualquer momento. O sistema utiliza **validação inteligente com IA** para verificar automaticamente:

A comprehensive online platform that digitizes the entire Carris document submission process, making services accessible from anywhere, anytime. The system uses **intelligent AI validation** to automatically verify:

- ✓ Correspondência de nomes nos documentos vs. base de dados
- ✓ Validação de NIF (Número de Identificação Fiscal)
- ✓ Extração automática de dados de documentos (OCR)
- ✓ Verificação de autenticidade de documentos

---

## ✨ Funcionalidades Implementadas / Implemented Features

### 🟢 Atualmente Funcionais / Currently Functional:

- 📄 **Submissão de Documentos** - Upload digital de documentos (PDF, JPG, PNG)
  - Formulário com campos para tipo de documento e notas
  - Validação básica de formato de ficheiro
  - Armazenamento seguro em diretório dedicado

- 🎨 **Interface Responsiva** - Design adaptável para desktop, tablet e telemóvel
  - Layout grid responsivo com CSS moderno
  - Navegação intuitiva
  - Cartões de serviço com hover effects

- 🐳 **Infraestrutura Docker** - Containerização completa para fácil deployment
  - Docker Compose configurado
  - Environment variables preparadas
  - Volume persistence para uploads

- 🌐 **Sistema de Rotas Flask** - Backend estruturado com endpoints REST
  - `GET /` - Página inicial
  - `GET/POST /submit-document` - Submissão de documentos
  - `GET /renew-document` - Renovação de passes (em desenvolvimento)
  - `GET /create-pass` - Criação de passes (em desenvolvimento)

---

## 🚧 Funcionalidades em Desenvolvimento / Features in Development

### 🔄 Próximas Implementações / Next Implementations:

1. **🤖 Validação Inteligente com IA**
   - OCR (Optical Character Recognition) para extração de dados
   - Validação automática de NIF vs. base de dados
   - Verificação de correspondência de nomes
   - Deteção de documentos fraudulentos
   - Bibliotecas a integrar: pytesseract, OpenCV, TensorFlow/PyTorch

2. **💾 Integração de Base de Dados**
   - PostgreSQL para persistência de dados
   - Models com SQLAlchemy:
     - Utilizadores (User)
     - Documentos (Document)
     - Passes (Pass)
     - Histórico de validações (ValidationHistory)
   - Migrations com Alembic

3. **🔐 Sistema de Autenticação**
   - Registo e login de utilizadores
   - Hash de passwords com bcrypt
   - Gestão de sessões seguras
   - Tokens JWT para API
   - Recuperação de password via email

4. **📋 Painel de Administração**
   - Dashboard para visualização de estatísticas
   - Gestão de documentos pendentes
   - Sistema de aprovação/rejeição
   - Histórico de atividades
   - Relatórios exportáveis

5. **✅ Validação Avançada de Documentos**
   - Verificação de tamanho e formato
   - Análise de metadata
   - Deteção de duplicados
   - Controlo de versões
   - Assinatura digital

6. **📧 Sistema de Notificações**
   - Confirmação de submissão via email
   - Alertas de estado de processamento
   - Notificações SMS (opcional)
   - Webhooks para integrações

7. **🎫 Sistema Completo de Passes**
   - Criação de novos passes online
   - Renovação automática
   - Histórico de passes
   - Download de comprovantes em PDF
   - QR codes para validação

8. **🛡️ Segurança Reforçada**
   - CSRF protection
   - Rate limiting
   - Content Security Policy
   - Sanitização de inputs
   - Audit logging
   - Encriptação de dados sensíveis

---

## 📄 Tipos de Documentos Suportados / Supported Document Types

O sistema está preparado para processar os seguintes documentos da Carris:

The system is prepared to process the following Carris documents:

- 📇 **Cartão de Cidadão / Citizen Card** - Para validação de identidade
- 🛂 **Passaporte / Passport** - Documento alternativo de identificação
- 🎓 **Certificado Escolar / School Certificate** - Para passes estudante
- 💼 **Declaração de Entidade Patronal / Employer Declaration** - Para passes sociais
- 💳 **Comprovativo de Rendimentos / Proof of Income** - Para tarifários especiais
- 🏥 **Atestado Médico / Medical Certificate** - Para passes com necessidades especiais

**Formatos aceites:** PDF, JPG, JPEG, PNG

---

## 🛠️ Tecnologias / Technologies

### Stack Atual / Current Stack

- **Backend:** Python 3.11 + Flask 2.3.3
- **Frontend:** HTML5 + CSS3 + JavaScript ES6+
- **Templating:** Jinja2 3.1.2
- **Containerização:** Docker + Docker Compose
- **Controlo de Versão:** Git + GitHub

### Bibliotecas Atuais / Current Libraries

```python
Flask==2.3.3          # Web framework
Jinja2==3.1.2         # Template engine
Werkzeug==2.3.7       # WSGI utilities
Pillow==10.0.1        # Image processing (preparado para OCR)
python-dotenv==1.0.0  # Environment variables
```

### Tecnologias Planeadas / Planned Technologies

**IA e Processamento de Imagem / AI and Image Processing:**
- pytesseract - OCR para extração de texto
- OpenCV - Processamento de imagem
- TensorFlow/PyTorch - Modelos de validação

**Base de Dados / Database:**
- PostgreSQL 15+ - Base de dados relacional
- SQLAlchemy - ORM Python
- Alembic - Database migrations

**Autenticação e Segurança / Authentication and Security:**
- Flask-Login - Session management
- bcrypt - Password hashing
- PyJWT - JSON Web Tokens
- Flask-CORS - Cross-origin requests

**Notificações / Notifications:**
- Flask-Mail - Email sending
- Celery - Task queue
- Redis - Message broker

### Software Necessário / Required Software

- Docker Desktop (inclui Docker Compose)
- Git (opcional, para clonar repositório)
- Navegador Web moderno (Chrome, Firefox, Safari, Edge)

## 🚀 Complete Setup Guide

### Step 1: Install Docker Desktop

#### Windows 11/10:
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Run the installer as Administrator
3. Follow installation wizard (enable WSL 2 if prompted)
4. Restart your computer
5. Launch Docker Desktop and wait for it to start
6. Verify installation:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux (Ubuntu/Debian):
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER

# Logout and login again
```

### Step 2: Get the Project

#### Option A: Clone with Git
```bash
git clone https://github.com/your-username/CarrisPlus-GP.git
cd CarrisPlus-GP
```

#### Option B: Download ZIP
1. Download project ZIP file
2. Extract to desired location
3. Open terminal in project folder

### Step 3: Run the Application

#### First Time Setup:
```bash
# Navigate to project directory
cd CarrisPlus-GP

# Build and start containers
docker-compose up --build

# Wait for "Running on http://0.0.0.0:5000" message
```

#### Subsequent Runs:
```bash
# Start existing containers
docker-compose up

# Or run in background
docker-compose up -d
```

### Step 4: Access the Application

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. You should see the CarrisPlus homepage

## 🔧 Development Commands

```bash
# View running containers
docker ps

# View application logs
docker-compose logs web

# Stop the application
docker-compose down

# Rebuild after code changes
docker-compose up --build

# Enter container for debugging
docker exec -it carrisplus-gp-web-1 bash

# Install additional Python packages
docker exec -it carrisplus-gp-web-1 pip install package-name
```

## 📁 Project Structure

```
CarrisPlus-GP/
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Python dependencies
├── 🐳 Dockerfile            # Container configuration
├── 🐳 docker-compose.yml    # Multi-container setup
├── 📄 .dockerignore         # Docker build exclusions
├── 📁 templates/            # HTML templates
│   ├── base.html           # Base template
│   └── index.html          # Homepage
├── 📁 static/              # Static assets
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
└── 📁 uploads/             # Document storage
```

## 👥 Team Development Workflow

### For Each Team Member:

1. **Initial Setup:**
   ```bash
   git clone <repository-url>
   cd CarrisPlus-GP
   docker-compose up --build
   ```

2. **Daily Development:**
   ```bash
   git pull origin main
   docker-compose up
   # Make your changes
   git add .
   git commit -m "Your changes"
   git push origin your-branch
   ```

3. **Adding New Dependencies:**
   ```bash
   # Add to requirements.txt
   echo "new-package==1.0.0" >> requirements.txt
   
   # Rebuild container
   docker-compose up --build
   ```

## 🐛 Troubleshooting

### Common Issues:

**Docker not starting:**
- Ensure Docker Desktop is running
- Check system tray for Docker whale icon
- Restart Docker Desktop if needed

**Port 5000 already in use:**
```bash
# Kill process using port 5000
sudo lsof -ti:5000 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "8000:5000"  # Use port 8000 instead
```

**Permission errors on Windows:**
- Run terminal as Administrator
- Or use WSL2 terminal instead

**Container build fails:**
```bash
# Clean Docker cache
docker system prune -a

# Rebuild from scratch
docker-compose build --no-cache
```

---

## 🏗️ Arquitetura do Sistema / System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        UTILIZADOR / USER                     │
│                     (Browser Interface)                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   CAMADA DE APRESENTAÇÃO                     │
│                    PRESENTATION LAYER                        │
├─────────────────────────────────────────────────────────────┤
│  HTML5 + CSS3 + JavaScript  │  Jinja2 Templates             │
│  Responsive Design          │  Form Validation              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE APLICAÇÃO                       │
│                    APPLICATION LAYER                         │
├─────────────────────────────────────────────────────────────┤
│  Flask Routes           │  Business Logic                    │
│  Authentication [TODO]  │  Document Processing               │
│  Session Management     │  Validation Rules [TODO]           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE VALIDAÇÃO IA                    │
│                    AI VALIDATION LAYER [TODO]                │
├─────────────────────────────────────────────────────────────┤
│  OCR Engine             │  Name Matching                     │
│  NIF Validation         │  Document Authentication           │
│  Data Extraction        │  Fraud Detection                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                      CAMADA DE DADOS                         │
│                       DATA LAYER [TODO]                      │
├─────────────────────────────────────────────────────────────┤
│  PostgreSQL             │  File Storage                      │
│  SQLAlchemy ORM         │  Document Archive                  │
│  User Management        │  Audit Logs                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Fluxo de Trabalho / Workflow

### Submissão de Documentos / Document Submission Flow

```
1. Utilizador faz upload → 2. Validação de formato → 3. Extração OCR [TODO]
                                                              ↓
8. Notificação email ← 7. Armazenamento BD ← 4. Validação IA [TODO]
                                                              ↓
                                              5. Verificação NIF vs. BD [TODO]
                                                              ↓
                                              6. Aprovação/Rejeição [TODO]
```

---

## 📊 Estado de Desenvolvimento / Development Status

| Funcionalidade | Status | Progresso |
|----------------|--------|-----------|
| Interface Web | ✅ Completo | 100% |
| Upload de Documentos | ✅ Funcional | 100% |
| Sistema de Rotas | ✅ Completo | 100% |
| Docker Setup | ✅ Completo | 100% |
| Base de Dados | 🚧 Planeado | 0% |
| Autenticação | 🚧 Planeado | 0% |
| Validação IA/OCR | 🚧 Planeado | 0% |
| Painel Admin | 🚧 Planeado | 0% |
| Sistema de Email | 🚧 Planeado | 0% |
| API REST | 🚧 Planeado | 0% |

**Progresso Global: ~25%**

---

## 🎯 Roadmap de Desenvolvimento / Development Roadmap

### Fase 1: Fundação (Atual) ✅
- [x] Setup inicial do projeto
- [x] Containerização Docker
- [x] Interface básica
- [x] Upload de ficheiros

### Fase 2: Backend Core (Próximo)
- [ ] Integração PostgreSQL
- [ ] Autenticação de utilizadores
- [ ] Templates em falta (renew_document.html, create_pass.html)
- [ ] Correção de base.html

### Fase 3: Validação Inteligente
- [ ] Setup OCR (pytesseract)
- [ ] Extração de dados de documentos
- [ ] Validação de NIF
- [ ] Matching de nomes

### Fase 4: Funcionalidades Avançadas
- [ ] Painel de administração
- [ ] Sistema de notificações
- [ ] Gestão de passes completa
- [ ] Relatórios e estatísticas

### Fase 5: Produção
- [ ] Testes automatizados
- [ ] Segurança reforçada
- [ ] Performance optimization
- [ ] Deployment em produção

---

## 📞 Suporte / Support

Para questões ou problemas:
1. Consulte a secção de troubleshooting acima
2. Reveja a documentação do Docker Desktop
3. Contacte os membros da equipa

For issues or questions:
1. Check the troubleshooting section above
2. Review Docker Desktop documentation
3. Contact team members for assistance

---

## 📝 Licença / License

Projeto académico desenvolvido no âmbito do curso de Engenharia Informática.

Academic project developed as part of the Computer Engineering course.

---

## 🙏 Agradecimentos / Acknowledgments

- **Carris** - Pela inspiração do caso de uso
- **Flask Community** - Pela excelente documentação
- **Open Source Contributors** - Pelas ferramentas utilizadas

---

**Desenvolvido com dedicação pela equipa CarrisPlus**
**Developed with dedication by the CarrisPlus team**

**🚌 Tornando o transporte público mais acessível, um documento de cada vez**
**🚌 Making public transportation more accessible, one document at a time**