from enum import Enum


class QueryName(str, Enum):
    top10_despesas_ano = "top10_despesas_ano"
    top10_despesas_trimestre = "top10_despesas_trimestre"
    create_demonstrativos_contabeis = "create_demonstrativos_contabeis"
    create_operadoras = "create_operadoras"
    import_demonstrativos = "import_demonstrativos"
    import_operadoras = "import_operadoras"
