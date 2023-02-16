# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1 | set2
set4 = set1 & set2
set5 = set1 - set2
set6 = set2 - set1
set7 = set1 ^ set2
print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
