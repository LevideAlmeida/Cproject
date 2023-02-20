string = "LMNO"
lista = ["Levi", "Pedro", 1, 2, 3, "Eric"]
tupla = "python", "é", "mais", "dinamico", "que", "C"
salas = [
    # 0        1
    ["Maria", "Helena"], # Sala 0

    # 0
    ["Levi", ],  # Sala 1

    # 0          1
    ["Vitoria", "Emily", "Alef"], # Sala 2

]

for nome in lista:
    print(nome, end=" ")

print("\nLevi", "Pedro", 1, 2, 3, "Eric")
print(*lista)
print(*string)
print(*tupla)

print(*salas, sep="\n")
