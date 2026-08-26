from time import sleep
print('=' * 30)
print('{:^30}'.format('BANCO DO BRONHA'))
print('=' * 30)
saque = int(input('Digite o valor a ser sacado: '))
print('PROCESSANDO...')
sleep(2)
ced = 50
totced = 0
while True: #quando eu fiz, botei 4 whiles e 4 variaveis, uma pra cada cédula. Deu certo, mas ocupou mais memória!
    if saque >= ced:
        saque -= ced
        totced += 1
    else: 
        if totced > 0:
            print(f'Cédulas de R${ced} a ser cedido: {totced}')
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if saque == 0:
            break
print('Tenha um excelente dia!')
