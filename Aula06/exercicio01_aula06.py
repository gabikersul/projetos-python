
menu = '''
+---------------MENU--------------+
| 1 - Transformar num em texto    |
| 0 - Sair                        |
+---------------------------------+
Escolha: '''

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

def printNumDigitado():
    num_extenso = int(input('Digite um número de 0 a 9: '))
    print('Número digitado: {}\n'.format(num[num_extenso]))

while True:
    opcao = (input(menu))
    if opcao == '0':
        break
    elif opcao == '1':
        printNumDigitado()
    else:
        print('===== Opção inválida =====')


