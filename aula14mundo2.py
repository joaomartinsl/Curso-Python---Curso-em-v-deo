#ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO: While 
'''c = 1
while c < 11:
    print(c)
    c += 1
print('Fim')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Você quer continuar? [S/N]: '))
print('Fim!')'''

n = 1
par = impar = 0
while n != 0: 
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 2 == 1:
            impar += 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))
