from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print('Código: {}  Nome: {}  Matrícula: {} Semestre: {}º'.format(str(self.codigo), self.nome, self.matricula, str(self.semestre)))