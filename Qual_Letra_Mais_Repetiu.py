frase = 'O python é uma linguagem de programação multiparadigma, python foi criado por Guido van Rossum'
contagem_letra_mais_repetida = 0
letra_mais_repetida = None
i = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    contagem_atual = frase.count(letra_atual)

    if contagem_letra_mais_repetida < contagem_atual:

        contagem_letra_mais_repetida = contagem_atual
        letra_mais_repetida = letra_atual

    i += 1

print(contagem_letra_mais_repetida, f"'{letra_mais_repetida}'")
