from pydantic import BaseModel
from typing import Optional

from app.enums.sql_trimestre_enum import SqlTrimestreEnum


class QueryParams(BaseModel):
    data: int
    descricao: Optional[str] = None
    trimestre: Optional[SqlTrimestreEnum] = None
