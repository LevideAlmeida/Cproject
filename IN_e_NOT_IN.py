# Operadores logicos in e not in
# strings são itéraveis
# Podem ser navegadas item a item
# 0 1 2 3 4 5
# L E V I V I
# -6 -5 -4 -3 -2 -1
nome = 'Levivi'
print(nome[3]) # Colocando o indice de acordo com a posição do caractere, o interpretador irá acessar o caractere naquele indice
print(nome[-3]) # Tambem funciona com numeros negativos

print('L' in nome) # Verifica se o caractere 'L' existe dentro de {nome}
print('á' in nome) # Verifica se o caractere 'á' existe dentro de {nome}

# O in verifica se algo existe dentro de uma string
# se algo ESTÁ(in) na string
# O not in apenas faz o inverso
# se algo NÃO ESTÁ(not in) na string

print('L' not in nome) #Se 'L' não está na string = true
print('á' not in nome) #Se 'á' não está na string = true
