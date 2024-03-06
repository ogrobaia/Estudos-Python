# colções e listas

precos = [20, 50, 200]
print(precos.index(200))
print(precos[2])


idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
print(total)


# LAÇOS DE REPETIÇÃO - CHUTE
import random

valor_aleatorio = random.randint(1, 10)

acertou = False

# while acertou == False:
#    chute = int(input("Chute um valor de 1 a 10: "))
#    if chute > valor_aleatorio:
#        print("chute foi maior que o valor gerado")
#    elif chute < valor_aleatorio:
#        print("Chute foi menor que o valor gerado")
#    elif chute == valor_aleatorio:
#        acertou == True
#        print("Parabens você acertou")

velocidade = int(input("Informe a velocidade que trafegava na via : "))
velocidade_max = 100
multa_leve = "leve"
multa_grave = "grave"
multa_gravissima = "gravissima"

if velocidade <= 100:
    print(" Você esta em velocidade permitida")
elif velocidade > 100 and velocidade <= 110:
    print(
        f"Você esta acima da velocidade de {velocidade_max} , multa {multa_leve}, sua velocidade era de {velocidade} "
    )
elif velocidade > 110 and velocidade <= 120:
    print(
        f"Você esta acima da velocidade de {velocidade_max} , multa {multa_grave}, sua velocidade era de {velocidade}"
    )
elif velocidade > 120:
    print(
        f"Você esta acima da velocidade de {velocidade_max}, multa {multa_gravissima}, sua velocidade era de {velocidade}"
    )
else:
    print(" Digite novamente : ")
