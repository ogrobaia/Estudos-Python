# Listas: Coleção ordenada, MUTÁVEL e que permite valores duplicados
# Tuplas: Coleção ordenada, IMUTÁVEL e que permite valores duplicados
# Dicionario: Coleção não ordenada , MÚTAVEL e que não permite valores duplicados

lista = ["item1", "item2"]
tupla = ("item1", "item2")

dicionario = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}
print(dicionario)


# Utilizando a Quebra-de-linha
dicio = {
    "nome": "Bruna",
    "idade": "27",
    "nacionalidade": "brasileira",
    "idade": "35",  # ELE DESCONSIDERA A ANTERIOR, nao podem haver duas valores iguais
}

print(dicio)

# Acessar itens no dicionario / Imprimir
print(dicio['idade'])

print(dicio.get("nacionalidade"))

print(dicio.keys)  # imprime todas as chaves existentes no dicionario

print(len(dicio))  # imprime o numero de itens no dicionario

print(dicio.values())  # imprime os valor de chave no interior do dicionario

if "idade" in dicio:
    print("A chave idade existe")

## MODIFICAR VALORES DO DICIONARIO ##

dicio1 = {"nome": "Gabriel", "ano": 1993, "valor_lógico": True}
print(dicio1)
dicio1["nome"] = "marcos"
print(dicio1)


dicio1.update({"nome": "Ana"})
print(dicio1)


## Adicionar item ao dicionario ##

dicio1.update({"estado": "Rio de Janeiro"})
print(dicio1)

## Elimina o ultimo item do dicionario #
# apenas da versão 3.7  e acima
# nas versões anteriores ela elimina um item aleoatório

dicio1.popitem()  # (.popitem)
print(dicio1)


dicio1.pop("nome")  # Elimina o dado (.pop)
print(dicio1)

del dicio1["ano"]  # Remover utilizando (del) forma deve se utilizar [] CHAVES
print(dicio1)

dicio1.clear()  # Apaga todas as chaves do dicionario
print(dicio1)


dicio2 = {"nome": "Gabriel", "ano": 1993, "valor_lógico": True}
print(dicio2)

for x in dicio2:  # Imprime somente as chaves do dicionário
    print(x)


for x in dicio2:    # Imprime os valores das Chaves
    print(dicio2[x])

for x, y in dicio2.items():  # Imprime a CHAVE e o VALOR
    print(x, y)

dicio3 = dicio2.copy()  # Copia o dicionario por inteiro
print(dicio3)

dicio4 = dict(dicio3)  # Copia usando a fução (.dict)
print(dicio4)

dicio3["idade"] = 27
print(dicio1)
print(dicio2)
print(dicio3)
print(dicio4)


# Metodo fromkeys ## transforma tupla em dicionario

# index     0        1        2
tupla = ("item1", "item2", "item3")
dicio5 = dict.fromkeys(tupla)
print(dicio5)


# chave:valor

dicio6 = {
    "dicio1": {
        "nome": "ana",
        "idade": "25"
    },
    "dicio2": {
        "nome": "joao",
        "idade": "16"
    },
    "dicio3": {
        "nome": "maria",
        "idade": "40"
    },
}
print(dicio6)
