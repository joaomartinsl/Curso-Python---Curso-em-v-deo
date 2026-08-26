l = float(input('Digite a largura da parede: '))
al = float(input('Digite a altura da parede: '))
area = l * al
tinta = area / 2
print('Sua parede tem a dimensão {}x{}, resultando em uma área de {}m². \nSerá necessário {} litros de tinta para pintar-la.'.format(l, al, area, tinta))
