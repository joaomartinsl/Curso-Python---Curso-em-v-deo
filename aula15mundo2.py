'''cont = 1
while True:
    print(cont, end=' -> ')        Esse código faz com que o While aconteça infinitamente!
    cont += 1
print('Acabou')''' 

n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 4:
        break
    s += n
print(f'A soma de todos os números digitados é {s}.')