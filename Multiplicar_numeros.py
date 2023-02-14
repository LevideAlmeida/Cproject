def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplilicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(15))
print(triplilicar(10))
print(quadruplicar(7.5))



# def duplicar(numero):
    # return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4
