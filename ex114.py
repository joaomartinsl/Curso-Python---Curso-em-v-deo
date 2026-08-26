import urllib
import urllib.request # CONSIGO ACESSAR SITES COM ESSA BIBLIOTECA

try:
    site = urllib.request.urlopen("https://www.youtube.com")
except urllib.error.URLError:
    print("Não consegui acessar o site Youtube.")
else:
    print("Tudo ok, site Youtube acessado com sucesso.")