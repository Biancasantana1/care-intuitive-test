from enum import Enum

class SqlSelectQueryNameEnum(str, Enum):
    TOP10_DESPESAS_ANO = "top10_despesas_ano"
    TOP10_DESPESAS_TRIMESTRE = "top10_despesas_trimestre"