salario1 = float(input('Qual seu salario? '))
aumento1 = salario1 * 10 / 100
aumento2 = salario1 * 15 / 100

if salario1 > 1.250:
    print(f'Seu salario sera de : {salario1 + aumento1}')
else:
    salario1 <= 1.250
    print(f' Seu salario sera de: {salario1 + aumento2}')
