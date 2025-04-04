import os
import csv

def fix_text(text):
    """
    Corrige possíveis problemas de codificação em textos com encoding Latin1.

    - Tenta decodificar o texto de 'latin1' para 'utf-8'.
    - Remove espaços em branco antes/depois.
    - Retorna o texto original em caso de erro na conversão.
    """
    try:
        return text.encode('latin1').decode('utf-8').strip()
    except Exception:
        return text.strip()


def load_operators(path=None):
    """
    Carrega os dados das operadoras a partir de um arquivo CSV da ANS.

    - Se nenhum caminho for informado, usa o CSV padrão em `data/operadores_csv/Relatorio_cadop.csv`.
    - Realiza a correção de acentuação/codificação em cada campo.
    - Retorna uma lista de dicionários contendo dados padronizados das operadoras.
    """
    if path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(os.path.join(current_dir, '..', '..', 'data', 'operadores_csv', 'Relatorio_cadop.csv'))

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
    """
    Realiza uma busca textual por razão social no cache de operadoras.

    - A busca é case-insensitive e ignora acentuação.
    - Retorna todas as operadoras cuja razão social contém o texto pesquisado.
    """
    query = query.lower()
    return [op for op in OPERATORS_CACHE if query in op["razao_social"].lower()]
