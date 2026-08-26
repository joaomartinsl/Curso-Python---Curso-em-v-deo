from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hipot = hypot(co, ca)
print('Um triângulo com cateto oposto {} e cateto adjacente {}, \ntem como hipotenusa: {:.2f}'.format(co, ca, hipot))
