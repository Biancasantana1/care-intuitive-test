from fastapi import FastAPI
from app.api import scraping_routes, transform_routes, operator_routes, sql_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ANS Nivelamento API", version="1.0")

app.include_router(scraping_routes.router)
app.include_router(transform_routes.router)
app.include_router(operator_routes.router)
app.include_router(sql_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
