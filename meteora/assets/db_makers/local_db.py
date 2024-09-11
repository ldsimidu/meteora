import sqlite3
import os
from db_makers.addtab_pessoas_db import *

#Arquivo definindo todos os caminhos das databases do sistema

caminho_banco_meteora = os.path.join('meteora', 'assets', 'database', 'meteora.db')
banco_meteora = sqlite3.connect(caminho_banco_meteora)