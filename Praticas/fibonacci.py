p1 = 0
p2 = 1


def fibonacci(v1):
  if v1 > 0:
    global p1, p2
    n = p1 + p2
    print(n)
    p1 = p2
    p2 = n
    fibonacci(v1 - 1)
  else:
    return 0


quantidade = input('digite a quantidade de valores da serie:')
quantidade = int(quantidade)  #converte para inteiro
print(p1)
print(p2)
fibonacci(quantidade - 2)
