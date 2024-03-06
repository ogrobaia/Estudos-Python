"""
y = 1200
x = int(input("informe o valor que recebe:"))

if x <= y:
    print("Sera cobrado Importo!")
elif x > y:
    print("Não sera cobrado Imposto")

"""

materia1 = int(input("Qual a nota da materia1?:"))
materia2 = int(input("Qual a nota da materia2?:"))
materia3 = int(input("Qual a nota da materia3?:"))


media = int(materia1 + materia2 + materia3 / 3)

if media >= 7:
    print("Voce foi aprovado!Parabêns!!!")
elif media < 7:
    print("Você esta de Recuperação! Se empenhe mais na proxima vez!!!")
    
print(media)
