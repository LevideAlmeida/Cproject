# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Levi',
    'sobrenome': 'Almeida',
}
separador = '---------------------------------------------------'

print(len(pessoa)) # len - quantidade de chaves
print(separador)

print(tuple(pessoa.keys())) # keys - retorna iterável com o nome das chaves
print(separador)

print(list(pessoa.values())) # values - retorna iterável com os valores
print(separador)

print(list(pessoa.items())) # items - retorna iterável com chaves e valores
print(separador)

# Usando o metodo items para imprimir o dicionario
for chave, valor in pessoa.items():
    print(chave, valor)

print(separador)

pessoa.setdefault('idade', 16) # setdefault - adiciona valor se a chave não existe
print(pessoa['idade'])

print(separador)

print(pessoa)
