# Construa o algoritmo em Python de uma lista
# duplamente encadeada que possui uma função para
# inserir elementos, uma para imprimir os elementos na
# ordem que foram inseridos e uma função para imprimir
# os elementos na ordem inversa a que foram inseridos.

from Lista import Lista

lista = Lista()
menu = '''
+-------------MENU--------------+
|   1 - Adicionar no início     |
|   2 - Remover do início       |
|   3 - Adicionar no fim        |
|   4 - Remover do fim          |
|   5 - Imprimir                |
|   6 - Imprimir ordem inversa  |
|   0 - Sair                    |
+-------------------------------+
Escolha: '''

while True:
    opcao = (input(menu))

    if opcao == '0':
        break
    elif opcao == '1':
        lista.adicionar_inicio(input('Informe um valor: '))
    elif opcao == '2':
        lista.excluir_inicio(input('Informe um valor: '))
    elif opcao == '3':
        lista.adicionar_fim(input('Informe um valor: '))
    elif opcao == '4':
        lista.excluir_fim(input('Informe um valor: '))
    elif opcao == '5':
        lista.imprimir()
    elif opcao == '6':
        lista.imprimir_inverso()
    else:
        print('Opção inválida')