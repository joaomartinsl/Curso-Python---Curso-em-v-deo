def notas(*n, sit=False):
    """
    -> Funcionalidade que recebe notas (quantas quiser) e calcula o total de notas, 
    a maior nota, a menor nota, a média e (opcional) a situação do aluno

    Args:
        n (float, qualquer quantidade): notas do aluno
        sit (bool, optional): para saber se quer ver a situação do aluno ou não. Defaults to False.

    Returns:
        dict: dicionário contendo todas as informações do aluno
    """
    dados = {}
    dados['total'] = len(n)
    cont = maior = menor = 0
    while cont != len(n):
        if cont == 0:
            maior = menor = n[cont]  # PODERIA TER SIMPLESMENTE USADO max(n) e min(n) PARA ENCONTRAR ESSES VALORES MAXIMO E MINIMO
        else:
            if n[cont] > maior:
                maior = n[cont]
            if n[cont] < menor:
                menor = n[cont]
        cont += 1
    dados['maior'] = maior
    dados['menor'] = menor
    media = sum(n) / len(n)
    dados['média'] = media
    if sit == True:
        if media <= 3:
            dados['situação'] = 'PÉSSIMA'
        elif 3 < media <= 5:
            dados['situação'] = 'RUIM'
        elif 5 < media <= 7:
            dados['situação'] = 'RAZOÁVEL'
        elif media >= 9:
            dados['situação'] = 'EXCELENTE'
        else:
            dados['situação'] = 'BOM'
    return dados

#Main
help(notas)
resp1 = notas(10, 5.5, 6, sit=True)
print(resp1)
resp2 = notas(2, 3, 4, 5, 1)
print(resp2)
resp3 = notas(10, 10, 10, 10, 10, sit=True)
print(resp3)
resp4 = notas(4.5, 5, 6, 7, sit=True)
print(resp4)
resp5 = notas(1, 1, 1, sit=True)