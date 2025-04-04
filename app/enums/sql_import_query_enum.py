from enum import Enum

class SqlImportQueryEnum(str, Enum):
    DEMONSTRATIVOS = "import_demonstrativos"
    OPERADORAS = "import_operadoras"