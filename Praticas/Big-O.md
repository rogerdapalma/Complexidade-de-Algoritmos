```c
#include <stdio.h>

// Função para calcular a soma dos elementos de um array
int somaArray(int arr[], int tamanho) {
    int soma = 0;
    for(int i = 0; i < tamanho; i++) {
        soma += arr[i];
    }
    return soma;
}

// Função para imprimir os elementos de um array
void imprimeArray(int arr[], int tamanho) {
    printf("Elementos do array: ");
    for(int i = 0; i < tamanho; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    // Declaração de um array e sua inicialização
    int numeros[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int tamanho = sizeof(numeros) / sizeof(numeros[0]);

    // Impressão dos elementos do array
    imprimeArray(numeros, tamanho);

    // Cálculo da soma dos elementos do array
    int soma = somaArray(numeros, tamanho);

    // Impressão da soma dos elementos do array
    printf("Soma dos elementos do array: %d\n", soma);

    return 0;
}
````
#
## Função: `somaArray`

````c
int somaArray(int arr[], int tamanho) {
    int soma = 0; // O(1)
    for(int i = 0; i < tamanho; i++) { // O(n)
        soma += arr[i]; // O(1)
    }
    return soma; // O(1)

    //TOTAL : O(N)
}
````
#
##  Função `imprimeArray`

````c
void imprimeArray(int arr[], int tamanho) {
    printf("Elementos do array: "); // O(1)
    for(int i = 0; i < tamanho; i++) { // O(n)
        printf("%d ", arr[i]); // O(1)
    }
    printf("\n"); // O(1)

    //TOTAL : O(N)
}
````
#
## Função `main`

```c
int main() {
    int numeros[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // O(1)
    int tamanho = sizeof(numeros) / sizeof(numeros[0]); // O(1)

    imprimeArray(numeros, tamanho); // O(n)

    int soma = somaArray(numeros, tamanho); // O(n)

    printf("Soma dos elementos do array: %d\n", soma); // O(1)

    return 0; // O(1)

    //TOTAL : O(N) + O(n) = O(n)
}
```
## Complexidade Total:

````
O(n)+O(n)=O(n)
````

