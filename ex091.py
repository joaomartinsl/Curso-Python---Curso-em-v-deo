from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
    }
ranking = dict()
for k, v in jogadores.items():
    print(f"O {k} rolou um {v} no dado!")
    sleep(1)
print("-=" * 30)
print(f"{'TABELA':^60}")
print("-=" * 30)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
for i, item in enumerate(ranking):
    print(f"{i + 1}° - {item[0]} -> {item[1]} no dado.")
    sleep(1)