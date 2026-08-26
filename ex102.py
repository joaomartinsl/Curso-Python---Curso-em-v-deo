def fatorial(num, show=False):
    """
    -> Funcionalidade que calcula o fatorial de um número
     Args:
        num (int): valor a ser calculado
        show (bool, optional): parametro que mostrará o calculo ou não. Defaults to False.
    Returns:
        int: fatorial calculada
    """
    print("-" * 30)
    fat = 1
    while num > 0:
        fat *= num
        if show == True:
            print(f"{num}", end=' ')
            if num != 1:
                print("x", end=' ')
            else:
                print("=", end=' ')
        num -= 1
    return fat
#MAIN
num = int(input("Digite o número para saber seu fatorial: "))
print(fatorial(num, show=True))
print(fatorial(num))
help(fatorial)