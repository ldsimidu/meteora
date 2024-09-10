from main import *

#Consulta com SQL
def sql_df(query):
    with engine.connect() as conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall() #Criar dataframe
    return pd.DataFrame(dados, columns=consulta.keys())

query = 'SELECT CONDICAO FROM PRODUTOS'

query01 = 'SELECT CONDICAO, COUNT(*) FROM PRODUTOS GROUP BY CONDICAO;'
sql_df(query01)