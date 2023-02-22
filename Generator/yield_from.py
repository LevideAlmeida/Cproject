# yield from => Continuar de onde o gerador antenrior parou
def gen1():
    print("COMCEÇOU GEN1")
    yield 1
    yield 2
    yield 3
    print("ACABOU GEN1\n")

def gen2():
    print("COMCEÇOU GEN2")
    yield 10
    yield 20
    yield 30
    print("ACABOU GEN2\n")

def gerar_gen(gen=None):
    if gen is not None:
        yield from gen()

    print("COMCEÇOU GERAR_GEN")
    yield 4
    yield 5
    yield 6
    print("ACABOU GERAR_GEN\n")

g1 = gerar_gen(gen1)
g2 = gerar_gen(gen2)
g3 = gerar_gen()

for n in g1:
    print(n)

for n in g2:
    print(n)

for n in g3:
    print(n)
