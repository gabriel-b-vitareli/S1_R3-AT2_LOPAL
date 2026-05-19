nome = input('Digite seu nome: ')
nome = nome.strip().upper()
listaNome = []
for c in range(len(nome)):
  listaNome.append(nome[c])
  print(*listaNome)
