"""
Metodos uteis:
    append, insert, pop, del, clear, extend, +

Create Read Update   Delete (CRUD)
 ||     ||    ||       ||
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2, 3, 4]
lista[2] = 30
print(lista)
del lista[2]
print(lista)
print(lista[2])
# Nota: Apagar um item do meio da lista, faz todos os itens posteriores
# serem movidos para tras, usando processamento
# então evitar remover itens do meio de listas muito grandes

lista.append(5) # Adicionar um item no final da lista
print(lista)
lista.pop() # Remover o item do final da lista
print(lista)
lista.append(6)
lista.append(7)
print(lista)
ultimo_valor = lista.pop(2) # O metodo pop retorna o valor removido, o que torna possivel coloca-lo em uma variavel
print(lista, "Removido:", ultimo_valor)
