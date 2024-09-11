from db_editors.addtab_pessoas_db import *
from functions import *

#printa todo o banco de dados atual da tabela de 'pessoas'
print(view_pessoas.fetchall())

tabela_inserir = input('Qual das tabelas deseja inserir dados?\n\n(1) Pessoas\n\n(2)???\n\n->')
if tabela_inserir == '1':
    nome = input("Digite o nome:\n->")
    idade = verificar_numero("Digite a idade:\n->")
    email = input("Digite o email:\n->")

    cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))

    banco_meteora.commit()
    print(view_pessoas.fetchall())
else:
    print('ainda nao ta rolando esse dai pae')

#Responsável por fechar a conexão com a database
banco_meteora.close()