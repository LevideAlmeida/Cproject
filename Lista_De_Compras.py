"""
Faça uma lista usando list
O usuario deve ter a opção de inserir, apagar
e listar valores da sua lista
Não permita que o programa quebre com indices
inexistentes na sua lista
"""
lista = []

import os

while True:
    tamanho_lista = len(lista)

    print("Menu de manipulação da lista: ")
    print("1 - Inserir um item na lista")
    print("2 - Apagar um item da lista")
    print("3 - Listar a lista")
    print("4 - Sair")
    opcao = input("Escolha uma opção valida e aperte ENTER: ")
    os.system("clear")

    if opcao == "1":

        if bool(lista) is False:
            item = input("Digite o nome do item para inserir na lista: ")
            lista.append(item)
            continue

        indice_item = input("Insira a posição do item na lista: ")

        if indice_item.isdigit():
            indice_item = int(indice_item)
        else:
            print("Insira um numero valido!!!!")
            continue

        item = input("Digite o nome do item para inserir na lista: ")
        lista.insert(indice_item, item)

    elif opcao == "2":
        if bool(lista) is False:
            print("Não existe nada para se apagar")
            continue

        indice_item = input("Insira a posição do item a ser excluido: ")

        if indice_item.isdigit():
            indice_item = int(indice_item)
        else:
            print("Insira um numero valido!!!!")
            continue

        if indice_item >= tamanho_lista:
            print("Não é possivel apagar nesse indice!")
            continue

        lista.pop(indice_item)

    elif opcao == "3":
        for indice, item in enumerate(lista):
            print(indice, item)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção invalida!!!")
        continue
