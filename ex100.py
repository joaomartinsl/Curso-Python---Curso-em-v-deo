from random import randint

def sortear(lista):
    print("Os números sorteados foram: ", end='')
    for num in range(0, 6):
        lista.append(randint(1, 10))
        print(lista[num], end=' ')
    print()

def somarPares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos números pares dessa lista deu {soma}.")

#Main
numeros = []
sortear(numeros)
somarPares(numeros)