# Introdução à função lambda (função sem nome de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções sem nome
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.

# Ordenação de listas
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)

listas = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

                #def   #parametro   #return
listas.sort(key=lambda item:        item['nome'])
           #key - chave a ser ordenada

# Vizualizando de forma crua:
# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

listas2 = sorted(listas, key=lambda item: item['nome'])

def exibe(dicionario):
    for lista in dicionario:
        print(lista)


exibe(listas)
print()
exibe(listas2)
