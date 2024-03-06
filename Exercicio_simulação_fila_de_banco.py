ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um clinete ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação(f, A ou S): ")
    
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguem para atender.")
    elif operação == "F":
        ultimo += 1 
        fila.append(ultimo)
    elif operação == "S":
        break
    else:
        print("Operação invalida! Digite apenas F, A ou S!")
        