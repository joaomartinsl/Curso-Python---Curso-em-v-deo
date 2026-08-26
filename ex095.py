dados = dict()
gols = list()
time = list()
while True:
    dados['nome'] = str(input("Nome do jogador: "))
    dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? R: "))
    for partidas in range(0, dados['partidas']):
        gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {partidas + 1}: ")))
        dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    dados.clear()
    gols.clear()
    while True:
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print("=" * 60)
print(f"{'Cod.':>5} {'Nome':<20} ")
print("=" * 60)
for i, jog in enumerate(time):
    print(f"{i:>5} {jog['nome']:<20} | Gols: {jog['gols']} Total: {jog['total']}")
print("=" * 60)
while True:
    show = int(input("Mostrar dados de qual jogador (999 para)? Cod: "))
    if show < len(time):
        print(f"DADOS DO JOGADOR {time[show]['nome']}:")
        for i, gols in enumerate(time[show]['gols']):
            print(f"- No jogo {i + 1}, {time[show]['nome']} fez {gols} gols.")
    else:
        if show == 999:
            break
        else:
            print(f"Não foi encontrado nenhum jogador com código {show}.")
    print("=" * 60)
print("<<<< ENCERRADO >>>>")