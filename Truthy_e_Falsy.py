# Valores Truthy e Falsy - tipos mutaveis e não mutaveis
lista = []
tupla = ()
dicionario = {}
conjunto = set()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'Falsy' if not valor else 'Truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista}', falsy(lista))
print(f'{dicionario}', falsy(dicionario))
print(f'{tupla}', falsy(tupla))
print(f'{string}', falsy(string))
print(f'{conjunto}', falsy(conjunto))
print(f'{inteiro}', falsy(inteiro))
print(f'{flutuante}', falsy(flutuante))
print(f'{nada}', falsy(nada))
print(f'{falso}', falsy(falso))
print(f'{intervalo}', falsy(intervalo))
