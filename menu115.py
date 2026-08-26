from time import sleep
from pacote115.dados import *

def linha(cor = 'branco'):
    if cor == 'verde':
        print(f"{cores['verde']}={cores['branco']}" * 50)
    if cor == 'vermelho':
        print(f"{cores['vermelho']}={cores['branco']}" * 50)
    if cor == 'branco':
        print("=" * 50)

def cabecalho(txt, cor = 'branco'):
    if cor == 'verde':
        linha('verde')
        print(f"{cores['verde']}{txt:^50}{cores['branco']}")
        linha('verde')
    if cor == 'vermelho':
        linha('vermelho')
        print(f"{cores['vermelho']}{txt:^50}{cores['branco']}")
        linha('vermelho')
    if cor == 'branco':
        linha()
        print(f"{txt:^50}")
        linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL', 'verde')
    c = 1
    for items in lista:
        print(f"{cores['verde']}{c}{cores['branco']} - {cores['verde']}{items}{cores['branco']}")
        c += 1
    linha('verde')
    opcao = leiaInt("Opção: ", len(lista))
    return opcao

def saindo():
    cabecalho('ENCERRANDO PROGRAMA...', 'vermelho')
    sleep(1.5)
    print(f"{cores['verde']}Volte sempre!{cores['branco']}")
