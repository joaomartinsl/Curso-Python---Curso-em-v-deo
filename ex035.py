print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
n1 = float(input('Digite o primeiro lado: '))
n2 = float(input('Digite o segundo lado: '))
n3 = float(input('Digite o terceiro lado: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Esses segmentos acima \033[1;34mPODEM\033[m formar um triângulo!')
else:
    print('Esses segmentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo!')
