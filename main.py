from datetime import datetime
import mysql.connector
import os
from urllib.parse import urlparse

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
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("⏱️ Registro:", agora)
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Registro (timestamp) VALUES (%s)", (agora,))
        conn.commit()
        print("✅ Registro salvo!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Erro ao registrar: {e}")

if __name__ == "__main__":
    registrar_execucao()