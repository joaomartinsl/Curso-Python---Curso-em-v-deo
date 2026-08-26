from pacote115.menu import *
from pacote115.arquivo import *

arq = 'ex115arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Mostrar pessoas cadastradas', 'Cadastras nova pessoa', 'Encerrar programa'])
    if resposta == 1:
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = leiaInt("Idade: ", 150)
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        saindo()
        break
