import sqlite3
import logging

def load_data(df, db_path="data/output.db"):
    logging.info("Carregando dados no banco SQLite...")

    conn = sqlite3.connect(db_path)
    df.to_sql("cotacoes", conn, if_exists="append", index=False)

    conn.close()
    logging.info("Carga concluída com sucesso!")
