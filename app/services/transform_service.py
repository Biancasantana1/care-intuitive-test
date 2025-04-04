import os
from datetime import datetime
from app.core.pdf_table import extract_pdf_table
from app.core.csv_utils import save_csv_with_replacements
from app.core.zip_utils import zip_files

def process_pdf_attachment():
    """
    Processa o PDF do Anexo I da ANS, extrai as tabelas e gera um CSV transformado,
    substituindo siglas por descrições legíveis. Em seguida, compacta o CSV em um arquivo ZIP.

    - Localiza o PDF em `data/scraping/`.
    - Extrai as tabelas com `pdfplumber`.
    - Salva o CSV em `data/transform/` com nome padrão `Teste_Bianca.csv`.
    - Aplica substituições como 'OD' → 'Odontológico' e 'AMB' → 'Ambulatorial'.
    - Gera um ZIP com o CSV transformado.

    Retorna o caminho absoluto do arquivo ZIP.
    """
    os.makedirs("data/transform", exist_ok=True)
    pdf_path = 'data/scraping/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    base_name = f'Teste_Bianca'

    df = extract_pdf_table(pdf_path)
    csv_path = f'data/transform/{base_name}.csv'
    save_csv_with_replacements(df, csv_path)

    zip_path = f'data/transform/{base_name}.zip'
    zip_files([csv_path], zip_path)

    return os.path.abspath(zip_path)
