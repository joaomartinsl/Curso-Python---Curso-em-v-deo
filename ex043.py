peso = float(input('Digite o seu peso (kg): '))
alt = float(input('Digite a sua altura (m): '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('O seu IMC é de {:.2f}, isso configura-se como \033[1mABAIXO DO PESO\033[m.'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu IMC é de {:.2f}, isso configura-se como \033[1mPESO IDEAL\033[m.'.format(imc))
elif 25 <= imc < 30:
    print('O seu IMC é de {:.2f}, isso configura-se como \033[1mSOBREPESO\033[m.'.format(imc))
elif 30 <= imc < 40:
    print('O seu IMC é de {:.2f}, isso configura-se como \033[1mOBESIDADE\033[m.'.format(imc))
elif imc >= 40:
    print('O seu IMC é de {:.2f}, isso configura-se como \033[1mOBESIDADE MÓRBIDA\033[m.'.format(imc))
