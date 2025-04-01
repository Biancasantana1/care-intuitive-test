import zipfile
import os

def zip_files(files: list, zip_name: str):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return zip_name
