x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def somar(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

soma = somar(3, 12, 8, 91, 65, 43)
print(soma)

numeros = 12, 215, 28, 87

soma = somar(*numeros)
print(soma)

print(sum(numeros)) # sum (soma) => Função de soma já pronta
