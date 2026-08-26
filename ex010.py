real = float(input('Digite a quantidade que você possui na carteira: R$'))
dolar = real / 3.27
print('Com R${:.2f} reais, você pode comprar US${:.2f} doláres!'.format(real, dolar))
