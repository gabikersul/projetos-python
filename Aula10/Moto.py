from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, rodas, modelo, potencia, partidaEletrica):
        Automovel.__init__(self, marca, rodas, modelo, potencia)
        self.partidaEletrica = partidaEletrica

    def mostrarInformacoes(self):
        print('Tipo: Moto - Qtd Rodas: {} - Marca: {} - Modelo: {} - Velocidade atual = {}km/h - Potência do motor: {} - Tem PartidaEletrica: {}'.format(
            str(self.qtdRodas), self.marca, self.modelo, str(self.velocidade), str(self.potenciaDoMotor), self.temPartidaEletrica()))
        

    def temPartidaEletrica(self):
        if self.partidaEletrica == True:
            return 'Sim'
        return 'Não'

