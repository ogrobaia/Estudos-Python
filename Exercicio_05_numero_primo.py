"""
Descobrir se um numero e primo
    
"""
print(30 * "-")

numero = int(input("Insira um numero para descobrir se ele e primo: "))

if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("Esse não eh um numero primo")
            break
    else:
        print("Esse numero e primo")
else:
    print("Esse numero não e primo: numero menor ou igual a 1") 
    
    
print(30 * "-")
           