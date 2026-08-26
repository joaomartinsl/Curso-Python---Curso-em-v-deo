continuar = 'S'
maior = menor = quant = total = 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    quant += 1
    total += num
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
media = total / quant
print(f'Você digitou {quant} números, sendo sua média igual à {media:.1f}.')
print('O maior número digitado foi {} e o menor número digitado foi {}.'.format(maior, menor))