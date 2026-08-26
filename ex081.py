lista = []
while True:
    num = int(input('Digite um valor para ser adicionado na lista: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você adicionou {len(lista)} valores na lista.')
lista.sort(reverse = True)
print(f'Lista completa em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 NÃO está presente na lista!')
