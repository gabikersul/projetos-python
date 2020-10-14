class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print('Código: {} - Nome: {} - Matrícula: {}'.format(str(self.codigo), self.nome, self.matricula))
