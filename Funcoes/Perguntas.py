perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'opções': ['1', '3', '4', '6'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5 * 5?',
        'opções': ['25', '10', '15', '50'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10 / 2?',
        'opções': ['20', '0', '10', '5'],
        'resposta': '5',
    },
]

def perguntar(pergunta):

    print(pergunta['pergunta'])
    for i, opcao in enumerate(pergunta['opções']):
        print(f'{i + 1})', opcao)

    opcao_escolhida = input('Escolha uma opção e aperte ENTER: ')
    if opcao_escolhida.isdigit():
        opcao_escolhida = int(opcao_escolhida)
    else:
        return False

    if opcao_escolhida > len(pergunta['opções']) or opcao_escolhida < 1:
        return False

    if pergunta['opções'][opcao_escolhida - 1] == pergunta['resposta']:
        return True

quantidade_de_acertos = 0

for pergunta in perguntas:
    if perguntar(pergunta):
        print("Acertou!👍")
        quantidade_de_acertos += 1
    else:
        print("Errou!❌")
    print()

print(f'Você acertou {quantidade_de_acertos} de {len(perguntas)} perguntas', end=' ')

if quantidade_de_acertos == 0:
    print('😭')
elif quantidade_de_acertos == 1:
    print('👎')
elif quantidade_de_acertos == 2:
    print('😃👍')
elif quantidade_de_acertos == len(perguntas):
    print('🥳🎉💯')
