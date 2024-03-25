import numpy as np
import matplotlib.pyplot as plt
import time

# Tamanhos das matrizes quadradas
sizes = [5, 10, 50, 100, 500, 1000, 1500]

# Vetor
vector = np.random.rand(max(sizes))

# Tempo de execução para cada tamanho
execution_times = []

for size in sizes:
  # Matriz quadrada
  matrix = np.random.rand(size, size)

  # Medir o tempo de execução da multiplicação
  start_time = time.time()
  result = np.dot(vector[:size], matrix)
  end_time = time.time()

  # Adicionar o tempo de execução à lista
  execution_times.append(end_time - start_time)

  # Imprimir a matriz quadrada, o vetor, o resultado e o tempo de execução
#  print(f"Matriz quadrada para n = {size}:\n{matrix}\n")
#  print(f"Vetor para n = {size}:\n{vector[:size]}\n")
#  print(f"Resultado da multiplicação para n = {size}:\n{result}\n")
  print(
      f"Tempo de execução para n = {size}: {end_time - start_time} segundos\n")

# Gráfico
plt.plot(sizes, execution_times, marker='o')
plt.xlabel('Tamanho da Matriz (n)')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução da Multiplicação de Vetor por Matriz')
plt.grid(True)
plt.show()
