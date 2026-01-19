# CarrisPlus - Sistema de Autenticação e Gestão de Passes

Plataforma web para digitalizar submissão de documentos e gestão de passes da Carris com validação automática por IA.

**Projeto Académico - Desenvolvimento de Software B | Ano Letivo 2024/2025**

**Equipa:** Davi (2024301), Iago (2024195), Ana (2024184)

---

## 🚀 Demo Online

**Frontend:** [Adicionar URL após deploy]
**API Docs:** [Adicionar URL após deploy]

---

## ✨ Funcionalidades Implementadas

### Autenticação (RF-001)
- ✅ Registo de utilizadores com validação
- ✅ Login seguro com JWT tokens
- ✅ Proteção contra brute force (5 tentativas)
- ✅ Validação de NIF português
- ✅ Recuperação de password
- ✅ Dashboard protegido

### Segurança (RNF-002)
- ✅ Password hashing com bcrypt
- ✅ JWT tokens com expiração 24h
- ✅ Proteção SQL Injection
- ✅ Proteção XSS/CSRF
- ✅ Rate limiting
- ✅ Logs de auditoria
- ✅ Conformidade RGPD

---

## 🛠️ Tecnologias

### Backend
- Python 3.11
- Flask 2.3.3
- MySQL
- bcrypt
- PyJWT

### Frontend
- React 18
- Redux Toolkit
- React Router
- Axios

### DevOps
- Docker
- Docker Compose
- Git

---

## 🏃 Quick Start Local

### Pré-requisitos
- Docker Desktop

### Executar

```bash
# Clonar repositório
git clone [url-do-repo]
cd CarrisPlus-GP

# Iniciar todos os serviços
docker-compose up --build

# Aceder aplicação
# Frontend: http://localhost:3000
# Backend: http://localhost:5000
# phpMyAdmin: http://localhost:8080
```

---

## 📚 Documentação

- [Guia de Início Rápido](QUICKSTART.md)
- [Documentação Docker](README_DOCKER.md)
- [Guia de Deploy](DEPLOY_GUIDE.md)
- [Modelação do Projeto](Modelacao_CarrisPlus.pdf)

---

## 🎯 Próximas Funcionalidades

- [ ] Upload de documentos (RF-002)
- [ ] Validação automática com OCR/IA (RF-002)
- [ ] Gestão de passes (RF-003)
- [ ] Painel de administração (RF-004)
- [ ] Notificações por email (RF-005)

---

## 📊 Arquitetura

```
CarrisPlus/
├── backend/          # API Flask
│   ├── auth/        # Autenticação
│   ├── models/      # Modelos de dados
│   └── config/      # Configurações
├── frontend/        # React App
│   ├── components/  # Componentes React
│   ├── store/       # Redux store
│   └── services/    # API services
└── docker-compose.yml
```

---

## 🔐 Variáveis de Ambiente

### Backend
```env
FLASK_ENV=development
JWT_SECRET_KEY=your-secret-key
DATABASE_URL=mysql://user:pass@host:port/db
```

### Frontend
```env
REACT_APP_API_URL=http://localhost:5000
```

---

## 🧪 API Endpoints

### Autenticação
```
POST /api/auth/register - Registar utilizador
POST /api/auth/login    - Login
GET  /api/auth/me       - Utilizador atual
POST /api/auth/logout   - Logout
```

### Health Check
```
GET /health - Status do serviço
```

---

## 👥 Contribuidores

- Davi (2024301) - Full Stack Developer
- Iago (2024195) - Backend Developer
- Ana (2024184) - Frontend Developer

---

## 📄 Licença

Projeto académico - Todos os direitos reservados

---

## 📞 Suporte

Para questões sobre o projeto, contactar a equipa através do repositório GitHub.
