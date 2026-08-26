dados = dict()
pessoas = list()
while True:
    dados.clear()
    dados['nome'] = str(input("Nome: "))
    while True:
        dados['sexo'] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print("Por favor, digite apenas M ou F para identificar!")
    dados['idade'] = int(input("Idade: "))
    pessoas.append(dados.copy())
    while True:
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print("Por favor, digite apenas S ou N para continuar!")
    if continuar == 'N':
        break
print("-=" * 30)
print(f"A) Ao todo, foram registradas {len(pessoas)} pessoas.")
total = 0
for cont in range(0, len(pessoas)):
    total += pessoas[cont]['idade']
media = total / len(pessoas)
print(f"B) A média das idades registradas foi {media} anos.")
print(f"C) As mulheres que foram registradas: ", end=' ')
for i, pessoa in enumerate(pessoas):
    if pessoa['sexo'] == 'F':
        print(f"{pessoa['nome']};", end=' ')
print()
print(f"D) Lista de pessoas que estão acima da média de idade: ")
for i, pessoa in enumerate(pessoas):
    if pessoa['idade'] > media:
        print(f"Nome: {pessoa['nome']} - Sexo: {pessoa['sexo']} - Idade: {pessoa['idade']}")
print("<<<<ENCERRADO>>>>")