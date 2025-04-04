from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.enums.create_tables import TableCreationQuery
from app.enums.csv_folder_name import CsvFolderName
from app.enums.query_enum import QueryName
from app.enums.select_tables import SelectQuery
from app.enums.sql_import_name import SqlImportName
from app.enums.trimestre_enum import TrimestreEnum
from app.services.sql_service import (
    list_available_queries,
    get_query_contents,
    execute_query_by_name,
    run_import_files, execute_select_query_by_name
)

router = APIRouter(prefix="/sql", tags=["SQL Scripts"])


@router.get("/queries", summary="Listar todas as queries disponíveis")
def list_queries():
    return list_available_queries()


@router.get("/show/{query_name}", summary="Exibir conteúdo da query SQL")
def show_query(query_name: QueryName):
    content = get_query_contents(query_name.value, inline=True)
    if not content:
        raise HTTPException(status_code=404, detail="Query não encontrada")
    return {"query_name": query_name.value, "sql": content}


@router.post("/run/{query_name}", summary="Criar Tabelas no banco de dados")
def run_query(query_name: TableCreationQuery):
    result = execute_query_by_name(query_name.value)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.post("/{folder_name}/{sql_name}", summary="Importar arquivos CSV para o banco de dados")
def import_csv_data(folder_name: CsvFolderName, sql_name: SqlImportName):
    results = run_import_files(folder_name.value, sql_name.value)
    return {"import_results": results}


@router.get("/run/{query_name}", summary="Executar uma query SELECT SQL")
def run_select_query(
        query_name: SelectQuery,
        ano: int,
        descricao: Optional[str] = None,
        trimestre: Optional[TrimestreEnum] = Query(None,
                                                   description="Trimestre (apenas para consulta trimestral; valores: 1,2,3,4)")
):
    replacements = {
        ":descricao": descricao or None,
        ":ano": str(ano)
    }
    if query_name == SelectQuery.top10_despesas_trimestre:
        if trimestre is None:
            raise HTTPException(status_code=400,
                                detail="O parâmetro 'trimestre' é obrigatório para a consulta trimestral.")
        replacements[":trimestre"] = str(trimestre.value)

    result = execute_select_query_by_name(query_name.value, replacements=replacements)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
