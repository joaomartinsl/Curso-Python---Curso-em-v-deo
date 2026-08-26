from time import sleep
def contagem(ini, fim, passo):
    print(f"Iniciando contagem de {ini} até {fim} de {passo} em {passo}:")
    print("=" * 30)
    sleep(1)
    cont = ini
    if passo != 0:
        if passo < 0:
            passo *= -1
        if ini > fim:
            while True:
                if cont < fim:
                    print("FIM!")
                    break
                print(cont, end=' ', flush=True)
                cont -= passo
                sleep(0.3)
        else:
            if fim > ini:
                while True:
                    if cont > fim:
                        print("FIM!")
                        break
                    print(cont, end=' ', flush=True)
                    cont += passo
                    sleep(0.3)
            else:
                print("O início e o fim são iguais, não é possível realizar uma contagem!")
    else:
        print("O passo é 0, logo, não é possível realizar uma contagem!")
    print("=" * 30)
    sleep(1)

#Main
contagem(1, 10, 1)
contagem(10, 0, 2)
print("<<<CONTAGEM PERSONALIZADA>>>")
inicial = int(input("Digite o valor inicial da contagem: "))
final = int(input("Digite o valor final da contagem: "))
passando = int(input("Digite o passo da contagem: "))
contagem(inicial, final, passando)
