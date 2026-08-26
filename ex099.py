from time import sleep
def maior(* num):
    print("=" * 40)
    print("Analisando os valores passados...")
    sleep(1)
    cont = maior = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram digitados {len(num)} números.")
    sleep(1)
    print(f"O maior número registrado foi {maior}.")
#Main
maior(2, 7, 4, 5, 1, 9, 0)
maior(2, 1)
maior(29, 111, 110)
maior()
maior(1)