import os
import sqlite3

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

conexao = sqlite3.connect(
    CAMINHO_BANCO,
    isolation_level=None
)

conexao.execute("BEGIN EXCLUSIVE")

print("Banco TRAVADO. Pressione ENTER para liberar.")

input()

conexao.execute("ROLLBACK")
conexao.close()

print("Banco liberado.")