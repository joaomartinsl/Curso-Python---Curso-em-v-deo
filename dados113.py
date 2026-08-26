def leiaInt(legenda): 
    print("-" * 30)
    while True:
        try:
            i = int(input(legenda))
        except (ValueError, TypeError):
            print("ERRO: Digite um número INTEIRO válido!")
            continue
        except KeyboardInterrupt:
            print("O usuário preferiu não digitar o valor.")
            return 0
        else:
            return i

def leiaNum(legenda):
    print("-" * 30)
    while True:
        try:
            n = float(input(legenda))
        except (ValueError, TypeError):
            print("ERRO: Digite um número REAL válido!")
        except KeyboardInterrupt:
            print("O usuário preferiu não digitar o valor.")
            return 0
        else:
            return n
