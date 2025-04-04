import csv
from pathlib import Path


def process_csv_files(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    for csv_file in input_dir.glob("*.csv"):
        output_file = output_dir / csv_file.name
        with open(csv_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
            reader = csv.reader(fin, delimiter=';')
            writer = csv.writer(fout, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                writer.writerow(row)
        print(f"Processado: {csv_file.name}")


def main():
    raw_operadores = Path("data/raw_csv/operadores_csv")
    processed_operadores = Path("data/operadores_csv")

    raw_demonstrativos = Path("data/raw_csv/demonstrativos_csv")
    processed_demonstrativos = Path("data/demonstrativos_csv")

    process_csv_files(raw_operadores, processed_operadores)
    process_csv_files(raw_demonstrativos, processed_demonstrativos)


if __name__ == "__main__":
    main()
