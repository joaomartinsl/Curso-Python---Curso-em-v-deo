vel = float(input('Qual a velocidade atual do carro? Digite: '))
if vel > 80:
    print('ATENÇÃO! Você ultrapassou o limite de velocidade que é de 80km. \nSerá aplicada uma multa de R${:.2f}!'.format((vel - 80) * 7))
else:
    print('Velocidade permitida!')
print('Tenha um bom dia e dirija com segurança!')