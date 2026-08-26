cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes!'.format(n, cont))
if cont == 2:
    print('Por isso ele \033[1;32mÉ\033[m um número \033[1;32mPRIMO\033[m!')
else:
    print('Por isso ele \033[1;31mNÃO É\033[m um número \033[1;31mPRIMO\033[m!')
