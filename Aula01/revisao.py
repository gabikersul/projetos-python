def imprimirPi():
    print("Valor do PI: ")
    print(3.14)


imprimirPi()

def getSalario():
    return 1045.0

print(getSalario())

def calcular_imprimir_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    print(area)

calcular_imprimir_area(2, 3)

def calcular_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    return area

altura = 5
volume = altura * calcular_area(4, 6)
print(volume)


def calcular_volume3(largura, area):
    volume = area * altura
    return volume


print(calcular_volume3(5, calcular_area(2, 4)))

porta = 3

def abrirPorta(porta):
    if porta > 0:
        print("Seja bem-vindo")
        porta = porta - 1
        abrirPorta(porta)
        

abrirPorta(porta)

carros = ["Doblo", "Novo Uno", "Sandero"]
print( carros[0])

