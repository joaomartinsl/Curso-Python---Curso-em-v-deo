from random import randint
from time import sleep
todosjogos = []
print("-=" * 30)
print(f"{'JOGO DA MEGA SENA':^30}")
print("-=" * 30)
quantjogos = int(input("Quantos jogos você quer que eu sorteie? R: "))
print("-=" * 30)
for num in range(0, quantjogos):
    megasena = [0, 0, 0, 0, 0, 0]
    for c in range(0, 6):
        while True:
            numero = randint(1, 60)
            if numero not in megasena:
                megasena[c] = numero
                break
    megasena.sort()
    todosjogos.append(megasena[:])
    print(f"Jogo {num + 1}: {megasena}")
    sleep(1.5)
print("-=" * 30)
print(f"Todos os jogos realizados: {todosjogos}")