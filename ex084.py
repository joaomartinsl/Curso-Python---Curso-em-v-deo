pessoas = list()
dados = list()
total = menorpeso = maiorpeso = cont = 0
continuar = 'S'
while continuar != 'N':
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    if cont == 0:
        menorpeso = maiorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    cont += 1
    total += 1
    dados.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
menores = list()
maiores = list()
for p in pessoas:
    if p[1] == menorpeso:
        menores.append(p[0])
    if p[1] == maiorpeso:
        maiores.append(p[0])
print(f"O total de pessoas cadastradas foi {total}.")
print(f"O menor peso registrado foi {menorpeso}Kg, sendo as pessoas: {menores}")
print(f"O maior peso registrado foi {maiorpeso}Kg, sendo as pessoas: {maiores}")