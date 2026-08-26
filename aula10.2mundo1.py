n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Parabéns, sua média final foi {:.1f} e você passou nessa matéria!'.format(m))
else:
    print('Infelizmente sua média final foi {:.1f} você não passou nessa matéria.'.format(m))
print('Tenha um bom dia!')
#print('Sua média final foi {:.1f}'.format(m))
#print('Parabéns!' if m >= 6 else 'Estude mais!')
