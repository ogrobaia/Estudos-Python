## Diferença entre for e while
# Com While

texto = "aeiou"
k = 0
while k < len(texto):
    letra = texto[k]
    print(letra)
    k = k + 1

lista = list(range(5))
k = 0
while k < len(lista):
    i = lista[k]
    print(i)
    k = k + 1

lista1 = ["cpbr6", 42, 3.14]
k = 0
while k < len(lista1):
    x = lista[k]
    print(x)
    k = k + 1


# Com FOR

for letra in "aeiou":
    print(letra)

for i in range(5):
    print(i)

for x in ["cpbr6", 42, 3.14]:
    print(x)
