# ⚠️ Sistema de Análise de Eventos de Deslizamento - Recife/PE

Sistema web interativo desenvolvido com Streamlit para análise de dados de umidade do solo e precipitação em eventos de deslizamento.

## 🎯 Funcionalidades

- ✅ Análise de 6 eventos de deslizamento pré-cadastrados
- ✅ Cálculo automático de distâncias entre eventos e estações (Haversine)
- ✅ Ranking de estações mais próximas
- ✅ Agregação horária estrita (igual ao código R)
- ✅ Visualização interativa de umidade do solo (6 níveis)
- ✅ Gráficos de precipitação (horária e diária)
- ✅ Marcador do momento exato do evento
- ✅ Estatísticas do período D-2 até D0
- ✅ Interface moderna e responsiva

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Instalação Local

### Passo 1: Baixar os arquivos

Baixe os seguintes arquivos:
- `streamlit_app.py`
- `requirements.txt`
- `README.md` (este arquivo)

### Passo 2: Criar ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o app

```bash
streamlit run streamlit_app.py
```

O app abrirá automaticamente no seu navegador em `http://localhost:8501`

## 🌐 Deploy no Streamlit Cloud (GRATUITO!)

### Passo 1: Criar conta no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em "Sign up" e crie sua conta

### Passo 2: Criar repositório

1. Clique em "New repository" (botão verde)
2. Nome: `analise-deslizamentos-recife`
3. Marque "Public"
4. Marque "Add a README file"
5. Clique em "Create repository"

### Passo 3: Fazer upload dos arquivos

1. No repositório criado, clique em "Add file" → "Upload files"
2. Arraste os 3 arquivos:
   - `streamlit_app.py`
   - `requirements.txt`
   - `README.md`
3. Clique em "Commit changes"

### Passo 4: Deploy no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Clique em "Sign in" e use sua conta do GitHub
3. Clique em "New app"
4. Selecione:
   - **Repository:** seu repositório (`analise-deslizamentos-recife`)
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
5. Clique em "Deploy!"

🎉 **Pronto!** Em 2-3 minutos seu app estará online com uma URL pública!

Exemplo: `https://seu-usuario-analise-deslizamentos-recife.streamlit.app`

## 📖 Como Usar

### 1. Upload de Dados
- Clique em "Browse files" na barra lateral
- Selecione **TODOS** os arquivos CSV da pasta `Recife_prec_umid_cemaden`
- Use Ctrl+A para selecionar todos de uma vez
- Aguarde o processamento

### 2. Selecionar Evento
Escolha um dos 6 eventos disponíveis:
- **Linha do Tiro** (18/06/2021)
- **Brejo da Guabiraba** (10/08/2021)
- **Alto Santa Terezinha** (07/06/2022)
- **Vasco da Gama** (02/08/2022)
- **Passarinho 1** (06/02/2023)
- **Passarinho 2** (06/02/2025)

### 3. Escolher Estação
- O sistema mostra o ranking das 10 estações mais próximas
- Selecione a estação desejada
- Os gráficos são atualizados automaticamente

### 4. Personalizar Visualização
- **Níveis de Profundidade:** Marque/desmarque os níveis 1-6
- **Visualização de Chuva:** Escolha entre "Horária" ou "Diária"

## 🔧 Arquivos do Projeto

```
projeto/
├── streamlit_app.py      # Código principal do app
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

## 📊 Dados de Entrada

O sistema espera arquivos CSV com as seguintes colunas:
- `datahora`: Data e hora da medição
- `sensor`: Tipo de sensor (umidade_solo_nivel1-6, chuva)
- `valorMedida`: Valor medido
- `nomeEstacao`: Nome da estação
- `codEstacao`: Código da estação

Formato: `recife_MM_YYYY.csv` (ex: `recife_06_2022.csv`)

## 🎨 Capturas de Tela

### Tela Principal
- Seleção de eventos em cards
- Ranking de estações por proximidade
- Informações do evento selecionado

### Gráficos
- **Umidade do Solo:** 6 níveis com cores diferentes
- **Precipitação:** Visualização horária (linha) ou diária (barras)
- **Linha Vermelha:** Marca o momento exato do evento

### Estatísticas
- Valores máximo, mínimo e médio
- Total de precipitação
- Número de registros válidos

## 🐛 Solução de Problemas

### Erro: "Module not found"
```bash
pip install --upgrade -r requirements.txt
```

### App não abre automaticamente
Acesse manualmente: `http://localhost:8501`

### Erro ao fazer upload
- Verifique se os arquivos são .csv
- Confirme que estão no formato correto (separador `;`)
- Tente fazer upload em lotes menores

### Deploy falhou
- Verifique se todos os 3 arquivos estão no repositório
- Confirme que o arquivo se chama exatamente `streamlit_app.py`
- Aguarde 5 minutos e tente novamente

## 💡 Dicas

1. **Upload Rápido:** Use Ctrl+A para selecionar todos os CSVs de uma vez
2. **Compartilhar:** A URL do Streamlit Cloud pode ser compartilhada com qualquer pessoa
3. **Atualizar Dados:** Basta fazer novo upload dos arquivos
4. **Performance:** O app processa apenas os dados necessários para o período D-2 até D0

## 📚 Tecnologias Utilizadas

- **Streamlit:** Framework para criar web apps em Python
- **Pandas:** Processamento e análise de dados
- **Plotly:** Gráficos interativos
- **NumPy:** Cálculos numéricos

## 🤝 Suporte

Para dúvidas ou problemas:
1. Verifique a seção "Solução de Problemas" acima
2. Confira a documentação do Streamlit: [docs.streamlit.io](https://docs.streamlit.io)
3. Consulte exemplos: [streamlit.io/gallery](https://streamlit.io/gallery)

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos - Doutorado em Ciências Climáticas.

## 🎓 Autor

Sistema desenvolvido para análise de eventos de deslizamento em Recife/PE como parte de pesquisa de doutorado.

---

**⚡ Desenvolvido com Streamlit - Deploy em minutos, análise poderosa!**
