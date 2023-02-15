# Métodos úteis dos dicionários em Python

separador = '---------------------------------------------------'

pessoa = {
    'nome': 'Levi',
    'sobrenome': 'Almeida',
}

print(pessoa.get('nome')) # get - Retorna o valor uma chave. Se ela não existir, retorna None

print(separador)

nome = pessoa.pop('nome') # pop - Apaga um item com a chave especificada(del)
print(nome)
print(pessoa)
print(separador)

pessoa.update({ # update - Atualiza um dicionário com outro
    'nome': 'Levi',
    'idade': 16,
    'peso(kg)': 60,
})

print(pessoa)
print(separador)

pessoa.popitem() # popitem - Apaga o último item adicionado
print(pessoa)
