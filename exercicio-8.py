L = [5, 7, 2, 9, 4, 1, 3]
L.sort()

tamanho = len(L)
maior = L[6]
menor = L[0]
soma = sum(L)
decrescente = sorted(L, reverse=True)

print(f"O tamanho da lista é de {tamanho} caracteres.")
print(f"O maior número da lista é {maior}.")
print(f"O menor número da lista é {menor}.")
print(f"A soma entre os números da lista resulta em {soma}.")
print(f"Em ordem crescente, a lista fica: {L}")
print(f"Em ordem decrescente, a lista fica: {decrescente}.")