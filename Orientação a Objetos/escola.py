# class Quadrado:
#     def __init__(self, lado):
#         self.lado = lado
#         self.area = lado * lado

#     def retorna_area(self):
#         print(self.area)


# quadrado = Quadrado(2)
# quadrado.retorna_area()

# class Aluno:
#     def __init__(self, nome, idade, matricula):
#         self.__nome = nome
#         self._idade = idade
#         self.matricula = matricula
#         self.notas = None

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_idade(self):
#         return self._idade

#     def set_idade(self, idade):
#         self.__idade = idade


# aluno1 = Aluno('Jose', 15, 123456)

# print(aluno1.get_nome())
# print(aluno1.get_idade())
# print(aluno1.matricula)
# print(aluno1.notas)

# HERANÇA SIMPLES #

class Pessoa:
    # (SUPERCLASSE) - classe mãe , classe pai

    def __init__(self, nome, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Classe Pessoa")

    def imprimir_nome(self):
        return f"Estou retornando a variavel: {self.nome}"

    def trabalhar(self):
        print("Trabalhando...")

    # (SubClasse) - classe filha , classe filho


class Administrador(Pessoa):

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe} Organizando PLanilhas ...")


class Aluno(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []
        print("Classe Aluno")

    def estudar(self):
        return "Estudando..."


class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):
        nome_clase = self.__class__.__name__
        print(f"Classe {nome_clase} Ensinando...")


aluno1 = Aluno('Ana')
print(aluno1.imprimir_nome())
professor1 = Professor('Julho')
print(professor1.imprimir_nome())
professor1.trabalhar()
administrador1 = Administrador('mik')
print(administrador1.imprimir_nome())
administrador1.trabalhar()


# print(type(aluno1))
# print(type(professor1))
# print(aluno1.estudar())
# print(professor1.lecionar())
