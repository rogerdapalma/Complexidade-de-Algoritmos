import numpy as np
import matplotlib.pyplot as plt
import time

# Pede ao usuário para inserir os tamanhos das matrizes separados por espaço
tam_input = input("Insira os tamanhos das matrizes separados por espaço: ")
tam = [int(n) for n in tam_input.split()]

# Itera sobre os diferentes tamanhos
for n in tam:
  # Marca o tempo de início
  inicio = time.time()

  # Cria duas matrizes quadradas aleatórias
  A = np.random.rand(n, n)
  B = np.random.rand(n, n)

  # Multiplica as duas matrizes
  X = np.dot(A, B)

  # Marca o tempo de término
  fim = time.time()

  # Calcula o tempo de execução
  tempo_execucao = fim - inicio

  # Imprime os resultados
  print(f"Tamanho da matriz: {n}x{n}")
  print(f"Tempo de execução: {tempo_execucao} segundos")

  # Gera o gráfico para a matriz resultante
  plt.matshow(X)
  plt.colorbar()
  plt.title(f"Gráfico da Matriz Resultante A * B (n={n})")
  plt.show()
