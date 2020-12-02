from Carro import Carro
from Bicicleta import Bicicleta
from Moto import Moto

motoVerdinha = Moto("Kawasaki", 2, "Verdinho", 2.0, True)
biciVermelhinha = Bicicleta("usada", 2, "Vermelhinha", 9, True)
carroAzulzinho = Carro("Fusca", 4, "Azul", 1.4, 2)

motoVerdinha.acelerar(30)
motoVerdinha.frear(10)
motoVerdinha.mostrarInformacoes()
biciVermelhinha.mostrarInformacoes()
carroAzulzinho.mostrarInformacoes()