#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int n = 10000; // Tamanho do array
    int arr1[n], arr2[n];
    clock_t start, end;
    double bubbleSortTime, insertionSortTime;

    // Preenchendo o array com números aleatórios
    for(int i = 0; i < n; i++) {
        arr1[i] = rand() % n;
        arr2[i] = arr1[i]; // Copiando os mesmos valores para arr2
    }

    // Medindo o tempo do Bubble Sort
    start = clock();
    bubbleSort(arr1, n);
    end = clock();
    bubbleSortTime = ((double) (end - start)) / CLOCKS_PER_SEC;

    // Medindo o tempo do Insertion Sort
    start = clock();
    insertionSort(arr2, n);
    end = clock();
    insertionSortTime = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Tempo gasto pelo Bubble Sort: %f segundos\n", bubbleSortTime);
    printf("Tempo gasto pelo Insertion Sort: %f segundos\n", insertionSortTime);

    return 0;
}
