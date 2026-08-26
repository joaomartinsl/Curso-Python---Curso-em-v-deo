from random import randint
from time import sleep
comp = randint(0, 5) #Faz o computador pensar (números inteiros)
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
jog = int(input('Digite o número que você ACHA que eu pensei: ')) #Jogador põe o numero que ele acha
print('PROCESSANDO...')
sleep(2)
if jog == comp:
    print('PARABÉNS! Você adivinhou o número que eu pensei!')
else:
    print('Se fudeu parça, eu GANHEI! Eu pensei no {} e você disse {}!'.format(comp, jog))
