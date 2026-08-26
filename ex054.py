from datetime import date
atual = date.today().year
maioridade = atual - 18
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if ano > maioridade:
        menor += 1
    else:
        maior += 1
print('Ao todo, {} pessoa(s) é/são \033[1;32mMAIOR(ES)\033[m de idade ou irá/irão fazer 18 anos nesse ano. \nE, também, {} pessoa(s) é/são \033[1;31mMENOR(ES)\033[m de idade.'.format(maior, menor))
