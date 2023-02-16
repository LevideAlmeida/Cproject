# Metodos uteis para set
# add, update, clear, discard

set1 = set()
set1.add(1) # add - Adiciona um valor no conjunto
set1.add('Levi')
set1.update(('Luzia', 1, 2, 4)) # update - Permite a adição de varios valores ao mesmo tempo
print(set1)
set1.discard('Levi') # discard - descarta um valor. Por sets não terem indices, precisa ser enviado o valor a ser descartado
set1.discard('Luzi') # Passar valores errados não gera um erro
set1.discard('Luzia')
print(set1)
set1.clear() # clear - Limpa os valores da lista
print(set1)
