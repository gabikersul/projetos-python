from Stack import Stack

pilha = Stack()
menu = '''
+--------MENU--------+
|   1 - Adicionar    |
|   2 - Remover      |
|   3 - Imprimir     |
|   0 - Sair         |
+--------------------+
Escolha: '''

while True:
    opcao = (input(menu))
    if opcao == '0':
        break
    elif opcao == '1':
       pilha.stack_push(input('Informe o valor: '))
    elif opcao == '2':
        pilha.stack_pop()   
    elif opcao == '3':
        pilha.stack_print() 
    else:
        print('=== Opção inválida ===')