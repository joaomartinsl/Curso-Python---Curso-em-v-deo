cores = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'branco': '\033[m'
}

def leiaInt(legenda, tam = 3): 
    while True:
        try:
            i = int(input(legenda))
        except:
            print(f"{cores['vermelho']}ERRO: Digite um número INTEIRO válido!{cores['branco']}")
            continue
        else:
            if 0 < i <= tam:
                return i
            else:
                print(f"{cores['vermelho']}ERRO: A opção {i} não é válida, tente novamente.{cores['branco']}")
        
