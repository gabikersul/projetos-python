nome = input('Digite o nome do estudante: ')
nota01 = float(input('Insira a 1º nota: '))
nota02 = float(input('Insira a 2º nota: '))

estudante = { 'nome' : nome, '1º nota' : nota01, '2° nota' : nota02 }

media = (estudante['1º nota'] + estudante['2° nota'])/2

estudante['media'] = media

print(estudante)