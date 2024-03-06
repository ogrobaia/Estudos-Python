"""
do While
Código para adivinhar um número
    
"""
palpite = 5 
numero = 9

while bool(palpite) is True:
    print("Qual numero correto: ")
    palpite = int(input())
    if palpite == numero:    # verificando o codigo
        print("Parabens Você acertou")
        break
    else:
        print("Você errou")
else:
    print("Weeo na aplicação")
    print(bool(palpite))
