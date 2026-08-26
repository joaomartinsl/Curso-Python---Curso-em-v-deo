from time import sleep
def helpi(foub):
    print(f"\033[0;32mPROCESSANDO FUNÇÃO/BIBLIOTECA {foub}...\033[m")
    sleep(1)
    print("\033[0;34m")
    help(foub)
    print("\033[m")
    sleep(1)

def personalizada(msg):
    print("\033[0;35m=\033[m" * (len(msg) + 2))
    print(f"\033[0;35m {msg} \033[m")
    print("\033[0;35m=\033[m" * (len(msg) + 2))

#Main
while True:
    personalizada("SISTEMA DE AJUDA PyHELP")
    foub = str(input("-> Função ou Biblioteca: "))
    if foub == 'fim':
        break
    helpi(foub)
print("\033[0;31mENCERRANDO...\033[m")
sleep(1)
print("\033[0;32mVolte sempre!\033[m")
