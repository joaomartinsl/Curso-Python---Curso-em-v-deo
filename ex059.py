from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''MENU DE OPÇÕES:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR NÚMERO
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] ENCERRAR PROGRAMA''')
    opc = int(input('Digite sua opção: '))
    if opc == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opc == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif opc == 3:
        if n1 > n2:
            print('{} é maior que {}!'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}!'.format(n2, n1))
        else:
            print('Os dois números tem o mesmo valor!')
    elif opc == 4:
        n1 = int(input('Digite um novo valor para o PRIMEIRO número: '))
        n2 = int(input('Digite um novo valor para o SEGUNDO número: '))
    elif opc not in [1, 2, 3, 4, 5]:
        print('\033[1;31mERRO!\033[m Opção inválida, tente novamente.')
    print('==' * 20)
    sleep(1)
print('ENCERRANDO...')
sleep(3)
print('Programa encerrado. Tenha um excelente dia e volte sempre!')
