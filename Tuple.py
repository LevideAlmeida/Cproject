"""
Tipo Tuple - Tupla => Uma lista imutavel
Uma lista na qual não se remove, insere ou modifica valores
"""
lista = ("levi", "Vitoria", "Emily")

print(lista, type(lista))

lista = list(lista)

print(lista, type(lista))

lista.append("Alef")

print(lista, type(lista))

lista = tuple(lista)

print(lista, type(lista))
