from db_editors.addtab_pessoas_db import *
from functions import *

cursor = banco_meteora.cursor()
'''
cursor.execute("""
    CREATE TABLE pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        idade INTEGER, 
        email TEXT
    )
""")
'''

cursor.execute("DROP TABLE IF EXISTS sqlite_sequence") 
