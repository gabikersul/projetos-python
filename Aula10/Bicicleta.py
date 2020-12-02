from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, rodas, modelo, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, rodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def mostrarInformacoes(self):
        print('Tipo: Bicicleta - Qtd Rodas: {} - Marca: {} - Modelo: {} - Velocidade Atual = {}km/h - Marchas: {}, Tem bagageiro: {}'.format(
            str(self.qtdRodas), self.marca, self.modelo,  str(self.velocidade), str(self.numMarchas), self.temBagageiro()))

    def temBagageiro(self):
        if self.bagageiro == True:
            return 'Sim'
        return 'Não'