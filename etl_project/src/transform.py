import pandas as pd
import logging
from datetime import datetime

def transform_data(data):
    logging.info("Transformando dados...")

    rates = data["rates"]
    df = pd.DataFrame([rates])
    df = df[["BRL", "USD", "GBP"]]  # Mantém só moedas principais
    df["timestamp"] = datetime.now()

    logging.info("Transformação concluída")
    return df
