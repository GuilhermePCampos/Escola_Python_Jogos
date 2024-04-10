class Aluno:
    def __init__(self, nome, idade, ra, sexo, cpf, matriculado=True):
        self.nome = nome
        self.idade = idade
        self.ra = ra  # Registro Acadêmico
        self.sexo = sexo
        self.cpf = cpf
        self.matriculado = matriculado

    def imprimir(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("RA:", self.ra)
        print("Sexo:", self.sexo)
        print("CPF:", self.cpf)
        print("Matriculado:", "Sim" if self.matriculado else "Não")

aluno1 = Aluno("João", 20, "123456", "Masculino", "123.456.789-10")
aluno1.imprimir()