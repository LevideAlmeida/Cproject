def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

print(executa(lambda x , y : x + y, 2, 3))
# print(executa(soma, 2, 3))
# print(soma(2,3))

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

# duplica = cria_multiplicador(2)
duplica = executa(lambda m: lambda n: n*m, 2)

print(duplica(14))

#Nota: usando só pra mostrar que dar pra fazer, mas não recomendo usar pra coisas mais complexas por acabar sendo dificil de ler
