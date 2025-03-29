import os
import time
import mysql.connector
from datetime import datetime

def conectar_mysql():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

def registrar_horario():
    while True:
        try:
            conn = conectar_mysql()
            cursor = conn.cursor()
            agora = datetime.now()

            cursor.execute("INSERT INTO logs (timestamp) VALUES (%s)", (agora,))
            conn.commit()

            print(f"✅ Registrado: {agora}")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"❌ Erro: {e}")

        time.sleep(30)

if __name__ == "__main__":
    registrar_horario()