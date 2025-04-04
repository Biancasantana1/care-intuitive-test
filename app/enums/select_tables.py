from enum import Enum

class SelectQuery(str, Enum):
    top10_despesas_ano = "top10_despesas_ano"
    top10_despesas_trimestre = "top10_despesas_trimestre"
