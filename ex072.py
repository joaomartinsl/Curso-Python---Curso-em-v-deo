extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
           'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
'''
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
escolha = 21
while escolha not in num:
    escolha = int(input('Digite um número entre 0 e 20: '))         - MEU CÓDIGO
print(f'O número digitado foi {extenso[escolha]}.')
'''
while True: 
    while True:
        escolha = int(input('Digite um número entre 0 e 20: '))
        if 0 <= escolha <= 20:
            break
        print('Número inválido.', end=' ')
    print(f'O número digitado foi {extenso[escolha]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Resposta inválida.')
    if resp in 'N':
        break
print('Programa finalizado.')