# maiúsculas e minúsculas 
# símbolos e espaços

"""
Security = chave
5ecurt1ty = senha 

hex
1 = 1
2 = 2
ate 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F

"""

chave = input("Digite a base da sua senha : ")

senha = ""
for letra in chave:
    if chave in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"   
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "13"   
    elif letra in "Ee": senha = senha + "14"  
    elif letra in "Ff": senha = senha + "15"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra
print(senha)                      
