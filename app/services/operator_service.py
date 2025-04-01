import os
import csv

def fix_text(text):
    try:
        return text.encode('latin1').decode('utf-8').strip()
    except Exception:
        return text.strip()

def load_operators(path=None):
    if path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(os.path.join(current_dir, '..', '..', 'data', 'Relatorio_cadop.csv'))
    operators = []
    with open(path, encoding="latin1") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            operators.append({
                "registro_ans": fix_text(row["Registro_ANS"]),
                "razao_social": fix_text(row["Razao_Social"]),
                "nome_fantasia": fix_text(row["Nome_Fantasia"]),
                "modalidade": fix_text(row["Modalidade"]),
                "uf": fix_text(row["UF"]),
                "cidade": fix_text(row["Cidade"]),
            })
    return operators

OPERATORS_CACHE = load_operators()

def search_operators(query: str):
    query = query.lower()
    return [op for op in OPERATORS_CACHE if query in op["razao_social"].lower()]
