import sqlite3
import os

# Caminho absoluto
caminho_do_banco = os.path.join('meteora', 'assets', 'database', 'primeiro_banco.db')
banco = sqlite3.connect(caminho_do_banco)

cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade int, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria@gmail.com')")

#banco.commit()

query = "SELECT * FROM pessoas"
view = cursor.execute(query)
print(view.fetchall())