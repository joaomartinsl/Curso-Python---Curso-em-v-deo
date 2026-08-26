def jogador(n = '<desconhecido>', g = 0):
    print(f"O jogador {n} fez {g} gols.")
#Main
nome = input("Nome do jogador: ").strip()
gols = input("Gols: ").strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome != '':
    jogador(nome, gols)
else:
    jogador(g = gols)
