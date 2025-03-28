import requests
import time
import os
import zipfile
from bs4 import BeautifulSoup

base_url = (
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/"
    "participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
)


def fecth(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None
    return response.text


def scrap_hrefs_link(url, keyword, extension):
    response = fecth(url)
    soup = BeautifulSoup(response, "html.parser")
    return [a['href'] for a in soup.find_all('a', href=True) if keyword
            in a['href'] and a['href'].endswith(extension)]


def download_files(files, path="./"):
    if not os.path.exists(path):
        os.makedirs(path)
    downloaded_files = []
    for link in files:
        if not link.startswith('http'):
            link = requests.compat.urljoin(base_url, link)
        file_name = os.path.basename(link)
        file_path = os.path.join(path, file_name)
        if os.path.exists(file_path):
            print(f"Arquivo já existe: {file_path}")
            continue
        with open(file_path, 'wb') as f:
            f.write(requests.get(link).content)
        downloaded_files.append(file_path)
        print(f"Baixado: {file_path}")

    return downloaded_files


def converter_pdf_to_zip():
    with zipfile.ZipFile("Anexos.zip", "w") as zipf:
        for pdf in download_files(scrap_hrefs_link(base_url, "Anexo", ".pdf")):
            if os.path.exists(pdf):
                zipf.write(pdf, os.path.basename(pdf))
    print("Arquivo zip criado")


def converter_csv_to_zip(file, name):
    with zipfile.ZipFile(name, "a") as zipf:
        if os.path.exists(file):
            zipf.write(file, os.path.basename(file))
    print("Arquivo CSV adicionado ao zip")
