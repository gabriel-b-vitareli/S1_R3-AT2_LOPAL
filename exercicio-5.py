nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo (F/M): ")
estadoCivil = input("Qual seu estado civil? (S/C/V/D): ")

while True:
    valido = True

    if len(nome) <= 3:
        print("Seu nome precisa ter mais que três caracteres.")
        nome = input("Digite seu nome novamente: ")
        valido = False

    if idade < 0 or idade > 150:
        print("Sua idade precisa estar entre 0 e 150.")
        idade = int(input("Digite sua idade novamente: "))
        valido = False

    if salario <= 0:
        print("Seu salário precisa ser maior que zero.")
        salario = float(input("Digite seu salário novamente: "))
        valido = False

    if sexo.lower() != "f" and sexo.lower() != "m":
        print("Sexo inválido. Tente novamente com 'F' ou 'M'.")
        sexo = input("Digite seu sexo novamente: ")
        valido = False

    if estadoCivil.lower() not in ['s', 'c', 'v', 'd']:
        print("Estado civil inválido. Tente novamente com 'S', 'C', 'V' ou 'D'.")
        estadoCivil = input("Digite seu estado civil novamente: ")
        valido = False

    if valido:
        break

print("Tudo certo.")