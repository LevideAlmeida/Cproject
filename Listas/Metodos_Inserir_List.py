"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2, 3, 4]
# lista.clear()
print(lista)
lista.insert(2, 50) # (Indice[Posição na lista], valor inserido)
print(lista)

lista.insert(100, 5) # Como o indice é maior que o tamanho da lista, o valor será inserido no final da lista
print(lista)
