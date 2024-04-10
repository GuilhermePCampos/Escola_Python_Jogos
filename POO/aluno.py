class Aluno:
    def __init__(self, nome, idade, ra, sexo, cpf, matriculado=True):
        self.nome = nome
        self.idade = idade
        self.ra = ra  # Registro Acadêmico
        self.sexo = sexo
        self.cpf = cpf
        self.matriculado = matriculado

    def imprimir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("RA:", self.ra)
        print("Sexo:", self.sexo)
        print("CPF:", self.cpf)
        print("Matriculado:", "Sim" if self.matriculado else "Não")

    def alterar_informacoes(self, nome=None, idade=None, ra=None, sexo=None, cpf=None, matriculado=None):
        if nome:
            self.nome = nome
        if idade:
            self.idade = idade
        if ra:
            self.ra = ra
        if sexo:
            self.sexo = sexo
        if cpf:
            self.cpf = cpf
        if matriculado is not None:
            self.matriculado = matriculado

aluno1 = Aluno("João", 20, "123456", "Masculino", "123.456.789-10")
aluno1.imprimir_informacoes()