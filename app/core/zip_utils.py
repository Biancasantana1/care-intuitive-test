import zipfile
import os

def zip_files(files: list, zip_name: str):
    """
    Compacta uma lista de arquivos em um único arquivo ZIP.

    - `files`: lista de caminhos absolutos ou relativos para os arquivos a serem compactados.
    - `zip_name`: nome (com caminho, se necessário) do arquivo ZIP a ser gerado.

    Retorna o caminho do arquivo ZIP gerado.
    """
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return zip_name
