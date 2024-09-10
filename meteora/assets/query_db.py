import sqlite3
import os

# Caminho absoluto
caminho_banco_pessoas = os.path.join('meteora', 'assets', 'database', 'primeiro_banco.db')
banco = sqlite3.connect(caminho_banco_pessoas)

cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade int, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria@gmail.com')")

#banco.commit()

query_pessoas = "SELECT * FROM pessoas"

view = cursor.execute(query_pessoas)

print(view.fetchall())