matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
coluna3 = pares = maior2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor para [{i}, {j}]: "))
print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end=' ')
        if coluna == 2:
            coluna3 += matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maior2 = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maior2:
                    maior2 = matriz[linha][coluna]
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da 3° coluna é {coluna3}.")
print(f"O maior valor da 2° linha é {maior2}.")