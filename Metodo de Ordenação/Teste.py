import random
import time
import matplotlib.pyplot as plt
import multiprocessing as mp

# Bubble Sort com contador de instruções
def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            counter += 1  # Conta cada comparação feita
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter += 3  # Conta as três operações de troca (swap)
    return counter

# Cocktail Sort com contador de instruções
def cocktail_sort(arr):
    n = len(arr)
    counter = 0
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            counter += 1  # Conta cada comparação
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                counter += 3  # Conta as três operações de troca (swap)
                swapped = True
        end -= 1
        if swapped:
            swapped = False
            for i in range(end, start, -1):
                counter += 1  # Conta cada comparação
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    counter += 3  # Conta as três operações de troca (swap)
                    swapped = True
            start += 1
    return counter

# Shell Sort com contador de instruções
def shell_sort(arr):
    n = len(arr)
    counter = 0
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            counter += 1  # Conta a operação de atribuição inicial
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                counter += 2  # Conta comparação e atribuição dentro do while
                j -= gap
            arr[j] = temp
            counter += 1  # Conta a atribuição final
        gap //= 2
    return counter

def test_sort(algorithm, arr):
    start_time = time.time()
    count = algorithm(arr.copy())
    elapsed_time = time.time() - start_time
    return elapsed_time, count

def test_sorting_algorithms(max_n):
    pool = mp.Pool(mp.cpu_count())
    times_bubble = []
    times_cocktail = []
    times_shell = []
    counters_bubble = []
    counters_cocktail = []
    counters_shell = []
    ns = list(range(1, max_n + 1, 500))

    big_list = [random.randint(1, 10000) for _ in range(max_n)]

    results_bubble = [pool.apply_async(test_sort, args=(bubble_sort, big_list[:n])) for n in ns if n <= 1500]  # Limitar Bubble Sort a 1500
    results_cocktail = [pool.apply_async(test_sort, args=(cocktail_sort, big_list[:n])) for n in ns if n <= 2000]  # Limitar Cocktail Sort a 2000
    results_shell = [pool.apply_async(test_sort, args=(shell_sort, big_list[:n])) for n in ns]

    for result in results_bubble:
        time, count = result.get()
        times_bubble.append(time)
        counters_bubble.append(count)

    for result in results_cocktail:
        time, count = result.get()
        times_cocktail.append(time)
        counters_cocktail.append(count)

    for result in results_shell:
        time, count = result.get()
        times_shell.append(time)
        counters_shell.append(count)

    pool.close()
    pool.join()

    plt.figure(figsize=(12, 12))
    plt.subplot(2, 1, 1)
    plt.plot(ns[:len(times_bubble)], times_bubble, label='Bubble Sort')
    plt.plot(ns[:len(times_cocktail)], times_cocktail, label='Cocktail Sort')
    plt.plot(ns, times_shell, label='Shell Sort')
    plt.xlabel('Tamanho da lista (N)')
    plt.ylabel('Tempo de execução (segundos)')
    plt.title('Tempo de Execução dos Algoritmos')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(ns[:len(counters_bubble)], counters_bubble, label='Bubble Sort')
    plt.plot(ns[:len(counters_cocktail)], counters_cocktail, label='Cocktail Sort')
    plt.plot(ns, counters_shell, label='Shell Sort')
    plt.xlabel('Tamanho da lista (N)')
    plt.ylabel('Contagem de Instruções')
    plt.title('Contagem de Instruções dos Algoritmos')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Solicitação de entrada do usuário
if __name__ == '__main__':
    user_input = int(input("Digite o valor máximo N para testar os algoritmos de ordenação: "))
    test_sorting_algorithms(user_input)
