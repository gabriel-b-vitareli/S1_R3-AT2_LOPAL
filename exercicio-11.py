numero = int(input("Digite um número para visualizar sua tabuada: "))

print("-"*20,f"TABUADA DO {numero}","-"*20)
for c in range(11):
  print(f"{numero} × {c} = \033[32m{numero * c}\033[0m")
print("-"*55)
