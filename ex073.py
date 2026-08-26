tabela = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians', 'Athletico Paranaense', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo', 'Botafogo', 'Grêmio', 'Vitória', 'Atlético Mineiro', 'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')
print(f'TABELA BRASILEIRÃO 2026 (RODADA 3):')
for pos, time in enumerate(tabela):
    print(f'{pos + 1:2}º - {time}')
print('==' * 70)
print(f'Os 5 primeiros colocados: {tabela[:5]}')
print('==' * 70)
print(f'Os 4 últimos colocados: {tabela[16:]}')
print('==' * 70)
print(f'A tabela em ordem alfabética:')
for time in sorted(tabela):
    print(time)
print('==' * 70)
print(f'O Flamengo está na {tabela.index('Flamengo') + 1}ª posição.')