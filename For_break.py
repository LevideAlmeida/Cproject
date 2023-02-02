for i in range(10):

    if i == 2:
        continue

    if i == 9:
        break

    for j in range(1 , 3):
        print(i, j)
else:
    print("For terminado com sucesso")
