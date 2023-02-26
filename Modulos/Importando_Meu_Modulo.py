# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão

import My_Module
from My_Module import credits_module

raise_to_two = My_Module.create_potentiation(2)
raise_to_three = My_Module.create_potentiation(3)

print(raise_to_two(12))
print(raise_to_three(6))
print(credits_module)
