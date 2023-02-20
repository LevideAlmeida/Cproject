# args e kwargs
# args - arguments (argumentos não nomeados)
# kwargs - keywords arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Argumentos não nomeados:')
    print(args, '\n')

    print('Argumentos nomeados:')
    print(kwargs)

    # Argumentos nomeados se transformam em dicionario
    for chave, valor in kwargs.items():
        print(chave, valor)


                          #Não Nomeados
mostro_argumentos_nomeados(123, 12312, nome='Levi', endereco=129)
                                      #Nomeados

pessoa_completa = {
    'nome': 'Emily',
    'sobrenome': 'Souza',
    'idade': 16,
    'altura': 1.55,
}

print('\n')
mostro_argumentos_nomeados(**pessoa_completa)
