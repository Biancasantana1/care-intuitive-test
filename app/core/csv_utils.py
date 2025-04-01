import pandas as pd

def save_csv_with_replacements(df: pd.DataFrame, csv_path: str):
    replacements = {
        'OD': 'Odontológico',
        'AMB': 'Ambulatorial'
    }

    columns_to_check = [col for col in df.columns if isinstance(col, str)]

    for col in columns_to_check:
        df[col] = df[col].replace(replacements, regex=True)

    df.to_csv(csv_path, index=False)
