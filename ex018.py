from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
print('O seno desse ângulo é {:.2f} \nO cosseno desse ângulo é {:.2f} \nA tangente desse ângulo é {:.2f}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
