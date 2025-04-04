from pydantic import BaseModel
from typing import Optional

from app.enums.trimestre_enum import TrimestreEnum


class QueryParams(BaseModel):
    data: int
    descricao: Optional[str] = None
    trimestre: Optional[TrimestreEnum] = None
