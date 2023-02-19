#Empacotamento de valores

a, b = 1, 2
a, b = b , a
# print(a, b)

# Empacotamento de dicionarios

print('Empacotamento: ', end='\n\n')

pessoa = {
    'nome': 'Levi',
    'sobrenome': 'Almeida'
}
separador = "--------------------------------------------------"

a, b = pessoa # Retorna apenas as chaves
print(a, b)

a, b = pessoa.values() # Retorna os valores dentro das chaves
print(a, b)

print(separador)

a, b = pessoa.items() # Retorna tanto as chaves quanto os valores em tuplas
print(a, b)

print(separador)

(a1, a2), (b1, b2) = pessoa.items() # Separando chaves e valores das tuplas
print(a1, a2, b1, b2)

print(separador)

for chave, valor in pessoa.items():
    print(chave, valor)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Desempacotamento de Dicionarios
print('Desempacotamento: ', end='\n\n')

outra_pessoa = {
    'nome': 'Eduarda',
    'sobrenome': 'Oliveira',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.50,
}

pessoa_completa = {**outra_pessoa, **dados_pessoa}
# O ** serve para extrair todos os valores do dicionario
print(pessoa_completa)
