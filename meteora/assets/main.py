from db_editors.addtab_pessoas_db import *
from db_editors.remtab_pessoas_db import *
from prettytable import PrettyTable #pip install prettytable
from functions import *


#printa todo o banco de dados atual da tabela de 'pessoas'
print(view_pessoas.fetchall())

tabela_inserir = input('Qual das tabelas deseja alterar dados?\n\n(1) Pessoas\n\n(2)???\n\n->')
if tabela_inserir == '1':
    
    tabela_add_exc = input('Qual das tabelas deseja inserir ou excluir dados?\n\n(1) Adicionar\n\n(2)Excluir\n\n->')
    if tabela_add_exc == '1':
        nome = input("Digite o nome:\n->")
        idade = verificar_numero("Digite a idade:\n->")
        email = input("Digite o email:\n->")
        telefone = verificar_numero("Digite seu telefone:\n->")
        genero = input("Insira seu genero:\n->")

        cursor.execute("INSERT INTO pessoas (nome, idade, email, telefone, Genero) VALUES (?, ?, ?, ?, ?)", (nome, idade, email, telefone, genero))

        banco_meteora.commit()

        query_pessoas = "SELECT * FROM pessoas"
        cursor.execute(query_pessoas)
        rows = cursor.fetchall()

        # Definindo a tabela
        table = PrettyTable()

        # Adicionando cabeçalhos
        table.field_names = ["ID", "Nome", "Idade", "Email", "Telefone", "Genero"]

        # Adicionando as linhas
        for row in rows:
            table.add_row(row)

        # Exibindo a tabela formatada
        print(table)
    else:
        listar_pessoas()
        
        id_exc = input('Digite o ID do cadastro que deseja excluir:\n->')
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_exc))
        
        banco_meteora.commit()
        

        
else:
    print('ainda nao ta rolando esse dai pae')


