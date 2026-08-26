# variáveis compostas - TUPLAS(IMUTÁVEIS): 
# utiliza-se os códigos do FATIAMENTO DE STRING para manipular as variaveis compostas!]
'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Yakissoba')

print(lanche)
print(lanche[2])
print(lanche[-1])
print(lanche[1:3])
print(lanche[1:])

#Tuplas são imutáveis:
lanche[1] = 'Refrigerante' - DA ERRO!
print(lanche[1])

for comida in lanche:
    print(f'Eu vou comer {comida}') - DADO
print('Comi')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') - POSICAO E DADO
print('Comi')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') - POSICAO E DADO
print('Comi')

print(sorted(lanche)) - APENAS ORGANIZA A TUPLA EM ORDEM ALFABÉTICA, SEM MUDAR A POSIÇÃO DOS DADOS
'''
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b - JUNTA AS DUAS TUPLAS, NÃO SOMA UMA NA OUTRA! - (a + b != b + a)

print(c)
print(c.index(8)) - LOCALIZA A POSIÇAO DO 8
print(c.index(2, 1)) - LOCALIZA A POSIÇAO DO 2 COMEÇANDO PELA POSIÇAO 1

print(c.count(5)) - CONTA QUANTOS 5 TEM
'''
'''
pessoa = ('João Pedro', 18, 'M', 108.30) - UMA TUPLA EM PYTHON PODE CONTER STR E INT/FLOAT JUNTOS
print(pessoa)
del(pessoa) - DELETA A VARIAVEL TODA
'''