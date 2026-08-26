from datetime import date
ficha = dict()
ficha['nome'] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
ficha['idade'] = date.today().year - nascimento
ficha['ctps'] = int(input("Carteira de Trabalho: "))
if ficha['ctps'] != 0:
    ficha['ano de contratação'] = int(input("Ano de contratação: "))
    ficha['salário'] = float(input("Salário: R$"))
    ficha['idade de aposentadoria'] = ficha['idade'] + (35 - (date.today().year - ficha['ano de contratação']))
print("-=" * 30)
for k, v in ficha.items():
    print(f"- {k} tem o valor {v}")