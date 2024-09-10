from main import *

query = 'SELECT CONDICAO FROM PRODUTOS'

#Consulta com SQL
def dawdawdwa(query):
    with engine.connect() as conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall() #Criar dataframe
    return pd.DataFrame(dados, columns=consulta.keys())