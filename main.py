import os
import mysql.connector
from urllib.parse import urlparse
from datetime import datetime

def conectar_mysql():
    db_url = os.getenv("DATABASE_URL")
    parsed = urlparse(db_url)

    return mysql.connector.connect(
        host=parsed.hostname,
        port=parsed.port or 3306,
        user=parsed.username,
        password=parsed.password,
        database=parsed.path.lstrip('/')
    )

def registrar_execucao():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()

        agora = datetime.now()
        cursor.execute("INSERT INTO logs (timestamp) VALUES (%s)", (agora,))
        conn.commit()

        print(f"✅ Execução registrada em: {agora}")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Erro ao registrar execução: {e}")

if __name__ == "__main__":
    registrar_execucao()
