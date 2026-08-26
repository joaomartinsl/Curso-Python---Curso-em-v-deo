from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Se você, atleta, nasceu em {}, no ano de {} você fará ou já fez {} anos.'.format(nasc, atual, idade))
if idade <= 9:
    print('Classificação: \033[1;32mMIRIM\033[m')
elif 14 >= idade > 9:
    print('Classificação: \033[1;32mINFANTIL\033[m')
elif 19 >= idade > 14:
    print('Classificação: \033[1;32mJÚNIOR\033[m')
elif 25 >= idade > 19:
    print('Classificação: \033[1;32mSÊNIOR\033[m')
elif idade > 25:
    print('Classificação: \033[1;32mMASTER\033[m')
