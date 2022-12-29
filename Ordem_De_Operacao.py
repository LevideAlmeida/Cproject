# Quando estão em conjunto em uma grande expressão numerica, operadores tem prioridade para serem resolvidos
# Exemplo:
# 4 + 5 ** 2 * 4 - 5 + (10 / 5)
# Prioridades
# 1. Parenteses (n + n)
# 2. **
# 3. * / // %
# 4. + -
# Operadores com mesmo nivel de prioridade são calculados da esquerda para direita

expressão_numerica = 4 + 5 ** 2 * 4 - 5 + (10 / 5)
print(expressão_numerica)
