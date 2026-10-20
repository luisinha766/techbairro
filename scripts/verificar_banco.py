import os
import sqlite3

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

print("\n=== CLIENTES CADASTRADOS ===")

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)


print("\n=== AUDITORIA ===")

cursor.execute("SELECT COUNT(*) FROM clientes")
total = cursor.fetchone()[0]

print("A1 - Total de clientes:", total)


# A2 - Campos vazios
cursor.execute("""
    SELECT id, nome
    FROM clientes
    WHERE TRIM(nome) = ''
       OR TRIM(telefone) = ''
       OR TRIM(email) = ''
       OR TRIM(endereco) = ''
""")

vazios = cursor.fetchall()

print("A2 - Campos vazios:", vazios)


# A3 - Telefone com letras ou símbolos
cursor.execute("""
    SELECT id, nome, telefone
    FROM clientes
    WHERE telefone GLOB '*[^0-9]*'
""")

telefones_invalidos = cursor.fetchall()

print("A3 - Telefones com letras/símbolos:", telefones_invalidos)


# A4 - E-mail fora do formato
cursor.execute("""
    SELECT id, nome, email
    FROM clientes
    WHERE email NOT LIKE '_%@_%._%'
""")

emails_invalidos = cursor.fetchall()

print("A4 - E-mails fora do formato:", emails_invalidos)

cursor.execute("""
    SELECT telefone, COUNT(*)
    FROM clientes
    GROUP BY telefone
    HAVING COUNT(*) > 1
""")

telefones_repetidos = cursor.fetchall()

print("A5 - Telefones repetidos:", telefones_repetidos)


conexao.close()