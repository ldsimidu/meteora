import sqlite3
import os
from .local_db import *


cursor = banco_meteora.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade int, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria@gmail.com')")

#banco.commit()

query_pessoas = "SELECT * FROM pessoas"

view_pessoas = cursor.execute(query_pessoas)

