from random import randint
tent = 1
comp = randint(0, 10)
print('=' * 30 + 'JOGO DA ADIVINHAÇÃO' + '=' * 30)
jog = int(input('Acabei de pensar em um número entre 0 e 10! Será que você consegue adivinhar? \nAdivinhe o número: '))
while jog != comp:
    if jog < comp:
        jog = int(input('Mais... Tente novamente: '))
    elif jog > comp:
        jog = int(input('Menos... Tente novamente: '))
    tent += 1
print('\033[1;32mParabéns\033[m, você acertou em {} tentativa(s)!'.format(tent))
