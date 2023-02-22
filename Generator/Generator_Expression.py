iteravel = ['Eu', 'Tenho', '__iter__']
iterator = iter(iteravel) # Tem __iter__ e __next__

import sys

lista = [n for n in range(100)] #Os valores estão todos salvos na memoria
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# O generator não deixa os valores todos salvos na memoria, apenas o valor registrado no momento
print(generator) # Não retorna os valores

# Pegando os valores que estão no generator
for n in generator:
    print(n)

# Não se pode usar o for mais de uma vez no generator
for n in generator:
    print(n, n, n, n)
