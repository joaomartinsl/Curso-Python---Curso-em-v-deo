nome = str(input('Qual o seu nome? R: ')).strip().title()
nome2 = nome.split()
nome3 = ' '.join(nome2)
if nome3 == 'João Pedro' or nome3 == 'Joao Pedro':
    print('Que nome lindo, meu xará!')
elif nome3 == 'Marcelo' or nome3 == 'Miguel' or nome3 == 'Cristiane':
    print('Gosto muito desse seu nome!')
else:
    print('Seja bem vindo!')
print('Tenha um bom dia, {}!'.format(nome3))
