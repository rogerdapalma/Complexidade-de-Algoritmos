import time
import matplotlib.pyplot as plt
import numpy as np

# Instruções: 4N^3 + 6N^2 + 4N + 4
def shell_sort(arr):
    n = len(arr)
    steps = 2
    gap = n // 2
    steps += 1
    while gap > 0:
        steps += 1  # while gap > 0
        for i in range(gap, n):
            steps += 2  # for loop start and comparison
            temp = arr[i]
            steps += 1
            j = i
            steps += 1
            while j >= gap and arr[j - gap] > temp:
                steps += 3  # while loop comparison, arr[j-gap], arr[j]
                arr[j] = arr[j - gap]
                steps += 1
                j -= gap
                steps += 1
            arr[j] = temp
            steps += 1
        gap //= 2
        steps += 1
    return steps

# Instruções: 4N^2 + 3N + 2
def bubble_sort(arr):
    n = len(arr)
    steps = 1
    for i in range(n):
        steps += 2  # for loop start and comparison
        for j in range(0, n - i - 1):
            steps += 3  # for loop start, comparison, n-i-1 calculation
            if arr[j] > arr[j + 1]:
                steps += 1  # if comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps += 2
    return steps

# Instruções: 10N^2 + 10N + 6
def shaker_sort(arr):
    n = len(arr)
    steps = 5
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        steps += 1  # while swapped
        swapped = False
        steps += 1
        for i in range(start, end):
            steps += 2  # for loop start and comparison
            if arr[i] > arr[i + 1]:
                steps += 1  # if comparison
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                steps += 2
                swapped = True
                steps += 1
        if not swapped:
            steps += 1  # if not swapped
            break
        swapped = False
        steps += 1
        end -= 1
        steps += 1
        for i in range(end - 1, start - 1, -1):
            steps += 3  # for loop start, comparison, and decrement
            if arr[i] > arr[i + 1]:
                steps += 1  # if comparison
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                steps += 2
                swapped = True
                steps += 1
        start += 1
        steps += 1
    return steps

# Instruções: 4N^2 + 6N + 3
def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        steps += 3  # for loop start, comparison, and increment
        key = arr[i]
        steps += 1
        j = i - 1
        steps += 1
        while j >= 0 and key < arr[j]:
            steps += 3  # while loop comparison, key, and arr[j]
            arr[j + 1] = arr[j]
            steps += 1
            j -= 1
            steps += 1
        arr[j + 1] = key
        steps += 1
    return steps

def measure_time_and_steps(sort_func, arr):
    start_time = time.time()
    steps = sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time, steps

# Parameters
array_sizes = [100, 200, 500, 1000]
repeats = 3

# Results storage
shellsort_times = []
bubblesort_times = []
shakersort_times = []
insertionsort_times = []

shellsort_steps = []
bubblesort_steps = []
shakersort_steps = []
insertionsort_steps = []

# Measure performance
for size in array_sizes:
    shellsort_time, shellsort_step = np.mean([
        measure_time_and_steps(shell_sort, np.random.randint(0, size, size))
        for _ in range(repeats)
    ], axis=0)
    bubblesort_time, bubblesort_step = np.mean([
        measure_time_and_steps(bubble_sort, np.random.randint(0, size, size))
        for _ in range(repeats)
    ], axis=0)
    shakersort_time, shakersort_step = np.mean([
        measure_time_and_steps(shaker_sort, np.random.randint(0, size, size))
        for _ in range(repeats)
    ], axis=0)
    insertionsort_time, insertionsort_step = np.mean([
        measure_time_and_steps(insertion_sort, np.random.randint(0, size, size))
        for _ in range(repeats)
    ], axis=0)

    shellsort_times.append(shellsort_time)
    bubblesort_times.append(bubblesort_time)
    shakersort_times.append(shakersort_time)
    insertionsort_times.append(insertionsort_time)

    shellsort_steps.append(shellsort_step)
    bubblesort_steps.append(bubblesort_step)
    shakersort_steps.append(shakersort_step)
    insertionsort_steps.append(insertionsort_step)

# Plotting Time
plt.figure(figsize=(12, 8))
plt.plot(array_sizes, shellsort_times, label='Shellsort', marker='o')
plt.plot(array_sizes, bubblesort_times, label='Bubblesort', marker='o')
plt.plot(array_sizes, shakersort_times, label='Shakersort', marker='o')
plt.plot(array_sizes, insertionsort_times, label='Insertionsort', marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithms Performance Comparison (Time)')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.xscale('log')
plt.show()

# Plotting Steps
plt.figure(figsize=(12, 8))
plt.plot(array_sizes, shellsort_steps, label='Shellsort', marker='o')
plt.plot(array_sizes, bubblesort_steps, label='Bubblesort', marker='o')
plt.plot(array_sizes, shakersort_steps, label='Shakersort', marker='o')
plt.plot(array_sizes, insertionsort_steps, label='Insertionsort', marker='o')
plt.xlabel('Array Size')
plt.ylabel('Number of Steps')
plt.title('Sorting Algorithms Performance Comparison (Steps)')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.xscale('log')
plt.show()
