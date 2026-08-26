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

#Main
n = leiaInt("Digite um número: ")
print(f"O número digitado foi {n}.")