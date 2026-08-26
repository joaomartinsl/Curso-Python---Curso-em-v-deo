num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    print('Comparando os dois números, o \033[1;34mPRIMEIRO\033[m número é \033[1;32mMAIOR\033[m')
elif num1 == num2:
    print('Ambos os valores são \033[1;32mIGUAIS\033[m')
else:
    print('Comparando os dois números, o \033[1;34mSEGUNDO\033[m número é \033[1;32mMAIOR\033[m')
