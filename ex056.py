tidade = 0
velho = 0
nvelho = ''
meninas = 0
for p in range(1, 5):
    print('=' * 10 + '{}ª PESSOA'.format(p) + '=' * 10)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    tidade += idade
    if sexo in 'Mm':
        if idade > velho:
            velho = idade
            nvelho = nome
    if sexo in 'Ff' and idade < 20:
        meninas += 1
media = tidade / 4
print('A média de idade do grupo é {:.1f}.'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(velho, nvelho))
print('O grupo possui {} menina(s) com menos de 20 anos.'.format(meninas))
