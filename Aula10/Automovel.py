from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, rodas, modelo, potenciaDoMotor):
        Veiculo.__init__(self, marca, rodas, modelo)
        self.potenciaDoMotor = potenciaDoMotor

    def mostrarInformacoes(self):
        print('Tipo: Automóvel - Qtd Rodas: {} - Marca: {} - Modelo: {} - Velocidade atual = {}km/h - Potência do motor: {}'.format(
            str(self.qtdRodas), self.marca, self.modelo, str(self.velocidade), str(self.potenciaDoMotor)))