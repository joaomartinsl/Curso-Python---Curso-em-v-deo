print('---' * 6)
print('LOJA DO BRONHA')
print('---' * 6)
cont = mvalor = total = m1000 = 0
mvitem = ' '
while True:
    item = str(input('Digite o produto adquirido: '))
    valor = float(input('Digite o valor do produto: R$'))
    cont += 1
    if cont == 1 or valor < mvalor: #como utilizam os mesmos códigos, posso colocar na mesma linha
        mvalor = valor
        mvitem = item
    if valor > 1000:
        m1000 += 1
    total += valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}.')
print(f'Ao todo, {m1000} itens custam mais que R$1000.00 reais.')
print(f'O item mais barato foi "{mvitem}" e custou R${mvalor:.2f}.')
