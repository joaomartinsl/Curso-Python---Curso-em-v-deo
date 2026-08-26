termos = 0
ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('{} ->'.format(ptermo), end=' ')
while termos != 9:
    termos += 1
    ptermo += razao
    print('{} ->'.format(ptermo), end=' ')
print('PA finalizada.')
