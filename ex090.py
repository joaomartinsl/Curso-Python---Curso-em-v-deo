ficha = dict()
ficha['nome'] = str(input("Nome: "))
ficha['média'] = float(input("Média final: "))
if ficha['média'] >= 7:
    ficha['situção'] = 'Aprovado'
elif ficha['média'] < 5:
    ficha['situação'] = 'Reprovado'
else:
    ficha['situação'] = 'Recuperação'
for k, v in ficha.items():
    print(f"- {k} é igual à {v}.")