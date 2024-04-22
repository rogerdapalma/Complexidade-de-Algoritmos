def fibonacci(n):
  if n == 0 or n == 1:
      return n
  else:
      return fibonacci(n-1) + fibonacci(n-2)

def main():
  print("Obter sequência de Fibonacci")
  num = int(input("Entre com um número: "))

  print(f"{num}º fibonacci: {fibonacci(num)}\n")

  print("Mostrar a sequência completa:")
  for i in range(num):
      print(fibonacci(i), end=" ")

if __name__ == "__main__":
  main()
