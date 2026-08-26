'''
Interactive Help:
sempre que eu precisar saber como funciona uma operação do python
desconhecida (que eu nao saiba utilizar), posso simplesmente colocar
help(funcao) -  que aparecera um manual para explicar essa funcao 
OBS: Para aparecer, tem que ser do proprio python!

docstrings:
Serve para eu mesmo DOCUMENTAR e EXPLICAR as funcoes que EU criar,
ela fica logo abaixo da funcao e tem que abrir com 3 " e fechar com 
as mesmas 3 ".
'''
def contador(ini, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
        :param ini: início da contagem
        :param fim: final da contagem
        :param passo: passo da contagem, de quanto em quanto ela passa
        :return: sem retorno
        Função criado por João Pedro Martins
    """
    cont = ini
    while cont <= fim:
        print(cont, end=' ')
        cont += passo
    print("FIM!")

help(contador)

'''
Parâmetros Opcionais:
Isso ocorre para que, caso uma função receba menos variáveis do que o 
categorizado anteriormente, ela não de erro, funcionara normalmente, sendo
uma ótima opção para não depender da declaracao de todas as variaveis
'''
def somar1(a, b, c=0):
    """
    -> Funcionalidade que recebe 3 parâmetros (sendo 1 opcional) e somar os valores recebidos.
    Args:
        a (int): primeiro valor
        b (int): segundo valor
        c (int, optional): terceiro valor. Defaults to 0.
    Função criada por João Pedro Martins
    """
    soma = a + b + c
    print(f"A soma é {soma}.")

somar1(2, 3, 4)
somar1(8, 2)

help(somar1)

'''
Escopo de variável:
Basicamente é a explicação de variáveis globais e locais, no qual a váriavel criada
DENTRO da função é local, logo se você criar B dentro da função e pedir para printar B
fora da função, vai dar erro. 
Também existe a possibilidade de você criar uma variavel global com o mesmo nome de uma 
variável local, exemplo: A dentro vale x e A fora vale y.
'''
def teste1():
    a = 10 # VARIAVEL LOCAL
    print(f"A dentro de teste1 vale {a}.")

def teste2():
    global a # é possivel utilizar o A global, alterando o de fora também!
    a = 15
    print(f"A dentro de teste2 vale {a}")

a = 5 # VARIAVEL GLOBAL
print(f"A fora antes de teste2 vale {a}")
teste1()
teste2()
print(f"A fora depois de teste2 vale {a}")

'''
Retorno de valores:
na função, ao invés de pedir para ela printar na tela, posso retornar o valor utilizando "return"
e atribuir o resultado da funcao a uma variável, podendo utilizar-la da maneira como eu quiser
'''
def somar2(a=0, b=0, c=0):
    soma = a + b + c
    return soma

r1 = somar2(3, 2, 4)
r2 = somar2(9, 5)
r3 = somar2(3)

print(f"Meus cálculos resultaram em: {r1}, {r2} e {r3}.")