try:
    n = int(input("Digite o numerador: "))
    d = int(input("Digite o denominador: "))
    r = n / d
except (TypeError, ValueError):
    print("Infelizmente tivemos um problema com o tipo de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
else:
    print(f"O resultado da divisão deu {r}.")
finally:
    print("Volte sempre, muito obrigado!")