s = cont = n = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número (999 para parar): '))
print('Você escreveu {} números e a soma deles é {}.'.format(cont, s))
#999 é a condição de parada - FLAG