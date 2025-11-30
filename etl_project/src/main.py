import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(filename="logs/etl.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def run_etl():
    logging.info("Iniciando pipeline ETL...")
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)
    logging.info("Pipeline ETL finalizado com sucesso!")

if __name__ == "__main__":
    run_etl()