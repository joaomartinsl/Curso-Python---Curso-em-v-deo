from pacote115.menu import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve algum ERRO na criação do seu arquivo.")
    else:
        print(f"Arquivo {a} criado com sucesso.")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Houve algum ERRO ao ler arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS:")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<35}{dado[1]:>9} anos.")
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve algum ERRO ao abrir o arquivo.")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve algum ERRO ao cadastrar a pessoa.")
        else:
            print(f"Registro de {nome} realizado com sucesso.")
    finally:
        a.close()
