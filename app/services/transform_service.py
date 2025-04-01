import os
from datetime import datetime
from app.core.pdf_table import extract_pdf_table
from app.core.csv_utils import save_csv_with_replacements
from app.core.zip_utils import zip_files

def process_pdf_attachment():
    pdf_path = 'data/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    base_name = f'Teste_Bianca_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

    df = extract_pdf_table(pdf_path)
    csv_path = f'data/{base_name}.csv'
    save_csv_with_replacements(df, csv_path)

    zip_path = f'data/{base_name}.zip'
    zip_files([csv_path], zip_path)

    return os.path.abspath(zip_path)
