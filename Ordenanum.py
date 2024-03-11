
import random

def sort_base_ruto(arr):
    n = len(arr)  # Determina o tamanho da lista
    trocas = 0  # Inicializa o contador de trocas realizadas durante a ordenação

    # Percorre todos os elementos da lista
    for i in range(n):
        min_idx = i  # Assume que o elemento atual é o menor

        # Procura pelo menor elemento na parte restante não ordenada da lista
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Atualiza o índice do menor elemento encontrado

        # Se o menor elemento não é o elemento atual, realiza a troca
        if min_idx != i:
            print(f"Troca: {arr[i]} <-> {arr[min_idx]}")  # Imprime a troca
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Troca os elementos
            trocas += 1  # Incrementa o contador de trocas

    return trocas  # Retorna o número total de trocas realizadas

# Gera uma lista de números aleatórios com 100.000 elementos
num_elementos = 100000
lista_aleatoria = [random.randint(0, 1000000) for _ in range(num_elementos)]

# Imprime a lista antes da ordenação
print("Lista antes da ordenação:", lista_aleatoria)

# Ordena a lista usando o Selection Sort e conta as trocas
num_trocas = sort_base_ruto(lista_aleatoria)

# Imprime a lista após a ordenação e o número total de trocas realizadas
print("Lista após a ordenação:", lista_aleatoria)
print("Número de trocas realizadas:", num_trocas)
