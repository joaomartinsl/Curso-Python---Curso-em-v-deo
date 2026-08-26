print('-=-' * 10)
print('Sequência de Fibonacci')
print('-=-' * 10)
num = int(input('Digite a quantidade de termos que você quer que mostre: '))
fibo = 3
p1 = 0
p2 = 1
print('{} -> {} ->'.format(p1, p2), end=' ')
while fibo <= num:
    p3 = p2 + p1
    print('{} ->'.format(p3), end=' ')
    p1 = p2 # se eu colocar dois =, vai dar errado, por que cria a condiçao que um é igual ao outro, logo apenas 1 = é a maneira correta.
    p2 = p3
    fibo += 1
print('FIM')