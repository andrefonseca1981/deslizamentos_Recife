# 🚀 GUIA RÁPIDO: Deploy no Streamlit Cloud

## ⚡ Resumo: 5 Passos Simples

1. Criar conta no GitHub
2. Criar repositório
3. Upload dos 3 arquivos
4. Conectar no Streamlit Cloud
5. Deploy automático!

---

## 📝 PASSO A PASSO DETALHADO

### PASSO 1: GitHub - Criar Conta (2 minutos)

1. Acesse: https://github.com
2. Clique em "Sign up" (canto superior direito)
3. Preencha:
   - Email
   - Senha
   - Username (ex: andre_doutorado)
4. Verifique seu email
5. ✅ Conta criada!

---

### PASSO 2: Criar Repositório (2 minutos)

1. No GitHub, clique no ícone "+" → "New repository"
2. Preencha:
   - **Repository name:** `analise-deslizamentos-recife`
   - **Description:** "Sistema de análise de eventos de deslizamento"
   - **Marque:** ☑️ Public
   - **Marque:** ☑️ Add a README file
3. Clique em "Create repository"
4. ✅ Repositório criado!

---

### PASSO 3: Upload dos Arquivos (3 minutos)

1. No seu repositório, clique em "Add file" → "Upload files"
2. Arraste os 3 arquivos para a área de upload:
   - ✅ `streamlit_app.py`
   - ✅ `requirements.txt`
   - ✅ `README.md`
3. Na caixa "Commit changes", escreva: "Adicionar aplicação"
4. Clique em "Commit changes"
5. ✅ Arquivos enviados!

**IMPORTANTE:** Certifique-se que os arquivos estão na raiz do repositório, NÃO dentro de uma pasta!

---

### PASSO 4: Streamlit Cloud - Conectar (3 minutos)

1. Acesse: https://share.streamlit.io
2. Clique em "Sign in"
3. Escolha "Continue with GitHub"
4. Autorize o Streamlit a acessar sua conta
5. ✅ Conectado!

---

### PASSO 5: Deploy (5 minutos)

1. No Streamlit Cloud, clique em "New app"
2. Preencha:
   - **Repository:** `seu-usuario/analise-deslizamentos-recife`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
3. Clique em "Deploy!"
4. Aguarde 2-3 minutos (barra de progresso)
5. ✅ App no ar!

**Sua URL será algo como:**
`https://seu-usuario-analise-deslizamentos-recife.streamlit.app`

---

## 🎉 PRONTO! Agora você tem:

✅ App público na internet
✅ URL compartilhável
✅ Atualizações automáticas
✅ Hospedagem gratuita
✅ SSL/HTTPS incluído

---

## 🔄 Como Atualizar o App

1. No GitHub, clique no arquivo que quer editar
2. Clique no ícone de lápis (Edit)
3. Faça suas alterações
4. Clique em "Commit changes"
5. **O Streamlit atualiza AUTOMATICAMENTE em ~1 minuto!**

---

## 📱 Como Compartilhar

Basta enviar a URL para qualquer pessoa:
- Por email
- Por WhatsApp
- Em apresentações
- Em artigos

**Não precisa de login ou senha para usar!**

---

## 🆘 Problemas Comuns

### Problema: "File not found: streamlit_app.py"
**Solução:** Verifique se o arquivo está na raiz do repositório (não em subpasta)

### Problema: "ModuleNotFoundError"
**Solução:** Verifique se o `requirements.txt` está correto e na raiz

### Problema: App não inicia
**Solução:** 
1. Clique nos 3 pontinhos → "Reboot app"
2. Ou clique em "Manage app" → "Reboot"

### Problema: Deploy travou
**Solução:** Aguarde 5 minutos. Se persistir, delete o app e crie novamente.

---

## 💡 Dicas Profissionais

1. **URL Personalizada:** No Streamlit Cloud, você pode configurar um domínio customizado
2. **Senha:** Adicione autenticação em "Settings" → "Secrets"
3. **Analytics:** Streamlit Cloud fornece estatísticas de uso gratuitamente
4. **Logs:** Veja logs em tempo real clicando em "Manage app"
5. **Atualização:** Sempre que fizer commit no GitHub, app atualiza sozinho!

---

## 📊 Limites Gratuitos

**Streamlit Cloud Free:**
- ✅ 1 app público ilimitado
- ✅ Recursos: 1 CPU, 800 MB RAM
- ✅ Uptime: 24/7
- ✅ Bandwidth ilimitado
- ✅ SSL incluído

**Suficiente para:**
- ✅ Análises acadêmicas
- ✅ Protótipos
- ✅ Apresentações
- ✅ Compartilhamento com colaboradores

---

## 🎓 Próximos Passos

Depois do deploy, você pode:

1. **Testar:** Acesse sua URL e teste todas as funcionalidades
2. **Compartilhar:** Envie o link para orientadores/colaboradores
3. **Iterar:** Faça melhorias no código e commit no GitHub
4. **Apresentar:** Use em defesas, reuniões, artigos

---

## 📞 Links Úteis

- **Documentação Streamlit:** https://docs.streamlit.io
- **Galeria de Apps:** https://streamlit.io/gallery
- **Forum da Comunidade:** https://discuss.streamlit.io
- **Deploy Docs:** https://docs.streamlit.io/streamlit-community-cloud

---

**Feito com ❤️ para facilitar sua pesquisa!**

Qualquer dúvida, consulte o README.md ou a documentação do Streamlit.
