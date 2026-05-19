senha = "676767"

userInput = input("Digite a senha: ")

while userInput != senha:
  userInput = input(f"Senha incorreta. Tente novamente: ")

print("\033[32mAcesso liberado!")