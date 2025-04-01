from fastapi import APIRouter, Query
from ..services.operator_service import search_operators

router = APIRouter(prefix="/operadoras", tags=["Operadoras"])

@router.get("/buscar")
def search(query: str = Query(..., description="Texto a ser buscado na razão social")):
    return search_operators(query)
