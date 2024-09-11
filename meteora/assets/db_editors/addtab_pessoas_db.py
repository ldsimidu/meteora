import sqlite3
import os
from .local_db import *
from prettytable import PrettyTable #pip install prettytable

cursor = banco_meteora.cursor()

query_pessoas = "SELECT * FROM pessoas"
view_pessoas = cursor.execute(query_pessoas)

def listar_pessoas():
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
    print(table)

