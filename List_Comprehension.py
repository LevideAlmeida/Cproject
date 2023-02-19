# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
lista = list(range(10))
print(lista)

lista = []
for numero in range(10):
    lista.append(numero)

print(lista)
lista.clear()

# List comprehension
lista = [
    #recebe numero
    numero
    #para cada numero
    for numero
    #no range(10)
    in range(10)
]

print(lista)

lista = [numero * 2 for numero in range(10)] # Duplicando os valores da lista
print(lista)
