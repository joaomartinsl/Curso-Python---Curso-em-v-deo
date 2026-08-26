lista = []
c = 0
while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    lista.append(n)
    if lista.count(n) > 1:
        print('Valor já presente na lista, não pode ser adicionado.')
        lista.pop(c)
    else:
        print('Valor adicionado com sucesso.')
    c += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 20)
lista.sort()
print(f'Os valores digitados foram: {lista}')