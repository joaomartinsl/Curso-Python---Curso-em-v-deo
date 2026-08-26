'''
FUNÇÕES - def:
É recomendado dar 2 espaços entre uma def e a main
# FUNCAO 1
def mostrarLinha():
    print("=" * 60)

#Main
mostrarLinha()
print(f"{'João Pedro':^60}")
mostrarLinha()


#FUNCAO 2
def mensagem(msg):
    print("=" * 60)
    print(f"{msg:^60}")
    print("=" * 60)

#Main
mensagem('SOU JONY BRONHA')


#FUNCAO 3
def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B vale {s}")

#Main
soma(12, 8)
soma(a = 3, b = 12)
soma(b = 7, a = 13)


#FUNCAO 4
def contador(* num):
    tam = len(num)
    print(f"Os números digitados foram {num} e, ao todo, tem {tam} números.")

#Main
contador(4, 5, 2)
contador(1, 2)
contador(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
'''

#FUNCAO 5
def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2

#Main
valores = [1, 2, 4, 8, 16, 32]
print(valores)
dobra(valores)
print(valores)