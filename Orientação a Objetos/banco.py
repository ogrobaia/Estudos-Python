"""
Paradigma Imperativo - Fortran - sequencia , desicão e a Iteração
Paradigma Estruturado - C - structs
Paradigma Proceduiral - Python
    
"""
from datetime import date

# Paradigma Imperativo


def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente


"""
Classe - Um conjunto de objetos com as mesmas características
Objeto - Representação do mundo real como um tipo de dado de uma classe 
Constructor - E a função com mesmo nome da classe 
Atributo - São as variaveis de uma classe

"""
"""
Visibilidade - Modificador de acesso
 
# Privada(private) - RESTRITIVA -> Define que os atributos e métodos só podem ser manipulados dentro da classe 
# Protegida(protected) - INTERMEDIÀRIA -> Define que os atributos e métodos so podem ser manipulados
dentro da classe e nas classes que herdam da classe onde foram definidos.
# Publica(public) - MENOS RESTRITIVA -> Define que os atributos e métodos são acessivéis  em qualquer lugar

"""


class Conta:
    # Atributo de Classe

    taxa = 0.50

    @classmethod  # DECORATOR METODO DA CLASSE
    def retornaCodigo(cls):
        print('Codigo: 555')

    @staticmethod  # MÉTODO ESTATICO
    def retornaCodigoBanco():
        return '345'

    # Atributo de Instância

    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero  # Visibilidade protegida (protected)
        self.titular = titular  # Visibilidade publica (public)
        self.__saldo = saldo   # Visibilidade privada (privated)
        self.__historico = [saldo]

    def saldo(self):
        print(f'Saldo: R${self.__saldo}')

    def transacao(self, saldo):
        self.__historico.append(saldo)

    def extrato(self):
        for saldo in self.__historico:
            print(date.today())  # imprime a data
            print("-----Extrato----")
            print("Conta: ", self.titular)
            # self.saldo -= Conta.taxa  # ATRIBUTO DA CLASSE (Conta)
            print(f'Saldo: R${ self.__saldo} ')

    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)

    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


conta1 = Conta(123, 'Mona Lisa', 2300)
conta2 = Conta(456, 'Albert', 2000)

conta1.transferir(300, conta2)
conta1.saldo()
conta2.saldo()
conta1.extrato()


# Instâncias da Classe Conta
# conta1 = Conta(123, 'Joao Carlos', 2000)
# conta2 = Conta(456, 'Ana Maria', 5000)

# print(f'Titular : {conta1.titular} - Saldo: R${conta1.saldo}')
# print(f'Titular : {conta2.titular} - Saldo: R${conta2.saldo}')


# print(conta1.__dict__)
# print(conta2.__dict__)


# Atributo Dinâmico (Excluivo)
# Criado em tempo de excecução
# conta2.signo = 'peixes'
# print(conta1.__dict__)
# print(conta2.__dict__)

# Método da Classe
# Conta.retornaCodigo()  # modo correto por convenção
# conta1.retornaCodigo()

# Método Estático
# modo correto por convenção utilizando RETURN
# print(Conta.retornaCodigoBanco())
# print(conta2.retornaCodigoBanco())

"""
Simulção de Eventos Discretos -> Paradigma Oritentado a Objetos
Relação -> Destacando funções e variáveis 
---------------------------------------------------------------

Conceitos Estruturais 

-Classe

Classe é uma estrutura que abstrai um conjunto de objetos com características similares.
Definindo o comportamentodos seus objetos através das estruturas:

1- Atributos 
2- Métodos

A Classe define um tipo de dado abstrato 

- Objeto
Um objeto é a representação de um  conceito/entidade do mundo real, 
que possui um significa bem definido para um determinado software.

"""

# Reúso e Coesão
# Paradigma
# Acoplamento, Herança, Poliformismo, GAP semântico

"""
Conceitos Fundamentais

-Abstração
Processo pelo qual se isolam os atributos de um objeto,
considerando os que certos grupos de objetos tenham em comum.


-Reúso

Não existe pior prática em programação que repetir o código

"""
