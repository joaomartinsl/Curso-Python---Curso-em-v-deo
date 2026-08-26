'''para colocar uma cor no terminal: * \033[(style);(text);(back)m *
Style: 0 - None, 1 - Bold (Negrito), 4 - Underline, 7 - Negative (Inverte fundo e letra)
Text: 30 - Branco, 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - Magenta, 36 - Ciano, 37 - Cinza
Back: Mesma ordem do TEXT, mas ao invés de 30, é 40!'''
print('\033[7;37mTeste\033[m')
a = 2
b = 4
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m'.format(a, b))
nome = 'Janjão'
print('Olá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;32m', nome, '\033[m'))

# \033[m