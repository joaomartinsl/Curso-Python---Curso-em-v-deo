from random import choice
from time import sleep
print('============JOKENPÔ============')
print('''Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Digite a sua opção: '))
if jogador == 0:
    jogador = 'PEDRA'
elif jogador == 1:
    jogador = 'PAPEL'
elif jogador == 2:
    jogador = 'TESOURA'
else: 
    print('\033[1;31mERRO\033[m! Opção inválida! Tente novamente.')
opccomp = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opccomp)
if jogador == 'PEDRA' or jogador == 'PAPEL' or jogador == 'TESOURA':
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('==' * 15)
    print('O jogador escolheu {}'.format(jogador))
    print('O computador escolheu {}'.format(computador))
    print('==' * 15)
    if jogador == computador:
        print('\033[1mEMPATE\033[m! Foi um resultado justo!')
    elif (jogador == 'PEDRA' and computador == 'TESOURA') or (jogador == 'PAPEL' and computador == 'PEDRA') or (jogador == 'TESOURA' and computador == 'PAPEL'):
        print('\033[1;32mJogador venceu\033[m! Meus parabéns!')
    else:
        print('\033[1;31mComputador venceu\033[m! Tente novamente!')