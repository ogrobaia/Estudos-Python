"""
01 Area do Retângulo
02 Area do Quadrado
03 Se o produto que você quer avaliar custa (???) 
qual será o valor do mesmo com desconto de (???) %
04 Conversão de reais para dolar 
05 Conversão de dolar para reais 

"""
# Exercício 01
"""
print("Calcule a area de um Retangulo")

base = input("Qual o tamanho da base do seu retangulo?")
altura = input("Qual o tamanho da altura do seu retangulo?")
area = float(base) * float(altura) 

print(f'O seu Retangulo possui area : {area} ') 

"""
"""
# Exercicio 02

print("Qual a area do quadrado?")

lado = input("qual o valor e L ?")
area = float(lado) * float(lado) 

print(f'A area do Quadrado e de : {area}')

"""

"""
# Exercicio 03

# Obtendo valor sem desconto
V = float(input('\nInsira o valor sem desconto do produto: '))

# Obtendo a percentagem de desconto
P = float(input('Insira a percentagem de desconto: '))

# Calculando o valor descontado
Vd = V * P/100

# Calculando o valor final com desconto
Vf = V - Vd

# Imprimindo o resultado
print("\n==================================================\n")
print('O valor descontado é de: R$ {:,.2f}'.format(Vd))
print('O valor a pagar é de: R$ {:,.2f}'.format(Vf))

"""

"""
# Exercicio 04

print('Vamos montar um programa de conversão de moedas')
real = float(input('Entre com o valor em reais (R$): '))
dolar = float(input('Entre com a cotação atual do Dólar: '))
compra = real / dolar
# Lembre-se de utilizar ponto em vez de virgula para a digitração dos valores
print('Com a cotação em R$ {:.2f} você pode comprar U$ {:.2f} usando o valor R$ {:.2f} '.format(dolar, compra, real))
# valores em {:.2f}

"""

# Exercicio 05

print('Vamos montar um programa de conversão de moedas')
dolar = float(input('Entre com valor em Dolar(U$): '))
real = float(input('Entre com a cotação do real: '))
compra = dolar * real
print('Com a cotação do dolar a U$ {:.2f} você pode comprar R$ {:.2f} valor U$ {:.2f} dolar '.format(real, compra, real))