print('==' * 10)
print('10 TERMOS DE UMA P.A.')
print('==' * 10)
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = i + (10 - 1) * r
for c in range(i, d, r):
    print(c, '->', end=' ')
print(d)
print('PA Finalizada.')
