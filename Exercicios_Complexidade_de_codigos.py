velocidade = 61
local_carro = 90

RADAR_1 = 60
lOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')
    
if local_carro >= (lOCAL_1 + RADAR_RANGE) and  \
        local_carro <= (lOCAL_1 + RADAR_RANGE):
    print('carro multado em radar 1')
        