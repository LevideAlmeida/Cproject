"""
Listas em Python
Tipo list - Mutável
    extend - estende a lista
    + - concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

print(lista_c)

lista_a.extend(lista_b) # A lista_a foi extendida com os valores da lista_b
print(lista_a)
print(lista_b)
