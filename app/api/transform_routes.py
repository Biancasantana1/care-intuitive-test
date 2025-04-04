from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.transform_service import process_pdf_attachment

router = APIRouter(prefix="/transform", tags=["Transformação de Dados"])


@router.post("/extrair-csv", response_description="Gera e baixa o arquivo ZIP com o CSV extraído")
async def extract_csv_data():
    """
    Extrai as tabelas do PDF "Anexo I" da ANS, transforma os dados em um arquivo CSV estruturado,
    substitui siglas por descrições legíveis e retorna um arquivo ZIP com o CSV final.
    """
    zip_path = process_pdf_attachment()
    return FileResponse(path=zip_path, filename=zip_path.split("/")[-1], media_type='application/zip')
