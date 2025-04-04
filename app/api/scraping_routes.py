from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.scraping_service import download_and_zip_attachments

router = APIRouter(prefix="/scraping", tags=["Web Scraping"])

@router.get("/baixar-anexos", response_description="Baixa os anexos e retorna um arquivo ZIP")
async def download_attachments():
    """
    Realiza o download dos anexos "Anexo I" e "Anexo II" do site da ANS,
    salva localmente e retorna um arquivo ZIP contendo ambos.
    """
    zip_path = download_and_zip_attachments()
    return FileResponse(path=zip_path, filename=zip_path.split("/")[-1], media_type='application/zip')
