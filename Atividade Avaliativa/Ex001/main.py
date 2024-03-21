import numpy as np
import matplotlib.pyplot as plt

# Solicitando ao usuário que escolha o tamanho dos vetores
tam = int(input("Digite o tamanho dos vetores: "))

# Gerando vetores de tamanho definido com valores aleatórios
v1 = np.random.randint(1, 11, tam)  # Valores aleatórios entre 1 e 10
v2 = np.random.randint(1, 11, tam)

# Multiplicando os vetores elemento a elemento
result = v1 * v2

# Imprimindo os vetores e o resultado
print("Vetor 1:", v1)
print("Vetor 2:", v2)
print("Resultado da multiplicação:", result)

# Gerando o gráfico
plt.plot(result, marker='o', linestyle='-', color='b')
plt.title('Resultado da Multiplicação dos Vetores')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
