'''
pessoas = list()
dados1 = list()
dados2 = list()
dados3 = list()
dados1.append('Miguel')
dados1.append(12)
dados2.append('Cristiane')
dados2.append(50)
dados3.append('Marcelo')
dados3.append(51)
pessoas.append(dados1[:])
pessoas.append(dados2[:])
pessoas.append(dados3[:])
print(pessoas)

pessoas = [['João Pedro', 19], ['Cristiane', 50], ['Marcelo', 51], ['Miguel', 12]]
print(pessoas[0][0])
print(pessoas)
for pessoa in pessoas:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")
'''

galera = []
dado = []
for cont in range(0, 5):
    dado.append(str(input(f"Digite o nome da pessoa {cont + 1}: ")))
    dado.append(int(input(f"Digite a idade da pessoa {cont + 1}: ")))
    galera.append(dado[:])
    dado.clear()

totalmaior = totalmenor = 0
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} é maior de idade.")
        totalmaior += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        totalmenor += 1
print(f"No total, {totalmaior} pessoa(s) são/é maior(es) de idade e {totalmenor} pessoa(s) são/é menor(es) de idade.")