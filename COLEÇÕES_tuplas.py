# Tupla e uma variavel imutável
#

lista = ["item1", "item2", "item3"]
print(lista)

# Tupla não aceita modificação de itens
# Isto e diferente de reescrever a tupla

tupla = ("item1", "item2", "item3")
print(tupla)

# nao esta modificando , mais reescrevendo ela
tupla = ("item4", "item5", "verde")
print(tupla)

# loops
tupla1 = ("item1",)  # O que define a tupla e a VIRGULA (,)
tupla2 = ("a", "b")

tupla1 = tupla1 * 3
tupla3 = tupla1 + tupla2
print(tupla3)

for x in tupla1:  # numero de itens da tupla
    print(len(x))

for x in range(len(tupla3)):  # imprime os indices com os itens ao lado
    print(x, tupla3[x])

# Desempacotar uma tupla
tupla4 = ("item4", "item5", "item6", "item7", "item8",  "item9")
print(tupla4)

(x, *y, z) = tupla4  # Atribuindo itens com *(asterisco) para desempacotar
print("x:", x)
print("y:", y)
print("z:", z)
