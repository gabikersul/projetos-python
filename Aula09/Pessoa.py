class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.telefone = telefone

    def imprime_nome(self):
        print(self.nome)

    def _imprime_telefone(self):
        print(self.telefone)