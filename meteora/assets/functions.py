def escolha(lista_opcoes, msg):
    """docustring:
    Solicita que o usuário faça uma escolha a partir de uma lista de opções válidas.
    
    Args:
        lista_opcoes (list): Lista contendo as opções válidas que o usuário pode escolher.
        msg (str): Mensagem a ser exibida ao usuário, indicando que ele deve fazer uma escolha.

    Returns:
        str: A escolha feita pelo usuário, convertida para letras maiúsculas.
    
    O loop continua até que o usuário forneça uma entrada que esteja dentro de `lista_opcoes`.
    """
    escolha = input(msg).upper()
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida\n')
        escolha = input(msg).upper()
    return escolha

def verificar_numero(msg):
    while True:
        numero = input(msg)
        if numero == "":
            print('\nO campo não pode ser vazio\nPor favor, insira algum dado\n')
            
        if not numero.isnumeric():
            print('\nEste dado não é um número\nPor favor, insira seus dados em números\n')
            
        else:
            return int(numero)