import pdfplumber
import pandas as pd

def extract_pdf_table(pdf_path: str) -> pd.DataFrame:
    """
      Extrai todas as tabelas de um PDF e retorna como um DataFrame formatado.

      - Remove quebras de linha nas células.
      - Define a primeira linha encontrada como cabeçalho.
      - Remove linhas totalmente vazias e duplicações do cabeçalho.
      - Retorna um DataFrame limpo, com índices resetados.
      """
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and any(row):
                        cleaned_row = [cell.replace('\n', ' ') if isinstance(cell, str) else cell for cell in row]
                        data.append(cleaned_row)

    df = pd.DataFrame(data)
    df = df.dropna(how='all')
    header = df.iloc[0]
    df = df[1:]
    df.columns = header

    df = df[df.apply(lambda row: not row.equals(header), axis=1)]

    df.reset_index(drop=True, inplace=True)
    return df
