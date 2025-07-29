import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiposDeCambio.db')

def obtenerUltimaFecha():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT fecha FROM tiposDeCambio")
    fechas = cursor.fetchall()

    conn.close()

    if fechas:
        fechas_convertidas = [datetime.strptime(f[0], "%d/%m/%Y") for f in fechas]
        fecha_mas_reciente = max(fechas_convertidas)
        return fecha_mas_reciente
    else:
        return None