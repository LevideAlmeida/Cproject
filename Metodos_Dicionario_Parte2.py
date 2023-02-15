# Métodos úteis dos dicionários em Python

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
separador = '---------------------------------------------------'

# Não cria uma cópia, apenas faz com que d1 e d2 sejam o mesmo dicionario
d2 = d1

d2['c1'] = 900
print('d1:', f'\n{d1}')
print(separador)

# copy - retorna uma cópia rasa (shallow copy)
d2 = d1.copy()

d2['c1'] = 2121
print('dicionario1:', f'\n{d1}')
print(separador)
print('dicionario2:', f'\n{d2}')
print(separador)

# shallow copy: NÃO copia os valores mutaveis, mas os faz serem os mesmos valores na memoria

d1['l1'][1] = 666666
print('dicionario2:', f'\n{d2}')
print(separador)
print('dicionario1:', f'\n{d1}')
print(separador)

# deepcopy: copia TODOS os valores incluindo os mutaveis
import copy

d2 = copy.deepcopy(d1)

d2['l1'][0] = 6969
print('dicionario1:', f'\n{d1}')
print(separador)
print('dicionario2:', f'\n{d2}')
