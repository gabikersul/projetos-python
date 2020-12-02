from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, rodas, modelo, potencia, portas):
        Automovel.__init__(self, marca, rodas, modelo, potencia)
        self.qtdPortas = portas

    def mostrarInformacoes(self):
        print('Tipo: Carro - Qtd Rodas: {} - Marca: {} - Modelo: {} - Velocidade atual = {}km/h - Potência do motor: {} - Qtd Portas: {}'.format(
            str(self.qtdRodas), self.marca, self.modelo, str(self.velocidade), str(self.potenciaDoMotor), self.qtdPortas))
        