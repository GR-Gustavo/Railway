from datetime import datetime
import os

def main():
    nome = os.getenv("NOME", "usuário")  # variável de ambiente opcional
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Olá, {nome}! Este script rodou com sucesso em {agora}.")

if __name__ == "__main__":
    main()