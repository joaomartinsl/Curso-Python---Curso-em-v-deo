n = int(input('Digite um número para ver a sua tabuada: '))
print('-=-' * 8)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('-=-' * 8)
