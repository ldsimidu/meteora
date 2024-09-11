import sqlite3
import os
from .local_db import *

cursor = banco_meteora.cursor()

query_pessoas = "SELECT * FROM pessoas"
view_pessoas = cursor.execute(query_pessoas)

