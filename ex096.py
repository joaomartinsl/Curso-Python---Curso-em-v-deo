def Area(l, c):
    area = l * c
    print(f"Área do terreno de {l}m de largura e {c}m de comprimento: {area}m².")
    
#Main
print("CÁLCULO DO TERRENO")
print("-" * 40)
l = float(input("LARGURA(M): "))
c = float(input("COMPRIMENTO(M): "))
Area(l, c)