from pacote001 import moeda
valor = float(input("Digite um valor: R$"))
print(f"O valor {moeda.format(valor)} pela metade é {moeda.metade(valor, formatado = True)}.")
print(f"O dobro do valor {moeda.format(valor)} é {moeda.dobro(valor, formatado = True)}.")
print(f"Aumentando o valor {moeda.format(valor)} em 10%, resultará em {moeda.aumentar(valor, 10, formatado = True)}.")
print(f"Diminuindo o valor {moeda.format(valor)} em 10%, resultará em {moeda.diminuir(valor, 10, formatado = True)}.")