def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = input(msg).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print(f"\033[0;31mERRO! Insira apenas valores monetários! \"{valor}\" não é um deles.\033[m")
        else:
            valido = True
            return float(valor)

def leiaInt(legenda): 
    """
    -> Funcionalidade que lê uma mensagem e retorna o valor APENAS se ele for um número inteiro válido
    Args:
        legenda (str): Legenda que vai aparecer na imagem

    Returns:
        int: valor inteiro digitado.
    """
    print("-" * 30)
    while True:
        n = input(legenda)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\033[0;31mERRO! Digite apenas números inteiros válidos.\033[m")
    return n
