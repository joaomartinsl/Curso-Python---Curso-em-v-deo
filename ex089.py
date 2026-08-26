from time import sleep
boletim = []
continuar = 'S'
while True:
    nome = input("Nome do Aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N]: ").upper().strip()[0]
    if continuar == 'N':
        break
print("-" * 50)
for pessoa in range(0, len(boletim)):
    print(f"Aluno {pessoa}: {boletim[pessoa][0]} -> Média: {boletim[pessoa][2]}")
print("-" * 50)
while True:
    escolha = int(input("Digite o número do aluno para ver sua nota (999 finaliza o programa): "))
    if escolha < len(boletim):
        print(f"As notas de {boletim[escolha][0]} foram: {boletim[escolha][1]}.")
    elif escolha == 999:
            break
    else: 
        print("Aluno não encontrado, digite novamente!")
print("FINALIZANDO...")
sleep(1.5)
print("Volte sempre!")