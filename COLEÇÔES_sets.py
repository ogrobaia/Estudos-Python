# Dicionários : Coleção não ordenada, mutável e que não permite valores duplicados
# Sets : Coleção não ordenada, imutável e que não permite valores duplicados

# sets também são conhecidos como (conjuntos)
conjunto = {"item1", 3, True, 4.7, "são paulo"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

# Acessando itens do meu Set
print(3 in conjunto)  # True
print(19 in conjunto)  # False


# A resposta sera desordenada
for x in conjunto:
    print(x)


## Adicionar e remover Elementos ##
set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item5")
print(set1)
set1.add(8)
print(set1)
set1.add(True)
print(set1)

# Função .update ( consegue passar qualquer tipo de conjunto para dentro do set)
#  utilizando {} ou () ou []
set2 = {1, 2, 3, 4, 5}
set3 = {"item1", "item2", "item3"}
set2.update(set3)
print(set2)

# Repetindo numeros ele inclui apenas os que não existirem no conjunto
set4 = {1, 2, 3, 4}
set4.update([1, 3, 5, 7])
print(set4)

# Utilizando a função (.pop ( Remove o ultimo item))
# Sabemos que set gera uma lista ALEATÓRIA,isto é, sem garantia do item que será removido
set4.pop()  # Função (.pop) remove item
print(set4)

# Função (.remove)
# Se tentar remover item que ñ existe (ocorrera erro no código)
set4.remove(3)
print(set4)

# Função (.discard)
# Se tentar remover item que ñ exite (Ñ ocorrera erro no código)
set4.discard(2)
print(set4)


### FUNÇÕES DOS SETS ###


# União de conjuntos (.update) (.union)
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}

# conjunto1.update(conjunto2)
conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

# Função .intersection
# Exibe somente os numeros que se repetem
conjunto4 = {2, 3, 14, 23, 8, 9}
conjunto5 = conjunto1.intersection(conjunto4)
print(conjunto5)

# Função (.symetric_difference)
# Exibe os elementos que são diferentes nos grupos
# Aqueles que estão repetidos entres os grupos ñ serão exibidos
conjunto6 = {1, 2, 4, 5}
conjunto7 = {1, 3, 4, 7, 9}

conjunto8 = conjunto6.symmetric_difference(conjunto7)
print(conjunto8)
