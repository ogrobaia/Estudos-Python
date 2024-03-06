import random

for i in range(100):
    random_number = random.randint(1, 100)

print(random_number)


numero_sorteado = []

for i in range(20):
    numero_aleatorio = random.randint(1, 100)
    numero_sorteado.append(numero_aleatorio)
print("numero sorteado: ", numero_sorteado)


x = 2
y = 5

if y > 8:
    y = y * 2
else:
    x = x * 2
    print(x + y)


conta = int(input("Conta: "))
pgto = int(input("Pagamento: "))
troco = pgto - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print(f"Uma nota de {nota}")
        troco -= nota
    if conta == pgto:
        print("Não há troco a receber")
    if troco == 0:
        break
else:
    print(f"O valor da {pgto} é menor que o valor {conta}")


n = int(input("Número: "))
for k in range(2, n):
    while n % k == 0:
        print(k)
        n = n / k
