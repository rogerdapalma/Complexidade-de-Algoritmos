import numpy as np
import matplotlib.pyplot as plt
import time


def opcao1():
  """
    Realiza a multiplicação de dois vetores de tamanho definido pelo usuário e
    exibe o resultado em um gráfico.
    """
  tam = int(input("Digite o tamanho dos vetores: "))
  v1 = np.random.randint(1, 11, tam)
  v2 = np.random.randint(1, 11, tam)
  result = v1 * v2
  print("Vetor 1:", v1)
  print("Vetor 2:", v2)
  print("Resultado da multiplicação:", result)
  plt.plot(result, marker='o', linestyle='-', color='b')
  plt.title('Resultado da Multiplicação dos Vetores')
  plt.xlabel('Índice')
  plt.ylabel('Valor')
  plt.grid(True)
  plt.show()


def opcao2():
  """
    Avalia o tempo de execução da multiplicação de um vetor por uma matriz de diferentes tamanhos
    e exibe os resultados em um gráfico.
    """
  sizes = [5, 10, 50, 100, 500, 1000, 1500]
  vector = np.random.rand(max(sizes))
  execution_times = []
  for size in sizes:
    matrix = np.random.rand(size, size)
    start_time = time.time()
    result = np.dot(vector[:size], matrix)
    end_time = time.time()
    execution_times.append(end_time - start_time)
    print(
        f"Tempo de execução para n = {size}: {end_time - start_time} segundos\n"
    )
  plt.plot(sizes, execution_times, marker='o')
  plt.xlabel('Tamanho da Matriz (n)')
  plt.ylabel('Tempo de Execução (s)')
  plt.title('Tempo de Execução da Multiplicação de Vetor por Matriz')
  plt.grid(True)
  plt.show()


def opcao3():
  """
    Realiza a multiplicação de matrizes de tamanhos especificados pelo usuário e exibe o
    resultado em gráficos.
    """
  tam_input = input("Insira os tamanhos das matrizes separados por espaço: ")
  tam = [int(n) for n in tam_input.split()]
  for n in tam:
    inicio = time.time()
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    X = np.dot(A, B)
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"Tamanho da matriz: {n}x{n}")
    print(f"Tempo de execução: {tempo_execucao} segundos")
    plt.matshow(X)
    plt.colorbar()
    plt.title(f"Gráfico da Matriz Resultante A * B (n={n})")
    plt.show()


opcoes = {1: opcao1, 2: opcao2, 3: opcao3}

while True:
  print("\nMenu de Opções:")
  print("1. Multiplicação de Vetores")
  print("2. Multiplicação de Vetor por Matriz e Tempo de Execução")
  print("3. Multiplicação de Matrizes e Gráfico Resultante")
  print("0. Sair")
  escolha = int(input("Escolha uma opção: "))

  if escolha == 0:
    break
  elif escolha in opcoes:
    opcoes[escolha]()
  else:
    print("Opção inválida!")
