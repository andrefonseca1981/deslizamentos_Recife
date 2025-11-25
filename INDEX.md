# 📦 Pacote Completo: Sistema Streamlit de Análise de Deslizamentos

## 📋 Conteúdo do Pacote

### 🔧 Arquivos Principais (Deploy)
1. **streamlit_app.py** (16 KB)
   - Código principal do aplicativo
   - Sistema completo de análise
   - Pronto para deploy!

2. **requirements.txt** (61 bytes)
   - Lista de dependências Python
   - Necessário para o Streamlit Cloud
   - Versões testadas e funcionando

3. **README.md** (6 KB)
   - Documentação completa
   - Instruções de instalação
   - Como usar o sistema

### 📚 Guias de Apoio
4. **QUICK_START.md** (2 KB)
   - ⚡ Comece em 10 minutos!
   - Método mais rápido
   - Passo a passo resumido

5. **GUIA_DEPLOY.md** (4 KB)
   - 🚀 Deploy detalhado
   - Screenshots textuais
   - Solução de problemas

6. **GUIA_VISUAL.md** (8 KB)
   - 🎨 Ilustrações do sistema
   - Comparações e fluxos
   - Dicas profissionais

---

## 🎯 Por Onde Começar?

### Se você quer...

**🏃 Ir RÁPIDO (10 min):**
→ Leia: `QUICK_START.md`
→ Faça: Upload no GitHub + Deploy

**📖 Entender TUDO (30 min):**
→ Leia: `README.md` completo
→ Depois: `GUIA_DEPLOY.md`

**🎨 Ver EXEMPLOS (15 min):**
→ Leia: `GUIA_VISUAL.md`
→ Entenda: Como funciona

**🔧 Testar LOCALMENTE:**
→ Leia: Seção "Instalação Local" do README
→ Execute: `streamlit run streamlit_app.py`

---

## 📊 Arquitetura do Sistema

```
┌─────────────────────────────────────────────┐
│           INTERFACE WEB (Streamlit)         │
├─────────────────────────────────────────────┤
│  Upload CSVs → Processamento → Visualização│
├─────────────────────────────────────────────┤
│  • 6 Eventos Pré-cadastrados                │
│  • Cálculo de Distâncias (Haversine)        │
│  • Agregação Horária (igual R)              │
│  • Gráficos Interativos (Plotly)            │
│  • Estatísticas em Tempo Real               │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Streamlit** | 1.29.0 | Framework web |
| **Pandas** | 2.1.4 | Processamento de dados |
| **Plotly** | 5.18.0 | Gráficos interativos |
| **NumPy** | 1.26.2 | Cálculos numéricos |
| **Python** | 3.8+ | Linguagem base |

---

## ✨ Funcionalidades Principais

### 📍 Eventos de Deslizamento (6)
1. Linha do Tiro (18/06/2021)
2. Brejo da Guabiraba (10/08/2021)
3. Alto Santa Terezinha (07/06/2022)
4. Vasco da Gama (02/08/2022)
5. Passarinho 1 (06/02/2023)
6. Passarinho 2 (06/02/2025)

### 📊 Análises Disponíveis
- ✅ Umidade do Solo (6 níveis de profundidade)
- ✅ Precipitação (horária e diária)
- ✅ Período D-2 até D0 (automático)
- ✅ Ranking de estações por proximidade
- ✅ Estatísticas completas
- ✅ Marcador do momento do evento

### 🎨 Visualizações
- ✅ Gráficos de linha interativos
- ✅ Gráficos de barras
- ✅ Hover tooltips
- ✅ Zoom e pan
- ✅ Download de imagens
- ✅ Linha vermelha no evento

---

## 🚀 Workflow Recomendado

### Primeira Vez:
1. Ler `QUICK_START.md` (5 min)
2. Criar conta GitHub (2 min)
3. Upload dos 3 arquivos principais (2 min)
4. Deploy no Streamlit Cloud (3 min)
5. **TOTAL: ~12 minutos** ⏱️

### Uso Diário:
1. Acessar sua URL
2. Upload dos CSVs necessários
3. Selecionar evento
4. Escolher estação
5. Analisar gráficos
6. **TOTAL: ~2 minutos por análise** ⚡

---

## 💡 Dicas Importantes

### ✅ FAÇA:
- Use a pasta inteira de CSVs (Ctrl+A)
- Salve a URL do seu app
- Teste localmente antes do deploy (opcional)
- Leia o README completo
- Compartilhe com orientadores

### ❌ NÃO FAÇA:
- Colocar arquivos em subpastas no GitHub
- Alterar nomes dos arquivos principais
- Esquecer de commitar mudanças
- Usar Python < 3.8
- Tentar fazer deploy sem requirements.txt

---

## 📞 Suporte

### Documentação Oficial:
- **Streamlit:** https://docs.streamlit.io
- **Pandas:** https://pandas.pydata.org/docs/
- **Plotly:** https://plotly.com/python/

### Comunidade:
- **Forum Streamlit:** https://discuss.streamlit.io
- **Stack Overflow:** Tag `streamlit`
- **GitHub Issues:** Para bugs específicos

### Troubleshooting:
1. Consultar seção "Problemas Comuns" no README
2. Verificar logs no Streamlit Cloud
3. Reboot do app
4. Recriar do zero (última opção)

---

## 🎓 Para Pesquisa Acadêmica

### Vantagens:
✅ **Reprodutível** - Código versionado
✅ **Compartilhável** - URL pública
✅ **Documentado** - README completo
✅ **Gratuito** - Sem custos
✅ **Profissional** - Interface moderna

### Como Citar:
```
Sistema de Análise de Eventos de Deslizamento
Desenvolvido em: 2025
Tecnologia: Python + Streamlit
Disponível em: [sua-url].streamlit.app
```

---

## 📈 Próximos Passos

### Imediato (Agora):
- [ ] Fazer deploy básico
- [ ] Testar com seus dados
- [ ] Compartilhar com 1 pessoa

### Curto Prazo (Esta Semana):
- [ ] Personalizar eventos
- [ ] Adicionar coordenadas reais das estações
- [ ] Criar análises específicas

### Médio Prazo (Este Mês):
- [ ] Adicionar mais visualizações
- [ ] Exportar relatórios
- [ ] Integrar com outros dados

### Longo Prazo (Doutorado):
- [ ] Machine Learning
- [ ] Predição de eventos
- [ ] Publicação científica

---

## 🏆 Checklist Final

Antes de começar, certifique-se:
- [ ] Python 3.8+ instalado (para teste local)
- [ ] Conta GitHub criada
- [ ] Todos os 3 arquivos principais baixados
- [ ] CSVs dos dados disponíveis
- [ ] Internet estável
- [ ] Navegador atualizado

---

## 🎉 Você Está Pronto!

**Tudo que você precisa está neste pacote.**

Escolha seu caminho:
- 🏃 Rápido? → QUICK_START.md
- 📖 Completo? → README.md
- 🎨 Visual? → GUIA_VISUAL.md

**Boa sorte com sua pesquisa de doutorado!** 🎓

---

*Última atualização: Novembro 2025*
*Desenvolvido especialmente para análise de deslizamentos em Recife/PE*
