numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

for c in range(1, numero + 1):
    fatorial *= c

print(f"O fatorial de {numero}! é {fatorial}")
