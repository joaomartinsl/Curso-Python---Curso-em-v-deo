num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para sua conversão:
\033[1;32m[ 1 ]\033[m converter para \033[1;32mBINÁRIO\033[m.
\033[1;32m[ 2 ]\033[m converter para \033[1;32mOCTAL\033[m. 
\033[1;32m[ 3 ]\033[m converter para \033[1;32mHEXADECIMAL\033[m.''')
bases = int(input('Escolha uma das opções: '))
if bases == 1:
    print('{} como número \033[1;32mBINÁRIO\033[m é {}.'.format(num, bin(num)[2:]))
elif bases == 2:
    print('{} como número \033[1;32mOCTAL\033[m é {}.'.format(num, oct(num)[2:]))
elif bases == 3: 
    print('{} como número \033[1;32mHEXADECIMAL\033[m é {}.'.format(num, hex(num)[2:]))
else:
    print('Você não digitou uma \033[31mopção válida\033[m, por favor tente novamente e escolha uma das opções disponíveis!')