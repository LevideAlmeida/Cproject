# Manipulando chave e valores no dicionario
pessoa = {}

###
###
chave = 'nome'
pessoa[chave] = 'Levi'
print(pessoa[chave])


pessoa['sobrenome'] = 'Almeida'
print(pessoa['sobrenome'])

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
