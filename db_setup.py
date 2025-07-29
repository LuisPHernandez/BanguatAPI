import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiposDeCambio.db')

def create_db(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tiposDeCambio (
        fecha TEXT PRIMARY KEY,
        tipoDeCambio REAL
    )
    """)
    conn.commit()
    conn.close()
    print(f"Database y tabla creada en: {db_path}")

if __name__ == "__main__":
    create_db()