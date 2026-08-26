numeros = [[], []]
for num in range(0, 7):
    escolha = int(input(f"Digite o {num + 1}° número: "))
    if escolha % 2 == 0:
        numeros[0].append(escolha)
    else:
        numeros[1].append(escolha)
numeros[0].sort()
numeros[1].sort()
print(f"Os números pares registrados foram: {numeros[0]}")
print(f"Os números ímpares registrados foram: {numeros[1]}")
