## Parâmetros da função ##
# parâmetro e o nome dado aos valores utiliados na definição de uma função

def nome_da_função(nome, sobrenome):
    # Corpo da Função
    print(f"Ola , {nome} {sobrenome}")


nome = input("Qual seu nome? ")
sobrenome = input("Qual seu sobrenome? ")
nome_da_função(nome, sobrenome)

# Argumentos Nomeados ## (nome="nome")


def imprimir_nome(nome, sobrenome, idade):
    print("nome: ", nome)
    print("sobrenome: ", sobrenome)
    print("idade: ", idade)


imprimir_nome(nome="maria", sobrenome="clara", idade="25")


## Parâmetro Padrão ##

# Args = Argumentos Arbitrários
def imprimir_nome1(nome=None, sobrenome=None, idade=None, *args):
    if nome != None:
        print("nome: ", nome)
        print("sobrenome: ", sobrenome)
        print("idade: ", idade)
    else:
        print("Por favor insira seus dados")
        print("---------------------------")


print()
imprimir_nome1()
imprimir_nome1(nome="daniel", sobrenome="silva", idade="39")

## ARGS ## Argumentos Arbitrários ##


def imprimir_nomes(*nomes):
    print(nomes)


def imprime_telefones(*telefones):
    print(telefones)


def ende_rua(*endereço):
    print(*endereço)


lista2 = ("Av saturnino braga nº98 - BM - RJ")
ende_rua(*lista2)


lista1 = ("24-999-88-7755", "24-988-24-6655")
imprime_telefones(*lista1)

lista = ["Ana", "marcio", "Arnaldo"]
# passa para dentro da função como TUPLA ( podendo ser modificado para lista retirando os (*) asteriscos)
imprimir_nomes(*lista)


## KWARGS - Argumento Arbitrário **KWARGS  - KEYWORD ARGUMENTS ##

def imprimi_nomes2(nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")


dicio = {'nome': 'ana', 'sobrenome': 'julia'}
imprimi_nomes2(dicio)
