lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor para ser adicionado na lista: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista digitada foi: {lista}')
print(f'Os números pares digitados: {pares}')
print(f'Os números ímpares digitados: {impares}')
