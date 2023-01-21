"""
Laço de repetição
while (Enquanto)
Executa uma ação enquanto a condição for verdadeira
Loop infinito => Quando o codigo não tem fim, pela condição ser verdadeira para sempre
"""

# Loop infinito:

"""
    condicao = True

    while condicao:
        print("Levi")
"""


while True:
    nome = input("Qual o seu nome? ")
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break # Quebrar o laço

print("Acabou")
