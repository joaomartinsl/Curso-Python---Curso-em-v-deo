h = m = maior = quant = 0
print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip()
    quant += 1
    print('=' * 40)
    if sexo in 'Mm':
        h += 1
    if sexo in 'Ff' and idade < 20:
        m += 1
    if idade >= 18:
        maior += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: ')).strip()
    print('=' * 40)
    if resp in 'Nn':
        break
print(f'Você cadastrou {quant} pessoas, sendo {h} homens!')
print(f'Ao total, tiveram {m} mulheres com menos de 20 anos e {maior} pessoas maiores de idade!')
