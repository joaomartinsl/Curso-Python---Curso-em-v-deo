dados = dict()
gols = list()
dados['nome'] = str(input("Nome do jogador: "))
dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? R: "))
for partidas in range(0, dados['partidas']):
    gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {partidas}: ")))
    dados['gols'] = gols[:]
dados['total'] = sum(gols)

print("-=" * 30) # RESULTADO 01

print(dados)

print("-=" * 30) # RESULTADO 02

for k, v in dados.items():
    print(f"O campo {k} tem valor {v}.")

print("-=" * 30) # RESULTADO 03

print(f"O jogador {dados['nome']} fez {dados['partidas']} partidas:")
for i, gols in enumerate(dados['gols']):
    print(f"- Na partida {i}, {dados['nome']} fez {gols} gols.")
print(f"O total de gols foi {dados['total']}.")