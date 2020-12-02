class Veiculo:
    def __init__(self, marca, rodas, modelo):
        self.marca = marca
        self.qtdRodas = rodas
        self.modelo = modelo
        self.velocidade = 0
    
    def mostrarInformacoes(self):
        print('Tipo: Veículo - Qtd Rodas: {} - Marca: {} - Modelo: {} - Velocidade Atual = {}km/h'.format(
            str(self.qtdRodas), self.marca, self.modelo,  str(self.velocidade)))

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor