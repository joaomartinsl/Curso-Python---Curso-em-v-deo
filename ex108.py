from pacote001 import moeda
valor = float(input("Digite um valor: R$"))
print(f"O valor {moeda.format(valor)} pela metade é {moeda.format(moeda.metade(valor))}.")
print(f"O dobro do valor {moeda.format(valor)} é {moeda.format(moeda.dobro(valor))}.")
print(f"Aumentando o valor {moeda.format(valor)} em 10%, resultará em {moeda.format(moeda.aumentar(valor, 10))}.")
print(f"Diminuindo o valor {moeda.format(valor)} em 10%, resultará em {moeda.format(moeda.diminuir(valor, 10))}.")
