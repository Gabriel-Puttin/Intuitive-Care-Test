import requests
import time
import os
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


def scrap_pdfs_link():
    response = fecth(base_url)
    soup = BeautifulSoup(response, "html.parser")
    pdfs_link = [a['href'] for a in soup.find_all('a', href=True) if "Anexo"
                 in a['href'] and a['href'].endswith(".pdf")]
    return pdfs_link


def downlaod_pdfs():
    downloaded_files = []
    for link in scrap_pdfs_link():
        if not link.startswith('http'):
            link = requests.compat.urljoin(base_url, link)
        pdf_name = os.path.basename(link)
        pdf_path = os.path.join("./", pdf_name)

        with open(pdf_path, 'wb') as f:
            f.write(requests.get(link).content)
        downloaded_files.append(pdf_path)
        print(f"Baixado: {pdf_path}")

    return downloaded_files


downlaod_pdfs()
