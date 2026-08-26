produtos = ('Lápis', 1.50, 'Borracha', 1.50, 'Caderno', 22.90, 'Estojo', 34.90, 'Transferidor', 10.00, 'Compasso', 7.50, 'Mochila', 129.90, 'Canetas', 22.90, 'Livro', 55.90)
print('=' * 40)  
print(f'{"LOJÃO DO JONÃO":^40}')
print('=' * 40)
for pos, item in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{item:.<30}R$', end='')
    elif pos % 2 == 1:
        print(f'{item:6.2f}')
print('=' * 40)  