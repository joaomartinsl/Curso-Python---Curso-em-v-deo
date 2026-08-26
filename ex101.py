def idade(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    return idade

def voto(idade):
    if 18 <= idade <= 70:
        return "VOTO OBRIGATÓRIO"
    elif idade < 16:
        return "NÃO VOTA"
    else:
        return "VOTO OPCIONAL"

#MAIN
ano = int(input("Digite o ano em que você nasceu: "))

idade = idade(ano)
voto = voto(idade)

print(f"Situação atual com {idade} anos: {voto}")