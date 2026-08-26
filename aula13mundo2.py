# ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE: For
'''for c in range(1, 7):#Ele PARA no último (Não pega)
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('BOOM')

n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c)
print('FIM DA CONTAGEM')

from time import sleep
for c in range(3, 0, -1):
    print(c)
    sleep(1)
print('BOOOOOM, A bomba explodiu!')

i = int(input('Início: '))
f = int(input('Final: '))
d = int(input('De quanto em quanto? R: '))
for c in range(i, f+1, d):
    print(c)
print('FIM DA CONTAGEM')'''

s = 0  # declara a variável antes para dentro da soma ela estar definida!
for c in range(0, 5):
    n = int(input('Digite um número: '))
    s = s + n  # A cada repetição, o S é acrescentado!
print('O somatório de todos os números apresentados foi de {}.'.format(s))
