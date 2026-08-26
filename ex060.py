# from math import factorial - Importa da biblioteca math para realizar o fatorial rapidamente!
num =  int(input('Digite um número para ver o seu fatorial: '))
fat = num
print('Calculando {}! = {}'.format(num, num), end=' ')
while num != 1:
    num -= 1
    print('x {}'.format(num), end=' ')
    fat *= num
print('= {}'.format(fat))
