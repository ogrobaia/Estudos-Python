

def reduzir_numero(numero):
    if numero > 0:
        print(numero)
        reduzir_numero(numero - 1)


numero = int(input("Informe o numero que deseja reduzir: "))
reduzir_numero(numero)


# Fatorial sem Recursão

def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(5))

# Fatorial Recursivo


def fatorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorialR(numero - 1)


print(fatorialR(5))  # Fatorial 5!4!3!2!1! =
