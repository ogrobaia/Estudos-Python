

def maior_valor(x, y):
    if x > y:
        return x
    else:
        return y


x = int(input("Digite o numero x: "))
y = int(input("Digite o numero y: "))


maior = maior_valor(x, y)
print(f" O maior numero entre {x} e {y} é {maior}")

# Calculando a Media


def media(x, y):
    return (x + y) / 2


x = int(input("Digite o numero x: "))
y = int(input("Digite o numero y: "))

resultado_media = media(x, y)
print(f" A media entre os numeros {x} e {y} é {resultado_media}")
