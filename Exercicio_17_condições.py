distancia = int(input('informe a distancia que deseja percorrer! '))

desconto = 0.45
limite = 200
valor_normal = 0.50

if distancia <= limite:
    print(f'Sera cobrado o valor de :{distancia * valor_normal} ')
if distancia > 200:
    print(f'Sera cobrado o valor de : {distancia * desconto}')
    