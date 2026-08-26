lista = ['Um', 'Dois', 'Tres', 'Quatro']
lista.append('Cinco') # Adiciona um item na lista NO FINAL
lista.insert(0, 'Zero') # Adiciona um item no LOCAL ESCOLHIDO
print(lista)
del lista[0] # LOCAL
lista.pop(0) # AMBOS ELIMINAR A VARIAVEL NO LOCAL ESCOLHIDO
lista.remove('Dois') # Elimina o item ESCRITO DENTRO DELE - NOME
print(lista)
valores = list(range(4, 11)) # Forma uma lista com um RANGE de 4 A 10(Ultimo eliminado)
print(valores)
numeros = [3, 1, 5, 7, 4, 8 ,5 ,6]
print(numeros)
if 4 in numeros:
    numeros.remove(4)
else:
    print('Não achei o número 4!')
numeros [2] = 9
print(numeros)
numeros.sort() # Coloca os itens da LISTA EM ORDEM CRESCENTE
print(numeros)
numeros.sort(reverse = True) # ORDEM DECRESCENTE
print(numeros)
print(f'O tamanho dessa lista é {len(numeros)}') # TAMANHO DA LISTA
print('=' * 50)
novo = []
for c in range(0, 5):
    novo.append(int(input('Digite um número para a lista: ')))
novo.sort(reverse = True)
print(novo)
for pos, valor in enumerate(novo):
    print(f'{pos + 1}º - {valor}')
print('=' * 50)
a = [2, 3, 4, 5]
#b = a  - A partir do momento que iguala 2 listas, o que muda em uma muda na outra!
b = a[:] # vai criar uma CÓPIA DE A, logo não serao coodependentes!
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')