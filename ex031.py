km = float(input('Digite a distância da sua viagem: '))
print('Você está prestes a realizar uma viagem de {}km!'.format(km))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('O preço da sua viagem será R${:.2f}!'.format(preco))