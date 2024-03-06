#### Excercicio de contadores com while

fim = int(input("Digite o ultimo numero a imprimir:"))

x = 0
while x <= fim:
    if x % 3 == 0:  # multiplos de 2=(par)  3=(impar)
        print(x)
    x = x + 1
    
    