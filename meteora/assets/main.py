import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect, text

#URLs das tabelas contendo os dados
url_itens_pedidos = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/itens_pedidos.csv'
url_pedidos = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/pedidos.csv'
url_produto = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/produtos.csv'
url_vendedores = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/vendedores.csv'

#Leitura das tabelas
itens_pedidos = pd.read_csv(url_itens_pedidos)
pedidos = pd.read_csv(url_pedidos)
produto = pd.read_csv(url_produto)
vendedores = pd.read_csv(url_vendedores)

#Criação do DataBase local
engine = create_engine('sqlite:///:memory:')

#Inserindo as tabelas no DataBase
itens_pedidos.to_sql('itens_pedidos', engine, index=False)
pedidos.to_sql('pedidos', engine, index=False)
produto.to_sql('produtos', engine, index=False)
vendedores.to_sql('vendedores', engine, index=False)

#"Inspecionar" para ver se todas as tabelas foram add
inspector = inspect(engine)
print(inspector.get_table_names())