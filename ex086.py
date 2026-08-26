matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor para [{i}, {j}]: "))
print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end=' ')
    print()