"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input('Digite a sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome é invertido {nome[::-1]}')
    espaco = ' ' in nome
    if espaco:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    quantidade_de_letras = len(nome)
    print(f'Seu nome tem {quantidade_de_letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[quantidade_de_letras - 1:]}')
    print(f'Sua idade é {idade}')
