from datetime import date


class Paciente:
    def __init__(self, nome, idade, cpf, email):
        print("Acessei o constructor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    @classmethod
    def idadeAnoNascimento(cls, nome, anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return cls(nome, idade, cpf, email)


class Medico:
    pass


paciente = Paciente.idadeAnoNascimento(
    'Mona lisa', 1957, '000.000.000-00', 'mona@gmail.com')
print(paciente.__init__)
print(paciente.idade)
