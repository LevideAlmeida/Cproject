"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = "Levi"
preco = 1000.5942369348
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04x" % (1500, 1500))
