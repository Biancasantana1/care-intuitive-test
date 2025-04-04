from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.enums.sql_create_table_query_enum import SqlCreateTableQueryEnum
from app.enums.sql_csv_folder_name_enum import SqlCsvFolderNameEnum
from app.enums.sql_query_identifier_enum import SqlQueryIdentifierEnum
from app.enums.sql_select_query_name_enum import SqlSelectQueryNameEnum
from app.enums.sql_import_query_enum import SqlImportQueryEnum
from app.enums.sql_trimestre_enum import SqlTrimestreEnum
from app.services.sql_service import (
    list_available_queries,
    get_query_contents,
    execute_query_by_name,
    run_import_files,
    execute_select_query_by_name
)

router = APIRouter(prefix="/sql", tags=["SQL Scripts"])


@router.get("/queries", summary="Listar todas as queries disponíveis")
def list_queries():
    """
    Retorna a lista de arquivos de query SQL disponíveis no diretório de scripts.
    """
    return list_available_queries()


@router.get("/show/{query_name}", summary="Exibir conteúdo da query SQL")
def show_query(query_name: SqlQueryIdentifierEnum):
    """
    Retorna o conteúdo de uma query SQL específica.
    - `query_name`: nome do arquivo SQL sem extensão.
    """
    content = get_query_contents(query_name.value, inline=True)
    if not content:
        raise HTTPException(status_code=404, detail="Query não encontrada")
    return {"query_name": query_name.value, "sql": content}


@router.post("/run/{query_name}", summary="Criar Tabelas no banco de dados")
def run_query(query_name: SqlCreateTableQueryEnum):
    """
    Executa uma query SQL de criação de tabela no banco de dados.
    - `query_name`: identificador da query de criação.
    """
    result = execute_query_by_name(query_name.value)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.post("/{folder_name}/{sql_name}", summary="Importar arquivos CSV para o banco de dados")
def import_csv_data(folder_name: SqlCsvFolderNameEnum, sql_name: SqlImportQueryEnum):
    """
    Realiza a importação de arquivos CSV para o banco de dados com base em scripts SQL definidos.
    - `folder_name`: nome da pasta onde os CSVs estão localizados.
    - `sql_name`: nome do script SQL de importação.
    """
    results = run_import_files(folder_name.value, sql_name.value)
    return {"import_results": results}


@router.get("/run/{query_name}", summary="Executar uma query SELECT SQL")
def run_select_query(
    query_name: SqlSelectQueryNameEnum,
    ano: int,
    descricao: Optional[str] = None,
    trimestre: Optional[SqlTrimestreEnum] = Query(
        None,
        description="Trimestre (apenas para consulta trimestral; valores: 1,2,3,4)"
    )
):
    """
    Executa uma query SQL do tipo SELECT parametrizada.
    - `query_name`: nome da query SELECT disponível
    - `ano`: ano a ser aplicado como filtro
    - `descricao`: descrição textual para filtro por prestador ou operadora (opcional)
    - `trimestre`: obrigatório somente para consultas trimestrais
    """
    replacements = {
        ":descricao": descricao or None,
        ":ano": str(ano)
    }

    if query_name == SqlSelectQueryNameEnum.TOP10_DESPESAS_TRIMESTRE:
        if trimestre is None:
            raise HTTPException(
                status_code=400,
                detail="O parâmetro 'trimestre' é obrigatório para a consulta trimestral."
            )
        replacements[":trimestre"] = str(trimestre.value)

    result = execute_select_query_by_name(query_name.value, replacements=replacements)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
