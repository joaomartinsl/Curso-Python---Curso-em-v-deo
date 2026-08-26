casa = float(input('Digite o valor da casa desejada: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite a quantidade de anos em que você vai pagar: '))
pmensal = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, cada prestação sairá por {:.2f}!'.format(casa, anos, pmensal))
if pmensal > salario * 0.3:
    print('\033[1;31mNão podemos aprovar isso!\033[m \nIsso excede seu salário em mais de 30%!')
elif pmensal <= salario * 0.3: 
    print('Parabéns, seu empréstimo foi \033[1;32mAPROVADO\033[m!')
print('Tenha um bom dia!')
