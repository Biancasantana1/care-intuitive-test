from fastapi import APIRouter, Query
from ..services.operator_service import search_operators

router = APIRouter(prefix="/operadoras", tags=["Operadoras"])


@router.get("/buscar")
def search(query: str = Query(..., description="Texto a ser buscado na razão social")):
    """
    Busca textual por operadoras da ANS com base na razão social.
    - `query`: termo a ser buscado (case-insensitive, com correção de acentuação)
    """
    return search_operators(query)
