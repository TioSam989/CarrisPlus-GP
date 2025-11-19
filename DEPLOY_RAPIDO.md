# 🚀 Deploy Rápido - 5 Minutos

## Para hospedar GRÁTIS e partilhar com o professor:

### ⚡ Opção MAIS RÁPIDA: Railway.app

**1. Preparar (1 min):**
```bash
git add .
git commit -m "Ready for production"
git push
```

**2. Deploy (3 min):**

1. Vai a: **https://railway.app**
2. Clica "Start a New Project"
3. Login com GitHub
4. Seleciona "Deploy from GitHub repo"
5. Escolhe: **CarrisPlus-GP**
6. Railway faz deploy automático!

**3. Adicionar Base de Dados (1 min):**

1. No projeto Railway, clica "+ New"
2. Seleciona "Database" → "MySQL"
3. Pronto! Railway conecta automaticamente

**4. Partilhar com Professor:**

Railway vai gerar um URL tipo:
```
https://carrisplus-production.up.railway.app
```

**Copia esse URL e envia ao professor!**

---

## 🎯 Alternativa: Render.com (100% Grátis Sempre)

**Vantagem:** Grátis para sempre
**Desvantagem:** Adormece após 15 min (demora 30s a acordar)

### Passos:

1. Vai a: **https://render.com**
2. Signup com GitHub
3. "New +" → "Web Service"
4. Conecta repo CarrisPlus-GP
5. Configura:
   - Root: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
6. Deploy!

---

## 💡 Dica Pro:

**Para impressionar o professor:**

1. Deploy no Railway (mais rápido e profissional)
2. Cria 1-2 utilizadores de teste
3. Tira screenshots do sistema a funcionar
4. Partilha:
   - URL do site
   - Credenciais de teste
   - Screenshot do dashboard

**Exemplo de email:**

```
Olá Professor,

Aqui está o projeto CarrisPlus online:

URL: https://carrisplus.railway.app

Credenciais de teste:
Email: demo@carrisplus.com
Password: Demo1234

O sistema inclui:
- Registo e login seguro
- Validação de NIF português
- Proteção contra brute force
- Dashboard protegido
- Logs de auditoria

Cumprimentos,
[Teu nome]
```

---

## 📊 Custos:

- **Railway:** $5 grátis (dura 1-2 semanas)
- **Render:** Grátis para sempre
- **Vercel:** Grátis ilimitado (só frontend)

**Recomendação:** Railway para apresentação!

---

## ⏱️ Tempo Total: ~5 minutos

Quer ajuda para fazer o deploy AGORA? 🚀
