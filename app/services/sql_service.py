from pathlib import Path
from app.core.sql_runner import run_sql_file, run_select_sql_file
import logging

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

SQL_BASE_PATH = PROJECT_ROOT / "sql"
DATA_FOLDER = PROJECT_ROOT / "data"

logging.basicConfig(level=logging.DEBUG)

def list_available_queries():
    """
    Varre recursivamente a pasta SQL_BASE_PATH e retorna uma lista com as queries disponíveis.
    Cada item é um dicionário com:
      - category: nome da subpasta onde a query está.
      - name: nome do arquivo SQL (sem extensão).
      - path: caminho relativo à pasta 'sql'.
    """
    queries = list(SQL_BASE_PATH.rglob("*.sql"))
    return [
        {
            "category": q.parent.name,
            "name": q.stem,
            "path": str(q.relative_to(SQL_BASE_PATH))
        }
        for q in queries
    ]

def get_query_contents(query_name: str, inline: bool = True) -> str | None:
    """
    Lê e retorna o conteúdo de uma query SQL com base no seu nome (sem extensão).
    Se inline for True, remove as quebras de linha e espaços extras para retornar uma única linha.
    Retorna None se o arquivo não for encontrado.
    """
    query_path = find_query_path(query_name)
    if query_path and query_path.exists():
        content = query_path.read_text(encoding="utf-8")
        if inline:
            content = " ".join(line.strip() for line in content.splitlines())
        return content
    return None

def execute_query_by_name(query_name: str, descricao: str = None):
    """
    Executa uma query SQL identificada pelo nome do arquivo (sem extensão).
    Realiza a substituição do marcador ':descricao' se for informado.
    Retorna um dicionário com o nome da query e o resultado.
    """
    query_path = find_query_path(query_name)
    if not query_path or not query_path.exists():
        return {"error": "Query não encontrada"}

    result = run_sql_file(str(query_path))
    return {"query": query_name, "result": result}

def find_query_path(query_name: str) -> Path | None:
    """
    Procura recursivamente por um arquivo .sql cujo nome (sem extensão) seja igual a query_name.
    Retorna o Path se encontrado ou None caso contrário.
    """
    for sql_file in SQL_BASE_PATH.rglob("*.sql"):
        if sql_file.stem == query_name:
            return sql_file
    return None


def execute_select_query_by_name(query_name: str, replacements: dict = None) -> dict:
    """
    Executa uma query SELECT SQL identificada pelo nome do arquivo (sem extensão).
    Realiza a substituição dos tokens conforme o dicionário replacements.
    Retorna um dicionário com o nome da query e o resultado.
    """
    query_path = find_query_path(query_name)
    if not query_path or not query_path.exists():
        return {"error": "Query não encontrada"}

    sql = Path(query_path).read_text(encoding='utf-8')
    if replacements:
        for key, value in replacements.items():
            if value is None:
                sql = sql.replace(key, "NULL")
            else:
                sql = sql.replace(key, f"'{value}'")

    result = run_select_sql_file(sql)
    return {"query": query_name, "result": result}

def run_import_files(folder_name: str, sql_script: str) -> list[dict]:
    try:
        csv_folder = DATA_FOLDER / folder_name

        if not csv_folder.exists() or not csv_folder.is_dir():
            return [{"error": f"Pasta '{csv_folder}' não encontrada ou inválida."}]

        query_path = find_query_path(sql_script)
        if not query_path:
            return [{"error": f"Script SQL '{sql_script}.sql' não encontrado."}]

        results = []
        for csv_file in csv_folder.glob("*.csv"):
            full_path = f"/var/lib/mysql-files/{folder_name}/{csv_file.name}"
            replacements = {":full_path": full_path}
            res = run_sql_file(str(query_path), replacements=replacements)
            logging.debug(f"Retorno do run_sql_file para {csv_file.name}: {res}")
            results.append({
                "file": csv_file.name,
                "status": "OK" if not (isinstance(res, dict) and "error" in res) else "ERROR",
                "details": res
            })

        return results

    except Exception as e:
        error_msg = f"Erro na execução de run_import_files: {str(e)}"
        logging.error(error_msg)
        return [{"error": error_msg}]


