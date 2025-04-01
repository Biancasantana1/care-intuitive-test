# main.py
from fastapi import FastAPI
from app.api import scraping_routes, transform_routes, operator_routes
from fastapi.middleware.cors import CORSMiddleware

# Criação da instância da aplicação FastAPI
app = FastAPI(title="ANS Nivelamento API", version="1.0")

# Inclusão dos routers, permitindo a modularização das rotas em módulos separados
app.include_router(scraping_routes.router)
app.include_router(transform_routes.router)
app.include_router(operator_routes.router)

# Configuração do middleware CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bloco principal para execução da aplicação via uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
