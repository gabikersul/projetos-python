from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricao_estadual, quantidade_funcionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricao_estadual = inscricao_estadual
        self.quantidade_funcionarios = quantidade_funcionarios

    def imprime_cnpj(self):
        print(self.__cnpj)
        
    def emitir_nota_fiscal(self):
        print(self.__inscricaoEstadual)