import requests
from bs4 import BeautifulSoup

url = (
	"https://www.gov.br/ans/pt-br/acesso-a-informacao/"
	"participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
