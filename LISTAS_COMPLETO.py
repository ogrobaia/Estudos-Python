### Listas ###

lista1 = [2.0, 3.5, 4.1, 5.1, 6.1, 7.1]
lista2 = [True, False]
lista3 = ["anna", "joao", "marcio"]
lista4 = [True, "anna", 2.5, 4, 8]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

print(lista4[2:])  # Do indice 2 em diante
print(lista2[-1])  # de tras para frente inicia como negativo
print(type(lista1))  # imprime o tipo <class>

# Slicing

print(lista1[::])
print(lista1[1:])  # retorna o index que destacamos ate o fim da lista
print(lista1[2:])  # retorna o index que destacamos ate o fim da lista
print(lista1[:3])  # retorna do começo da lista até o index - 1
print(lista1[:4])  # retorna do começo da lsita ate o index -1
print(lista1[1:4])  # retorna do index destacado ate o index -1
print(lista1[1:6:2])

nome5 = "terra"

print(nome5[2:4])

# Tamanho da lista - fução len

print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))

# funções que so podem ser utilizadas com tipo de dados numéricos

print(sum(lista1))  # Somatorio dos itens da lista
x = 2.0 + 3.5 + 4.1 + 5.1 + 6.1 + 7.1
print(x)

print(max(lista1))  # Retorna o elemento de Maior valor da lista

print(min(lista1))  # Retorna o elemento de Menor Valor da lista


lista5 = list(range(10))
print(lista5)

lista6 = list("Curso Python")
print(lista6)

# Mudar itens da lista
# index     0         1          2
lista7 = ["gato", "cachorro", "peixe", "cavalo", "tubarão", "girafa"]
print(lista7)

print(type(lista7))
print(lista7[1])

lista7[1] = 'cavalo'  # Modificar o iten de uma lista
print(lista7)

# modificar do index 1 ao 3
# Modificar mais de um item da lista
lista7[1:4] = ["águia", "morcego", "elefante"]


# Adicionando Elementos a Lista

lista8 = ["carro", "barco", "avião"]
print(lista8)

# Função insert (ADICIONANDO ITEM A LISTA INFORMANDO ONDE ELE DEVE SER INSERIDO)
lista8.insert(1, "bicicleta")

lista8.append("moto")  # Adicionando item a lista
# ADICIONA APENA UM ARGUMENTO
# SEMPRE AO FINAL DA LISTA

# Adicionar itens a lista original
lista8.extend(["bola", "lua", "sol"])

# Remover itens (ESPECÍFICO no índice)
lista8.pop(0)
del lista8[1]

# Remover item (ítem ESPECíFICO)
# lista8.remove("barco")


for x in range(len(lista8)):  # listar o total de itens da lista
    print(x, lista8[x])       # para listas, mostrar item por index


# Apagar os elementos dentro de um lista

carrinho_de_compras = ["pão", "carne", "verdura",
                       "alface"]
# carrinho_de_compras.clear()  # APAGA todos os itens da lista/NÃO deixa de existir a lista

carrinho_de_compras.sort()  # ORDENA A LISTA alfabetica


print(carrinho_de_compras)

for x in range(len(carrinho_de_compras)):
    print(x, carrinho_de_compras[x])

# Ordena lista conforme ordem ALFABETICA

lista9 = ["Ana", "Priscila", "Marco", "Antonio", "João"]
print(lista9)

lista9.sort(key=str.lower)
print(lista9)


# Concatenando listas

lista10 = ["a", "b", "c"]
lista11 = [1, 2, 3,]

lista10.extend(lista11)
print(lista10)

# Copiando uma lista / Alterando duas listas
lista12 = lista11
print(lista12)

lista12.append(4)
print(lista11)
print(lista12)
