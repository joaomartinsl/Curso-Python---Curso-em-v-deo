s = 0
q = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        s = s + c
        q = q + 1
print('A soma de todos os {} números ímpares múltiplos de 3, dentro de 1 até 500, é {}!'.format(q, s))
