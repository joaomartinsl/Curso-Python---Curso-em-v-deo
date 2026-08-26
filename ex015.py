dias = int(input('Você alugou o carro tem quantos dias? R: '))
km = float(input('Quantos km você rodou com o carro? R: '))
valor = (dias * 60) + (km * 0.15)
print('Você deve pagar R${:.2f}'.format(valor))
