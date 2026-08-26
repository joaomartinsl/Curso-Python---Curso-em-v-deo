ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
for c in range(0, 10):
    print('{} ->'.format(ptermo), end=' ')
    ptermo += razao
    cont += 1
print('PAUSA')
termos = int(input('Digite a quantidade de termos que você quer ver: '))
while termos != 0:
    for c in range(0, termos):
        ptermo += razao
        cont += 1
        print('{} ->'.format(ptermo), end=' ')
    print('PAUSA')
    termos = int(input('Digite a quantidade de termos que você quer ver: '))
print('PA Finalizada com {} termos mostrados.'.format(cont))
