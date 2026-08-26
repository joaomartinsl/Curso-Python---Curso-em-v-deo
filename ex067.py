print('==' * 10)
print('PROGRAMA DE TABUADAS')
print('==' * 10) #Daqui pra cima não conta para a atividade estar correta, logo não considera no total de linhas
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0:
        break
    print('==' * 10)
    for c in range (1, 11):
        print(f'{n} x {c} = {c * n}')
    print('==' * 10)
print('PROGRAMA DE TABUADAS ENCERRADO.')