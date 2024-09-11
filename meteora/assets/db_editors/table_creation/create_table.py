import sqlite3
import os

caminho_banco_meteora = os.path.join('meteora', 'assets', 'database', 'meteora.db')
banco_meteora = sqlite3.connect(caminho_banco_meteora)

cursor = banco_meteora.cursor()
'''
#ADICIONAR TABLE E SUAS COLUNAS
cursor.execute("""
    CREATE TABLE pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        idade INTEGER, 
        email TEXT
    )
""")
'''


'''
cursor.execute("DROP TABLE IF EXISTS sqlite_sequence") #EXCLUIR TABLE
'''


'''
cursor.execute("ALTER TABLE pessoas ADD COLUMN telefone TEXT")
'''

cursor.execute("ALTER TABLE pessoas ADD COLUMN Genero TEXT")
'''
ADD COLUMN Endereco TEXT, 
ADD COLUMN Profissao TEXT, 
ADD COLUMN Status BOOLEAN;'''

