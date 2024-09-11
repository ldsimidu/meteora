from db_makers.addtab_pessoas_db import *


print(view.fetchall())

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o email: ")

cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))

banco.commit()
print(view.fetchall())

banco.close()