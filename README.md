# care-intuitive-test - Backend (FastAPI)

API desenvolvida em **FastAPI**, estruturada em Clean Architecture e exposta via Swagger. A aplicação fornece scraping de dados públicos da ANS, transformação de PDF para CSV e manipulação dinâmica de queries SQL.
Banco de dados utilizado foi o MySQL 8.

---

## ⚙️ Funcionalidades da API

### 📥 Web Scraping

- **GET /scraping/baixar-anexos**  
  Baixa os arquivos PDF "Anexo I" e "Anexo II" da ANS e retorna compactado em `.zip`.

---

### 📊 Transformação de Dados

- **POST /transform/extrair-csv**  
  Extrai tabelas do PDF "Anexo I", converte para CSV, substitui siglas e retorna `.zip`.

---

### 🏥 Operadoras da ANS

- **GET /operadoras/buscar?query=**  
  Busca textual por nome/razão social em operadoras da ANS (arquivo CSV).  
  - Corrige encoding (`Latin1 → UTF-8`)
  - Usa `registro_ans` como chave
  - Ideal para autocomplete, filtro, etc.

---

### 🗃️ SQL Scripts
- Os scripts do SQL também estão disponiveis na pasta `sql`.

- **GET /sql/queries**  
  Lista todas as queries SQL disponíveis no diretório.

- **GET /sql/show/{query_name}**  
  Exibe o conteúdo de uma query SQL específica.

- **POST /sql/run/{query_name}**  
  Executa uma query SQL do tipo DDL (ex: criação de tabelas).

- **GET /sql/run/{query_name}**  
  Executa uma query SQL do tipo `SELECT` e retorna os dados como JSON.

- **POST /sql/{folder_name}/{sql_name}**  
  Permite importar arquivos `.csv` para o banco de dados via SQL (ex: `LOAD DATA INFILE`).

---

## 🐳 Execução com Docker

### Pré-requisitos

- Docker
- Docker Compose

### Passo a passo
- Acesse:` http://localhost:8000/docs` para visualizar a documentação interativa da API via Swagger.

```bash
docker-compose up --build
