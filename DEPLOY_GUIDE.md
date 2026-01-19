# 🚀 Guia de Deploy - CarrisPlus

## Opção 1: Railway.app (MAIS FÁCIL E RÁPIDO) ⭐

### Passo 1: Preparar o Código

1. **Fazer commit das alterações:**
```bash
git add .
git commit -m "Add authentication system"
git push origin main
```

### Passo 2: Criar Conta no Railway

1. Vai a: https://railway.app
2. Clica em "Start a New Project"
3. Faz login com GitHub
4. Autoriza o Railway a aceder aos teus repositórios

### Passo 3: Deploy do Backend

1. No Railway, clica em "New Project"
2. Seleciona "Deploy from GitHub repo"
3. Escolhe o repositório `CarrisPlus-GP`
4. Railway vai detetar automaticamente que é um projeto Python/Flask

**Configurar Variáveis de Ambiente:**

Clica no serviço criado e vai a "Variables":

```
FLASK_APP=backend/app.py
FLASK_ENV=production
JWT_SECRET_KEY=seu-secret-key-super-secreto-aqui
DATABASE_URL=(Railway vai gerar automaticamente)
```

### Passo 4: Adicionar MySQL Database

1. No mesmo projeto, clica em "+ New"
2. Seleciona "Database" → "Add MySQL"
3. Railway vai criar a base de dados automaticamente
4. Conecta o backend à database (Railway faz isso automaticamente!)

### Passo 5: Deploy do Frontend

1. No mesmo projeto, clica em "+ New"
2. Seleciona "GitHub Repo" → Escolhe o mesmo repo
3. Configura para usar a pasta `frontend`

**Variáveis de Ambiente do Frontend:**
```
REACT_APP_API_URL=https://seu-backend.railway.app
```

### Passo 6: Testar

1. Railway vai gerar URLs automáticos:
   - Backend: `https://carrisplus-backend.railway.app`
   - Frontend: `https://carrisplus-frontend.railway.app`

2. Abre o frontend e testa!

---

## Opção 2: Render.com (TAMBÉM GRÁTIS)

### Passo 1: Criar Conta

1. Vai a: https://render.com
2. Faz signup com GitHub

### Passo 2: Deploy Backend

1. Clica em "New +"
2. Seleciona "Web Service"
3. Conecta o teu repositório GitHub
4. Configuração:
   - **Name:** carrisplus-backend
   - **Root Directory:** `backend`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

**Variáveis de Ambiente:**
```
FLASK_APP=app.py
FLASK_ENV=production
JWT_SECRET_KEY=seu-secret-key-aqui
DATABASE_URL=(Render vai gerar)
```

### Passo 3: Adicionar PostgreSQL

1. Clica em "New +"
2. Seleciona "PostgreSQL"
3. Nome: carrisplus-db
4. Copia a "Internal Database URL"
5. Adiciona ao backend nas variáveis de ambiente

**IMPORTANTE:** Vais ter que mudar de MySQL para PostgreSQL. É super fácil:

No `backend/requirements.txt`, muda:
```
PyMySQL==1.1.0
```

Para:
```
psycopg2-binary==2.9.9
```

No `backend/config/database.py`, muda a conexão.

### Passo 4: Deploy Frontend

1. Clica em "New +"
2. Seleciona "Static Site"
3. Conecta o repositório
4. Configuração:
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `build`

**Variável de Ambiente:**
```
REACT_APP_API_URL=https://carrisplus-backend.onrender.com
```

---

## Opção 3: Vercel (Frontend) + Render (Backend)

### Frontend no Vercel (SUPER RÁPIDO):

1. Vai a: https://vercel.com
2. Faz login com GitHub
3. Importa o repositório
4. Configura:
   - **Framework:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `build`

**Variável de Ambiente:**
```
REACT_APP_API_URL=https://seu-backend.onrender.com
```

---

## 🎯 Recomendação Final:

Para apresentação ao professor, usa:

### **Railway.app**
**Porquê?**
- ✅ Mais fácil de configurar
- ✅ Suporta MySQL nativamente
- ✅ Deploy automático do GitHub
- ✅ URL bonito
- ✅ Não adormece tanto quanto Render
- ✅ $5 grátis por mês (suficiente para apresentação)

---

## 📝 Checklist Antes de Deploy:

- [ ] Código no GitHub
- [ ] Testar localmente (já fizeste!)
- [ ] Mudar `FLASK_ENV=production`
- [ ] Mudar `JWT_SECRET_KEY` para algo seguro
- [ ] Testar no Railway/Render
- [ ] Partilhar URL com o professor

---

## 🔗 URLs que vais precisar partilhar:

Depois do deploy, vais ter algo tipo:

- **Frontend:** https://carrisplus.railway.app
- **Backend API:** https://carrisplus-api.railway.app

Envia o link do **Frontend** ao professor!

---

## ⚡ Deploy Rápido (5 minutos):

```bash
# 1. Commit tudo
git add .
git commit -m "Ready for deploy"
git push

# 2. Vai a railway.app
# 3. New Project → Deploy from GitHub
# 4. Seleciona CarrisPlus-GP
# 5. Adiciona MySQL database
# 6. Deploy frontend também
# 7. Partilha o link!
```

---

## 💰 Custos:

- **Railway:** $5 grátis/mês (suficiente para 1-2 semanas de apresentação)
- **Render:** Grátis para sempre (mas adormece após 15 min)
- **Vercel:** Grátis ilimitado (só frontend)

**Recomendação:** Usa Railway para a apresentação, é mais profissional!

---

Quer que te ajude a fazer o deploy no Railway agora? 🚀
