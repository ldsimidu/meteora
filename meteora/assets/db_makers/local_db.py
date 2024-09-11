import sqlite3
import os
from db_makers.addtab_pessoas_db import *

#Arquivo definindo todos os caminhos das databases do sistema

caminho_banco = os.path.join('meteora', 'assets', 'database', 'meteora.db')
banco = sqlite3.connect(caminho_banco)