"""
enumerate - enumera iteraveis (indices)

Usando enumarate se obtem o mesmo resultado do algoritimo do arquivo
Indice_list.py existente no repositorio "PythonProject"
"""

lista = ["Levi", "Vitoria", "Emily", "Alef"]
separador = "------------------------------------------------------"
# for item in enumerate(lista):
#     print(item)

# print(separador)


lista_enumerada = enumerate(lista)
# lista_enumerada = list(enumerate(lista))

for item in lista_enumerada:
    print(item)

print(separador)

for item in lista_enumerada:
    print(item)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print("FOR da tupla:")
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")
