lado1 = int(input('Primeiro lado: '))
lado2 = int(input('Segundo lado: '))
lado3 = int(input('Terceiro lado: '))
if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('Estes segmentos \033[1;32mPODEM\033[m formar um triângulo e ele é \033[1;32mISÓCELES\033[m!')
    elif lado1 == lado2 == lado3:
        print('Estes segmentos \033[1;32mPODEM\033[m formar um triângulo e ele é \033[1;32mEQUILÁTERO\033[m!')
    else:
        print('Estes segmentos \033[1;32mPODEM\033[m formar um triângulo e ele é \033[1;32mESCALENO\033[m!')
else:
    print('Estes segmentos \033[1;31mNÃO PODEM\033[m formar um triângulo!')
