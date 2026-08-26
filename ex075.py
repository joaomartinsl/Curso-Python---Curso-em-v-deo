num = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores:')
for n in num:
    print(n, end=' ')
print(f'\nO valor 9 foi digitado {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi encontrado.')
print('Os números pares digitados foram:')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')