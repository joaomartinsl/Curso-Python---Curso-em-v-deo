from random import randint
num = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(f'Os números sorteados foram: {num}')
'''
cont = maior = menor = 0
for n in num:
    cont += 1
    if cont == 1:
        maior = n 
        menor = n                                                             # MEU CÓDIGO
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'O maior número sorteado foi {maior}. \nO menor número sorteado foi {menor}.')
'''
print(f'O maior valor sorteado foi {max(num)}. \nO menor valor sorteado foi {min(num)}.')
 # APRESENTADO POR GUANABARA
