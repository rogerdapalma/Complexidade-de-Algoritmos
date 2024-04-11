# Regras:

## 1ªRegra: Calcular o laço mais interno;
```C
for no C:
N--> (1*I)+(N+1)*C+(NIn)+N+Bloco
```
NIn = N * (numero de incremento e decrementos)
### Inicialização + (Condição+1) + incremento/decremento
```C
for(i=0;i=j;i>m && j<100;i++,j++,k--){}

(1*2)+(N+1)*2)+(N*3)+(N*3)  
2+2N+2+3N+3N  
8N+4 
```


Laço em C do Google Sorte  
For_Interno
```c
if(vetor[j] > vetor[j+1]){
    aux = vetor[j];
    vetor[j] = vetor[j+1]
    vetor[j+1] = aux;
}
# Bloco possui 6 Instruções:
# 1+N+1+N+6N  
# 8N+2  
``` 
For_Externo:
```c
for(k=1;k<n;k++>) {
    printf("\n[%d] ",k);
    for(j=0;j < n-1; j++){
        if(vetor[j] > vetor[j+1]){
            aux = vetor[j];
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux;
        }
    }
}
# 1+N+1+N+N(Bloco)
# Bloco=2+8N+2
# Bloco8N+4
# 2N+2+N(8N+4)
# 2N+2+8N^2+4N
# Bubble = 8N^2+6N+2
```
###### https://www.sortvisualizer.com/

### Exercicio comparar Inster Sort com o Bulle Sort

```c
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

```

### Professor - Insertion Sort

```c
 void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = - 1;
        }
        arr[j + 1] = key;
    }
}

While = (N+1)(Comparação)+N(Bloco)
4N+2

Bloco:2+4N+2+1 = 4N+5
For:1+N+1+N+N(4N+5) = 4N²+7N+2

)
```