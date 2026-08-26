salario = float(input('Digite o valor do salário: R$'))
if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10
print('Seu salário que era de R${:.2f}, será agora de R${:.2f}.'.format(salario, aumento))
