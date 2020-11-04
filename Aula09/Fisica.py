from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprime_cpf(self):
        print(self.cpf)
    
    def _calcula_imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc