from pacote001 import moeda
valor = float(input("Digite um valor: R$"))
print(f"O valor R${valor:.2f} pela metade é R${moeda.metade(valor):.2f}.")
print(f"O dobro do valor R${valor:.2f} é R${moeda.dobro(valor):.2f}.")
print(f"Aumentando o valor R${valor:.2f} em 10%, resultará em R${moeda.aumentar(valor, 10):.2f}.")
print(f"Diminuindo o valor R${valor:.2f} em 10%, resultará em R${moeda.diminuir(valor, 10):.2f}.")
