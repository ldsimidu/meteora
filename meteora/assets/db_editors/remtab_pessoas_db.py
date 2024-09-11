"""from db_editors.local_db import *
from main import id_exc
import sqlite3
import os


cursor = banco_meteora.cursor()

query_pessoas = "DELETE FROM pessoas WHERE id = ?"
cursor.execute(query_pessoas, (id_exc,))
view_pessoas = cursor.execute(query_pessoas)"""