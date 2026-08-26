from datetime import date
sexo = int(input('''Qual o seu sexo?
[ 1 ] para FEMININO
[ 2 ] para MASCULINO
R: '''))
atual = date.today().year
if sexo == 1:
    ano = int(input('Digite o ano em que você nasceu: '))
    idade = atual - ano
    print('Se você nasceu em {}, no ano de {} você fará ou já fez {} anos.'.format(ano, atual, idade))
    print('Como você é do sexo feminino, a senhora não é obrigada a se alistar! Caso tenha interessa, apresente-se à uma junta militar!')
elif sexo == 2:
    ano = int(input('Digite o ano em que você nasceu: '))
    idade = atual - ano
    print('Se você nasceu em {}, no ano de {} você fará ou já fez {} anos.'.format(ano, atual, idade))
    if idade > 18:
        alistamento = idade - 18
        datan = atual - alistamento
        print('Você já deveria ter se alistado há {} ano(s).'.format(alistamento))
        print('Seu alistamento foi em {}.'.format(datan))
    elif idade == 18:
        print('Vá se alistar IMEDIATAMENTE!')
    else:
        alistamento = 18 - idade
        datan = atual + alistamento
        print('Você ainda não tem a idade permitida para se alistar, faltam {} ano(s).'.format(alistamento))
        print('Seu alistamento será em {}.'.format(datan))
else:
    print('Não consegui identificar o seu sexo, por favor, digite novamente!')
