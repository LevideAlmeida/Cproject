"""
CONSTANTES = "variaveis" que não vão mudar
muitas condições dentro de um if(ruim)
    -> muitos blocos de codigo(Ruim)
quanto mais simples melhor
"""
velocidade = 63  # Velocidade que o carro está
local_carro = 10  # Local em que o carro está na estrada

RADAR_1 = 60  # Velocidade maxima que o radar aceita
LOCAL_1 = 100  # Local onde o radar está
RADAR_RANGE = 1  # Alcance do radar

# Codigo bruto
"""
if velocidade > RADAR_1:
    print('Velocidade passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro foi multado em radar 1')

"""

# Versão mais legivel do mesmo codigo

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade passou do radar 1')

if carro_passou_radar_1:
    print("O carro passou em radar 1")

if carro_multado_radar_1:
    print('Carro foi multado em radar 1')
