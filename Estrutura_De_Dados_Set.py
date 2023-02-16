separador = '-------------------------------------'
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

set1 = set() # vazio
print(set1, type(set1))
set2 = set('Levi')
print(set2)
set3 = {1, 2, 3}
print(set3, type(set3))
print(separador)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

set1 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 1}
print(set1) # Eliminou os valores duplicados
print(separador)

# Removendo valores repetidos de uma lista
lista1 = [1, 4, 4, 4, 6, 8, 6, 3, 4, 1, 2, 6, 8]
set2 = set(lista1)
lista2 = list(set2)
print(lista2)
