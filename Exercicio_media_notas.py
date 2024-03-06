##### Media de notas Utilizando listas

notas = [6, 7, 5, 8, 9, 10, 4]  ### elementos do Indice (7)
soma = 0 
x = 0

while x < 7:   ### Numero de Elementos do Indice (7)
    soma += notas[x]
    x += 1
    print(f"Media: {soma / x:20.2f}")  #### 20.2f   20 = distância 2f = numero de zeros apos o ponto
    
    