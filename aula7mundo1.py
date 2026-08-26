# matematica
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
nome = input('Digite seu nome: ')
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
pot = n1 ** n2
print('A soma deles é {},\n o produto é {},\n4 a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência entre eles é {}'.format(di, pot))
print('Parabéns pelos cálculos {:=^20}!'.format(nome))