lista = []
for pos in range(0, 5):
    valor = int(input('Digite um valor para ser adicionado na lista: '))
    if pos == 0:
        lista.append(valor)
        print('Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos <= len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1
        print(f'Valor adicionado na posição {pos} da lista.')
print('=' * 40)
print(f'Lista completa: {lista}')