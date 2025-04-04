from enum import Enum

class SqlQueryIdentifierEnum(str, Enum):
    TOP10_DESPESAS_ANO = "top10_despesas_ano"
    TOP10_DESPESAS_TRIMESTRE = "top10_despesas_trimestre"
    CREATE_DEMONSTRATIVOS_CONTABEIS = "create_demonstrativos_contabeis"
    CREATE_OPERADORAS = "create_operadoras"
    IMPORT_DEMONSTRATIVOS = "import_demonstrativos"
    IMPORT_OPERADORAS = "import_operadoras"