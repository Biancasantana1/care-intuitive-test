# care-intuitive-test
# ANS API - FastAPI

API desenvolvida em FastAPI como parte de um desafio técnico, composta por três funcionalidades principais:

## Funcionalidades

### 1. Web Scraping de PDFs
- Acessa a [página oficial da ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Baixa os arquivos **Anexo I** e **Anexo II** em formato PDF
- Compacta os dois em um arquivo ZIP

### 2. Extração e Transformação de Dados
- Extrai todas as tabelas do **Anexo I (PDF)**
- Converte para um arquivo CSV estruturado
- Substitui siglas `OD` e `AMB` pelas descrições completas
- Compacta o CSV gerado em um `.zip` com nome `Teste_<seu_nome>.zip`

### 3. Busca de Operadoras
- Carrega um CSV com operadoras ativas da ANS
- Permite busca textual por razão social
- Corrige a acentuação dos dados via decodificação Latin1

## 🚀 Como executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
