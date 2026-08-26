nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média final foi {:.1f}.'.format(media))
if media >= 7.0:
    print('\033[1;32mPARABÉNS\033[m, com a sua média, você foi \033[1;32mAPROVADO\033[m.')
elif 7.0 > media >= 5.0:
    print('\033[1;31mATENÇÃO!\033[m Sua média final não atingiu o limite para ser aprovado, portanto você está em \033[1;31mRECUPERAÇÃO\033[m.')
elif media < 5.0:
    print('\033[1;31mATENÇÃO!\033[m Sua média foi muito abaixo do limite para ser aprovado, portanto você está \033[1;31mREPROVADO\033[m.')
print('Tenha um ótimo dia!')
