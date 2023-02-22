# Introdução as generator functions
# Funções geradoras, são funções com a capacidade de pausar
# Normalmente funções são executadas até o seu fim, mas em generator
# elas podem pausar em sua execução até que se chame o seu proximo valor
# generator = (n for n in range(10000))

def generator(n=0):
    yield 1 # Funções generators recebem yield para pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma vez...')
    yield 3 # Pausar
    print('Vou terminar...')
    return 'Acabou' # Esse return na função generator é a mensagem de erro caso o codigo tente chamar a função além do que ela existe

# Passando pelos valores da generator
# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Fazendo isso de forma dinamica
gen = generator()
for n in gen:
    print(n)

print("------------------------------")

def generator(n=0, maximum=10):
    while True:
        if n >= maximum:
            break
        yield n
        n += 1


gen = generator(maximum=20)

for n in gen:
    print(n)
