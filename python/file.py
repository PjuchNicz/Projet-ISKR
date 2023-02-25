import requests
from zipfile import ZipFile
import os
def download_file(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()

        # Extract filename and extension
        file = get_filename(url) #filename.extension
        _, extension = os.path.splitext(file) #(filename, "."+extension)
        extension = extension[1:] #extension without "."


        # Create directory if not exist
        if not os.path.exists(extension):
            os.makedirs(extension)

        # Create file path
        filepath = f"{os.path.join(extension, file)}" #extension/filename.extension

        # Download file
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024*1024):
                f.write(chunk)
        
        return filepath
    except Exception as e:
        raise Exception(f"download_file : {e}") from e

def get_filename(url):
    return os.path.basename(url)

def unzip_file(zip_path, output_dir):
    try:
        with ZipFile(zip_path, 'r') as zip_file:
            zip_file.extractall(path=output_dir)
    except Exception as e:
        raise Exception(f"unzip_file : {e}") from e
