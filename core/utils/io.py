import requests
import zipfile
import json
from io import BytesIO
from typing import Union


def download_binary_file(url:str)->None:

    with requests.get(url) as r:
        content = r.content

    return content

def download_text_file(url:str)->None:

    with requests.get(url) as r:
        text = r.text

    return text


def unzip_file(zip_file:Union[str, BytesIO], target_dir:str)->None:

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
        print(f'Zipfile: {zip_file} extracted.')

def save_text_file(file_path:str, content:str)->None:

    with open(file_path, 'w') as f:
        f.write(content)

def save_binary_file(file_path:str, content:bytes)->None:

    with open(file_path, 'wb') as f:
        f.write(content)

def save_json_file(file_path:str, content:dict)->None:

    with open(file_path, 'w') as f:
        json.dump(content, f)