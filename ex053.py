f = str(input('Digite uma frase: ')).upper().strip().split()
nf = ''.join(f)
inv = str()
for n in range(len(nf) - 1, -1, -1):
    inv += nf[n]
'''inv = nf[::-1]'''  # Essa atividade pode ser feita SEM FOR também!
print('O inverso de {} é {}!'.format(nf, inv))
if nf == inv:
    print('A frase digitada \033[1;32mÉ UM PALÍNDROMO\033[m!')
else:
    print('A frase digitada \033[1;31mNÃO É UM PALÍNDROMO\033[m!')
