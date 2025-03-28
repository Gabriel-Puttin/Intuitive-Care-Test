import pandas as pd
import pdfplumber
from utils.scrapper import converter_csv_to_zip, converter_pdf_to_zip

converter_pdf_to_zip()


def extract_data():
    pdf_path = "./Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages[2:]:
            table = page.extract_table()
            if table:
                data.extend(table[1:])

    columns = [
        "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB",
        "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.rename(
        columns={
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial"
        },
        inplace=True
    )

    df.to_csv("rol_de_procedimentos_e_eventos.csv",
              index=False, encoding='utf-8-sig')
    print("CVS salvo com sucesso!")


if __name__ == "__main__":
    extract_data()
    converter_csv_to_zip(
        "./rol_de_procedimentos_e_eventos.csv",
        "Test_rol_de_procedimentos_e_eventos.zip"
    )
