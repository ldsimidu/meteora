import sqlite3
import os
from .local_db import *
from main import id_exc

cursor = banco_meteora.cursor()

query_pessoas = "DELETE FROM pessoas WHERE id=" + id_exc
view_pessoas = cursor.execute(query_pessoas)