expressao = str(input('Digite uma expressão: '))
parenteses = []
for simb in expressao:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Expressão está válida!')
else:
    print('Expressão inválida!')