lista = []
for c in range(3):
  lista.append(int(input("Digite um valor: ")))

lista.sort()

print(f"O maior número da lista é {lista[2]}, enquanto o menor é {lista[0]}.")