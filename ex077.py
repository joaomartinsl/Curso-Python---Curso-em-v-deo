palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'LINGUAGEM', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nAs vogais da palavra {p} são: ', end='')
    for c in range(0, len(p)):
        if p[c] in 'AEIOU':
            print(p[c], end=' ')
