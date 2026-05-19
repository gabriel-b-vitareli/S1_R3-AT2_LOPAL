for c in range(0,101):
  if c % 2 == 0:
    print("\033[32m", c, " PAR")
  else:
    print("\033[31m", c, " ÍMPAR")