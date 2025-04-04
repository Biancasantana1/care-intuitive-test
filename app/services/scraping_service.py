import os
import requests
from bs4 import BeautifulSoup
from app.core.zip_utils import zip_files


def download_and_zip_attachments():
    """
    Realiza o scraping da página da ANS, baixa os PDFs dos anexos "Anexo I" e "Anexo II"
    e gera um arquivo ZIP contendo os documentos localmente.

    - Acessa a URL oficial da ANS via HTTP.
    - Identifica links para os PDFs "Anexo I" e "Anexo II".
    - Baixa os arquivos e os salva na pasta `data/scraping`.
    - Gera um arquivo `anexos_ans.zip` com os PDFs baixados.

    Retorna o caminho absoluto do arquivo ZIP gerado, ou `None` se nenhum anexo for encontrado.
    """
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a', href=True)

    os.makedirs("data/scraping", exist_ok=True)
    files = []

    for link in links:
        href = link['href']
        text = link.get_text(strip=True)

        if ("Anexo I" in text and href.endswith(".pdf")) or ("Anexo II" in text and href.endswith(".pdf")):
            final_url = href if href.startswith("http") else f"https://www.gov.br{href}"
            filename = final_url.split("/")[-1]
            path = f"data/scraping/{filename}"
            try:
                with requests.get(final_url, stream=True) as r:
                    with open(path, 'wb') as f:
                        f.write(r.content)
                files.append(path)
            except Exception:
                pass

    if not files:
        return None

    zip_path = "data/scraping/anexos_ans.zip"
    zip_files(files, zip_path)
    return os.path.abspath(zip_path)
