def soma(x, y):
    print(x + y)
    return x + y

soma1 = soma(9, 9)
soma2 = soma(5, 5)
print(soma1 + soma2)

def numero(x, y):
    if x > y:
        return y ** 2
    return x ** 2

variavel = numero(8, 4)
print(variavel)
variavel = numero(2, 5)
print(variavel)
