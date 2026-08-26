from random import shuffle
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
ordem = [n1, n2, n3, n4]
shuffle(ordem)
print('A ordem de apresentação será {}'.format(ordem))
