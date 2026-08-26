numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para ser inserido na lista na posição {c}: ')))
    if c == 0:
        maior = menor = numeros[0]
    else:
        if numeros[c] > numeros[c - 1]:
            maior = numeros[c]
        if numeros[c] < numeros[c - 1]:
            menor = numeros[c]
print('-=-' * 20)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior}, e ele foi digitados nas posições: ')
for pos, num in enumerate(numeros):
    if num == maior:
        print(pos, end='... ')
print(f'\nO menor número digitado foi {menor}, e ele foi digitado nas posições: ')
for pos, num in enumerate(numeros):
    if num == menor:
        print(pos, end='... ')
 