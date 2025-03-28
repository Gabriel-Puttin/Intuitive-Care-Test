from utils.scrapper import download_files, scrap_hrefs_link

BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
URL_ACTIVE_OPERATORS = (
    (
        "https://dadosabertos.ans.gov.br/FTP/PDA/"
        "operadoras_de_plano_de_saude_ativas/"
    )
)


accounting_2023_hrefs = scrap_hrefs_link(f"{BASE_URL}/2023", "2023", ".zip")
accounting_2024_hrefs = scrap_hrefs_link(f"{BASE_URL}/2024", "2024", ".zip")
carriers_ANS_report = scrap_hrefs_link(URL_ACTIVE_OPERATORS, "csv", ".csv")
print(accounting_2023_hrefs)
print(accounting_2024_hrefs)
print(carriers_ANS_report)


if __name__ == "__main__":
    download_files(accounting_2023_hrefs, "./Arquivos_contabeis/2023")
    download_files(accounting_2024_hrefs, "./Arquivos_contabeis/2024")
    download_files(carriers_ANS_report, "./Operadoras_Ativas_ANS")
