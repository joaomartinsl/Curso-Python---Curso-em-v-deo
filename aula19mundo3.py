'''
No dicionário: 
dict.values() - pega o CONTEÚDO do dicionário
dict.keys() - pega os ÍNDICES do dicionário
dict.items() - pega TUDO do dicionário

dicionario = {} - Abre o dicionario (ou dict())

for k, v in dicionario.items():
- k vai servir como as keys (índices) 
- v vai servir como as values (conteúdos)

Quando for entrar em um indice específico, continua utilizando [] para entrar nele:
dicionario['indice']

# PARTE 1 - DICIONARIO BÁSICO
dicionario = {'nome': 'João Pedro', 'idade': 19, 'sexo': 'Masculino'}
dicionario['peso'] = 98.5 # O NOVO APPEND

print(dicionario)

print(dicionario.values())
print(dicionario.keys()) # Aqui são as funções novas do dict
print(dicionario.items())

print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['sexo'])

for v in dicionario.values():
    print(v)

for k in dicionario.keys():
    print(k)

for k, v in dicionario.items(): # caso queira realizar um for onde consiga pegar as keys e os values
    print(f"{k} é {v}.")

# PARTE 2 - LISTA COM DICIONARIOS
brasil = []
estado1 = {'uf': 'Bahia', 'sigla': 'BA'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado3 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

for i, d in enumerate(brasil):
    print(f"O estado 0{i + 1} {d['uf']} tem como sigla: {d['sigla']}")

'''
# PARTE 3 - CÓPIA DE DADOS NO DICIONARIO
brasil = list()
estado = dict()
for cont in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())
for estado in brasil:
    for keys, values in estado.items():
        print(f"{keys}: {values}.")

