n = int(input("Digite quantos valores da sequência de Fibonacci você quer: "))
serie = []
a, b = 0, 1
for c in range(n):
  serie.append(a)
  a, b = b, a + b
print(*serie)
