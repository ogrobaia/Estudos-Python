# Paradigma imperativo
# imperare

# variáveis , atribuições e sequências
# C, Fortram, Cobol, Basic, Pascal, Ada, Modula-2

# Bloco Externo
nome = "Gabriel"  # Variável GLOBAL


def minha_funcao():
    # Bloco INTERNO *Corpo da Função
    nome = "Ana"
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)


# Imprime conforme sua chamada SEQUENCIAL (exatamente na ordem em que for chamada)
minha_funcao()
print(nome)


### RETORNO ###
def par_impar():
    return ("par")


print(par_impar())


def par_impar2():
    numero = 4
    if (numero % 2) == 0:
        return "numero par"
    return "numero impar"


print(par_impar2())
