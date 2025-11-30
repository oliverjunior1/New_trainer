import requests
import logging

def extract_data():
    url = "https://api.exchangerate.host/latest?base=EUR"
    logging.info("Extraindo dados da API...")
    response = requests.get(url)

    if response.status_code != 200:
        logging.error("Erro ao acessar API")
        raise Exception("Falha no extract")

    data = response.json()
    logging.info("Dados extraídos com sucesso")
    return data
