import os
import sqlite3

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

clientes_da_planilha = [
    ("Bibi luisa", "61988887777", "bibiluis@email.com", "Quadra 3 Casa 10"),
    ("Beatriz Lima", "61977776666", "bia@email.com", "Rua 5 Casa 2"),
    ("Diego Martins", "61966665555", "diego@email", "Rua 8 Casa 1"),
    ("Eduarda Rocha", "61955554444", "eduarda@email.com", "rua 4 casa6se ar"),
    ("Fábio Nunes", "6194444ABCD", "fabio@email.com", "Rua 9 Casa 4"),
    ("Gabriela Souza", "61922221111", "gabi@email.com", "Rua 2 Casa 7"),
    ("Helena Dias", "61933332222", "helena@email.com", "Rua 7 Casa 3"),
]

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

for cliente in clientes_da_planilha:
    cursor.execute("""
        INSERT INTO clientes (nome, telefone, email, endereco)
        VALUES (?, ?, ?, ?)
    """, cliente)

conexao.commit()
conexao.close()

print("Importação concluída.")