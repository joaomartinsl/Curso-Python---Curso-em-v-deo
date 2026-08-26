from random import randint
from time import sleep
cont = 0
print('-=-' * 10)
print('Jogo do PAR ou ÍMPAR')
print('-=-' * 10)
while True:
    escolha = str(input('Escolha par ou ímpar [P/I]: '))
    if escolha in 'PpIi':
        jog = int(input('Digite o seu valor: '))
        comp = randint(0, 10)
        total = jog + comp
        print('PAR')
        sleep(1)
        print('OU')
        sleep(1)
        print('IMPAR!!!')
        print('-' * 30)
        print(f'O jogador escolheu {jog} e o computador escolheu {comp}, resultando em {total}.')
        print('-' * 30)
        sleep(2)
        if (escolha in 'Pp' and total % 2 == 0) or (escolha in 'Ii' and total % 2 == 1):
            print('O jogador \033[1;32mVENCE\033[m! Meus parabéns!')
            print('Vamos jogar NOVAMENTE...')
            cont += 1
        else:
            print('O jogador \033[1;31mPERDEU\033[m!')
            sleep(0.5)
            print(f'Você ganhou {cont} vez(es).')
            print('Obrigado por jogar!')
            sleep(0.5)
            break
    else:
        print('Opção inválida! Tente novamente.')
print('\033[1;31mFIM DO JOGO!\033[m')