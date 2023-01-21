"""
Laços de repetição
Break => Quebra o laço
Continue => pula uma repetição
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    if contador >= 15 and contador <= 27:
        continue

    if contador == 40:
        break

    print(contador)

print('fim')
