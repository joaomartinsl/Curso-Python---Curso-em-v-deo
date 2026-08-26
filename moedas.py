def metade(valor = 0, formatado = False):
    resp = valor / 2
    if formatado:
        return format(resp)
    else:
        return resp

def dobro(valor = 0, formatado = False):
    resp = valor * 2
    if formatado:
        return format(resp)
    else:
        return resp

def aumentar(valor = 0, porcentagem = 0, formatado = False):
    resp = valor + (valor * (porcentagem / 100))
    if formatado:
        return format(resp)
    else:
        return resp

def diminuir(valor = 0, porcentagem = 0, formatado = False): 
    resp = valor - (valor * (porcentagem / 100))
    if formatado:
        return format(resp)
    else:
        return resp

def format(valor = 0.0, moeda = 'R$'):
    return f"{moeda}{valor:.2f}".replace('.',',')

def resumo(valor = 0, aumento = 0, diminui = 0):
    print("=" * 35)
    print(f"{'RESUMO DO VALOR':^35}")
    print("=" * 35)
    print(f"Preço analisado: \t{format(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, formatado=True)}")
    print(f"Metade do preço: \t{metade(valor, formatado=True)}")
    print(f"{aumento}% de aumento: \t{aumentar(valor, aumento, formatado=True)}")
    print(f"{diminui}% de redução: \t{diminuir(valor, diminui, formatado=True)}")
    print("=" * 35)
    
