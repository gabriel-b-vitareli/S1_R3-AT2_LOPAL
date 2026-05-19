# S1_R3 - AT2 LOPAL — Lógica de Programação em Python

Documentação dos 11 exercícios da atividade **S1_R3**, escritos em Python e executados no Google Colab.

---

## Índice

1. [Pares e Ímpares](#1-pares-e-ímpares) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-1.py)
2. [Maior e Menor](#2-maior-e-menor) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-2.py)
3. [Letras do Nome](#3-letras-do-nome) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-3.py)
4. [Sequência de Fibonacci](#4-sequência-de-fibonacci) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-4.py)
5. [Validação de Dados](#5-validação-de-dados) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-5.py)
6. [Número Primo](#6-número-primo) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-6.py)
7. [Fatorial](#7-fatorial) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-7.py)
8. [Operações com Lista](#8-operações-com-lista) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-8.py)
9. [Cardápio com Dicionário](#9-cardápio-com-dicionário) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-9.py)
10. [Sistema de Senha](#10-sistema-de-senha) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-10.py)
11. [Tabuada](#11-tabuada) - [Arquivo](https://github.com/gabriel-b-vitareli/S1_R3-AT2_LOPAL/blob/main/exercicio-11.py)

---

## 1. Pares e Ímpares

Percorre todos os números de 0 a 100 e classifica cada um como par ou ímpar. Números pares aparecem em verde no terminal, e ímpares em vermelho — isso é feito com **códigos de escape ANSI** (`\033[32m` para verde, `\033[31m` para vermelho).

A lógica principal usa o operador `%` (módulo), que retorna o resto de uma divisão. Se o resto de `c / 2` for zero, o número é par.

```python
for c in range(0, 101):
  if c % 2 == 0:
    print("\033[32m", c, " PAR")
  else:
    print("\033[31m", c, " ÍMPAR")
```

**Conceitos:** `for`, `if/else`, operador módulo, escape ANSI

---

## 2. Maior e Menor

Pede ao usuário que digite três números, guarda em uma lista e usa o método `.sort()` para ordenar em ordem crescente. Depois, é só pegar o índice `0` para o menor e o índice `2` para o maior.

```python
lista = []
for c in range(3):
  lista.append(int(input("Digite um valor: ")))

lista.sort()

print(f"O maior número da lista é {lista[2]}, enquanto o menor é {lista[0]}.")
```

**Conceitos:** `for`, lista, `.append()`, `.sort()`, `input`, f-string

---

## 3. Letras do Nome

Recebe um nome, remove espaços extras com `.strip()` e converte para maiúsculas com `.upper()`. Em seguida, vai adicionando uma letra por vez em outra lista e imprimindo o estado atual — o efeito é o nome sendo revelado progressivamente, letra a letra.

```python
nome = input('Digite seu nome: ')
nome = nome.strip().upper()
listaNome = []
for c in range(len(nome)):
  listaNome.append(nome[c])
  print(*listaNome)
```

> O `*listaNome` dentro do `print` desempacota a lista, imprimindo os elementos separados por espaço em vez de mostrar os colchetes.

**Conceitos:** `for`, lista, `len()`, string methods, desempacotamento com `*`

---

## 4. Sequência de Fibonacci

Gera os primeiros N termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8...), onde cada número é a soma dos dois anteriores. O truque está na troca de variáveis em uma única linha: `a, b = b, a + b`.

```python
n = int(input("Digite quantos valores da sequência de Fibonacci você quer: "))
serie = []
a, b = 0, 1
for c in range(n):
  serie.append(a)
  a, b = b, a + b
print(*serie)
```

**Conceitos:** `for`, lista, swap de variáveis, `input`

---

## 5. Validação de Dados

Coleta cinco informações do usuário (nome, idade, salário, sexo e estado civil) e valida cada uma individualmente. Se qualquer campo estiver errado, o programa pede a correção daquele campo específico e repete o ciclo.

A variável `valido` funciona como uma **flag booleana**: começa como `True` no início de cada iteração e vai para `False` se qualquer erro for encontrado. O loop só encerra com `break` quando a flag chega ao final ainda como `True`.

```python
while True:
    valido = True

    if len(nome) <= 3:
        print("Seu nome precisa ter mais que três caracteres.")
        nome = input("Digite seu nome novamente: ")
        valido = False

    # ... demais validações ...

    if valido:
        break
```

**Conceitos:** `while`, flag booleana, `break`, `input`, string methods

---

## 6. Número Primo

Verifica se um número é primo contando quantos divisores ele tem. Um número primo tem exatamente dois divisores: 1 e ele mesmo. O programa percorre todos os números de 1 até N e conta quantos dividem N sem deixar resto.

```python
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
```

> Números menores ou iguais a 1 são descartados logo no início, já que por definição não são primos.

**Conceitos:** `for`, contador, operador módulo, `if/else`, escape ANSI

---

## 7. Fatorial

Calcula o fatorial de um número (ex: `5! = 5 × 4 × 3 × 2 × 1 = 120`). Começa com `fatorial = 1` e vai multiplicando pelo valor de `c` a cada volta do loop, de 1 até N.

```python
numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

for c in range(1, numero + 1):
    fatorial *= c

print(f"O fatorial de {numero}! é {fatorial}")
```

**Conceitos:** `for`, acumulador com `*=`, `input`, f-string

---

## 8. Operações com Lista

Trabalha com uma lista pré-definida de números e extrai várias informações: tamanho, maior valor, menor valor, soma e as versões ordenadas (crescente e decrescente).

```python
L = [5, 7, 2, 9, 4, 1, 3]
L.sort()

tamanho    = len(L)
maior      = L[6]
menor      = L[0]
soma       = sum(L)
decrescente = sorted(L, reverse=True)
```

> Depois de ordenar com `.sort()`, o menor número sempre está no índice `0` e o maior no último. `sorted()` com `reverse=True` retorna uma nova lista sem modificar a original.

**Conceitos:** lista, `.sort()`, `sorted()`, `len()`, `sum()`, indexação

---

## 9. Cardápio com Dicionário

Cria um dicionário representando o cardápio anexado na atividade. Em Python, dicionários armazenam pares de **chave → valor**, aqui, o nome do produto é a chave e o preço é o valor.

```python
lanchonete = {
    "salgado":     4.5,
    "lanche":      6.5,
    "suco":        3,
    "refrigerante":3.5,
    "doce":        1
}

print(lanchonete)
```
<img width="314" height="175" alt="image" src="https://github.com/user-attachments/assets/8c04662f-5404-4626-8b97-c60c2ebfa0d8" />


**Conceitos:** dicionário, pares chave-valor

---

## 10. Sistema de Senha

Simula um sistema de autenticação simples. A senha correta está definida no código e o programa fica pedindo a entrada do usuário em loop até que ele acerte. Quando a senha está correta, exibe uma mensagem de acesso liberado em verde.

```python
senha = "676767"

userInput = input("Digite a senha: ")

while userInput != senha:
  userInput = input(f"Senha incorreta. Tente novamente: ")

print("\033[32mAcesso liberado!")
```

> O loop `while` continua enquanto a condição for verdadeira. Ele encerra automaticamente assim que o input do usuário bate com a senha armazenada.

**Conceitos:** `while`, comparação de strings, `input`, escape ANSI

---

## 11. Tabuada

Recebe um número e imprime a tabuada completa, de 0 a 10, com um cabeçalho formatado e separadores visuais. Os resultados de cada multiplicação aparecem em verde, com reset de cor ao final de cada linha.

```python
numero = int(input("Digite um número para visualizar sua tabuada: "))

print("-"*20, f"TABUADA DO {numero}", "-"*20)
for c in range(11):
  print(f"{numero} × {c} = \033[32m{numero * c}\033[0m")
print("-"*55)
```

> `"-" * 20` é uma forma pythônica de repetir uma string — cria uma linha de 20 traços sem precisar digitá-los um a um.

**Conceitos:** `for`, `input`, f-string, repetição de string, escape ANSI

---

*S1_R3 · AT2_LOPAL · Lógica de Programação em Python*

*OBS: A explicação foi feita manualmente, a estilização do README com Markdown foi feito com assistência de IA*
