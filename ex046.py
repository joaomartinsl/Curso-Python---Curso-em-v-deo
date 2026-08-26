from time import sleep
for c in range(10, 0, -1):
    if c == 3 or c == 2 or c == 1:
        print('\033[1;31m{}\033[m'.format(c))
        sleep(1)
    else:
        print(c)
        sleep(1)
print('\033[1;31m{}\033[m'.format(0))
print('BOOM! POW! POW! FELIZ ANO NOVOOOO!')
