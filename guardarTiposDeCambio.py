import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiposDeCambio.db')

def guardarTiposDeCambio(date_str, rate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO tiposDeCambio (fecha, tipoDeCambio) VALUES (?, ?)", (date_str, rate))
    conn.commit()
    conn.close()
    print(f"Se guardo el tipo de cambio para {date_str}: {rate}")