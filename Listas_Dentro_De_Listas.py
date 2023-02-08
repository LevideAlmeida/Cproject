"""
Listas dentro de listas e seus indices
"""

salas = [
    # 0        1
    ["Maria", "Helena"], # Sala 0

    # 0
    ["Levi", ],  # Sala 1

    # 0          1
    ["Vitoria", "Emily", "Alef"], # Sala 2

]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[0])

indice = 1
for sala in salas:
    print(f"Sala {indice}:")
    for aluno in sala:
        print(aluno)
    indice += 1
