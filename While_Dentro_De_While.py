quantidade_linhas = 5
quantidade_colunas = 5

linha = 1
coluna = 1

while linha <= quantidade_linhas:

    while coluna <= quantidade_colunas:
        print(coluna, end=" ")
        coluna += 1
    coluna = 1
    print("")
    linha += 1
