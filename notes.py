'''
Lembrar para utilizar: 
    COR - \033[m

    ex39 - from datetime import date - date.today().year - Importa o ANO ATUAL!

    ex19 - from random import choice - choice(lista) - Escolhe alguma opção da lista

    ex20 - from random import shuffle - shuffle(ordem) - Embaralha a ordem da lista

    ex28 - from random import radint - radint(x, y) - O computador pensa entre os números x e y (inteiros)
    ex28 - from time import sleep - sleep(x) - Faz o computador "dormir" por x segundos

    ex42 - end='' - Se posto no print da linha de cima, a linha que está em baixo sobe e fica do lado da primeira linha:
        print('Python', end='')
        print('é legal')
        O resultado no terminal ficaria assim:
        Python é legal

    Estrutura de repetição: FOR
        (x, y, z) x - início da contagem; y - onde a contagem PARA(y não estpa incluso na contagem); z - estruturação da contagem (-1 é reverso, 2 conta de 2 em 2...)
    
    ex48 - Quando houver uma estrutura de repetição:
        w = 0
        for c in range(x, y):
            w = w + c  <--> w += c (MESMA COISA!) - No lugar do c, pode ser utilizado qualquer número também!

    ex57 - while x not in 'yz': - Enquanto x não for y ou z, vai continuar rodando o programa!
    PS: Pode ser apenas 'in' também, no caso de enquanto x for y ou z!

    while True: - roda para SEMPRE até haver um 'break'
'''

'''pag = float(input('Digite o valor: '))
for c in range(0, 28):
    pag = pag * 2
print('Pagamento final foi de {}.'.format(pag))

FORMATAÇÃO:
{variavel:x} - x espaços
{variavel:^x} - x espaços centralizados
{float:.x} - x casas decimais


for i, l in enumerate(lista): 
- i vai ser um contador de 0 até o fim da lista.
- l vai ser a lista em si, ou seja, posso pegar l[0] ou l[1]
- uma boa opcão de for quando for utilizar lista


PARA ORDENAR DICIONÁRIOS: 
from operator import itemgetter - biblioteca para itemgetter

lista = sorted(dicionario.items(), key = itemgetter(int), reverse = True or False)
- primeiro é o dicionario a ser utilizado (com o .items())
- segundo é o itemgetter, que vai pegar o dado a ser ordenado, que acredito que sempre tem que ser um INT
- terceiro se é crescente ou decrescente.
'''
