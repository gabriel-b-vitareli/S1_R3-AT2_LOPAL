numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"\033[1;31m{numero} não é um número primo.")
else:
    quantidade_divisores = 0

    for c in range(1, numero + 1):
        if numero % c == 0:
            quantidade_divisores += 1

    if quantidade_divisores == 2:
        print(f"\033[1;32m{numero} é um número primo!")
    else:
        print(f"\033[1;31m{numero} não é um número primo.")
