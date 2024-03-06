# prâmetros da função
def nome_da_funcao(nome, sobrenome):  # Parâmetro de Definição
    # corpo da função
    print(f"ola , {nome} {sobrenome}")


nome = input("Qual seu nome? ")
sobrenome = input("Qual seu sobrenome: ")
# Argumento é o nome dado aos valores utilizados na chamada de uma função
nome_da_funcao(nome, sobrenome)


# Argumentos Nomeados
def imprime_nome(nome, sobrenome, idade, cidadenatal):
    if nome != None:  # se diferente de none
        print("nome: ", nome)
        print("sobrenome: ", sobrenome)
        print("idade: ", idade)
        print("cidadenatal: ", cidadenatal)
    else:
        print("Favor insira seus dados")
        print("-----------------------")


nome = "Anna"
sobrenome = "joana"
# dentro de imprime_nome com parametros DEFINIDOS e OUTROS OPCIONAIS para deficição
# nome e sobrenome OPCIONAIS
# idade e cidadenatal DEFINIDOS
imprime_nome(nome, sobrenome, idade="18", cidadenatal="volta Redonda")


# Parâmetro Padrão

def imprimir_imóvel(nomeImovel, n_quartos, vagasGaragem=nome):
    print("---------")
    print("Titulo: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas de garagem: ", vagasGaragem)


print()

# Exemplos de nº de argumentos <= nº dos parametros
imprimir_imóvel("Casa 3 Quartos - SP", 3)
imprimir_imóvel("Apartamanto - MG ", 2, 1)

# Exemplos de nº de argumentos > nº dos parâmetros
# imprimir_imóvel("Loja Comercial", 2, 5, "desconto") #ERRO NUMERO DE ARGUMENTOS MAIOR QUE PARAMETROS

# Argumento Arbitrário *args -
# devolve o resultado com uma TUPLA


def imprimir_imovel1(nomeImovel, n_quartos, vagas_garagem=None, *args):
    print("------------------")
    print("Título: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagas_garagem != None:
        print("Vagas de garagem: ", vagas_garagem)


imprimir_imovel1("Loja Comercial", 2, 5, "desconto")


def imprimir_nomes(nomes):
    print(type(nomes))


lista = ["ana", "joao", "maria", "wilson"]
imprimir_nomes(lista)  # Utilizando (*lista) desempacota os itens
