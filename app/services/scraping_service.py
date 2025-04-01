import os
import requests
from bs4 import BeautifulSoup
from app.core.zip_utils import zip_files

def download_and_zip_attachments():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a', href=True)

    os.makedirs("data", exist_ok=True)
    files = []

    for link in links:
        href = link['href']
        text = link.get_text(strip=True)

        if ("Anexo I" in text and href.endswith(".pdf")) or ("Anexo II" in text and href.endswith(".pdf")):
            final_url = href if href.startswith("http") else f"https://www.gov.br{href}"
            filename = final_url.split("/")[-1]
            path = f"data/{filename}"
            try:
                with requests.get(final_url, stream=True) as r:
                    with open(path, 'wb') as f:
                        f.write(r.content)
                files.append(path)
            except Exception:
                pass

    if not files:
        return None

    zip_path = "data/anexos_ans.zip"
    zip_files(files, zip_path)
    return os.path.abspath(zip_path)
