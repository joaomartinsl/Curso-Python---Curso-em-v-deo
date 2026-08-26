print('\033[1;32m==========LOJAS DO BRONHA==========\033[m')
total = float(input('Total da suas compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] para pagar à vista no PIX/Dinheiro
[ 2 ] para pagar à vista no Cartão
[ 3 ] para pagar parcelado no Cartão''')
paga = int(input('Digite a sua forma de pagamento: '))
if paga == 1:
    desc = total * 0.9
    print('Como você irá pagar à vista no PIX/Dinheiro, você recebe 10% de desconto! Seu total que era de R${:.2f} agora passará a ser de R${:.2f}!'.format(total, desc))
elif paga == 2:
    desc = total * 0.95
    print('Como você irá pagar à vista no Cartão, você recebe 5% de desconto! Seu total que era de R${:.2f} agora passará a ser de R${:.2f}!'.format(total, desc))
elif paga == 3:
    vezes = int(input('Em quantas vezes você quer parcelar? R: '))
    if vezes == 2:
        print('Pagando em 2x no Cartão, cada parcela sairá por R${:.2f}!'.format(total / 2))
        print('O total da sua compra é R${:.2f}.'.format(total))
    elif vezes >= 3:
        parcela = (total * 1.2) / vezes
        print('Pagando em {}x no Cartão, cada parcela sairá por R${:.2f}!'.format(vezes, parcela))
        print('O total da sua compra será R${:.2f}, pois possui 20% de juros!'.format(total * 1.2))
    else: 
        print('Não consegui identificar a quantidade de parcelas que você quer fazer, por favor, tente novamente!')
else: 
    print('Não consegui identificar a sua forma de pagamento, por favor, tente novamente!')
print('Tenha um \033[1;32mEXCELENTE\033[m dia!')