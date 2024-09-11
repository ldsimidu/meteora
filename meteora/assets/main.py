from db_makers.addtab_pessoas_db import *
from functions import *

#printa todo o banco de dados atual da tabela de 'pessoas'
print(view_pessoas.fetchall())

nome = input("Digite o nome:\n->")
idade = verificar_numero("Digite a idade:\n->")
email = input("Digite o email:\n->")

cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))

banco_meteora.commit()
print(view_pessoas.fetchall())

#Responsável por fechar a conexão com a database
banco_meteora.close()