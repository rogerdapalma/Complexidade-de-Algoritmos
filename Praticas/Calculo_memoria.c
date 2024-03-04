#include <stdio.h>

int multiplica(int a, int b) {
    return a * b;
}

int multiplica_alternativa(int a, int b) {
    int resultado = 0;
    for (int i = 0; i < b; i++) {
        resultado += a;
    }
    return resultado;
}

int main() {
    int a = 5;
    int b = 3;

    // Antes da instrução
    printf("Memória antes da instrução:\n");
    printf("Tamanho de int: %lu bytes\n", sizeof(int));
    printf("Memória ocupada por a e b: %lu bytes\n", 2 * sizeof(int));

    // Depois da instrução
    printf("\nMemória depois da instrução:\n");
    printf("Tamanho de int: %lu bytes\n", sizeof(int));
    printf("Memória ocupada por a, b, resultado e i: %lu bytes\n", 2 * sizeof(int) + 2 * sizeof(int));

    // Testando as funções
    printf("\nResultado da multiplicação usando a primeira função: %d\n", multiplica(a, b));
    printf("Resultado da multiplicação usando a segunda função: %d\n", multiplica_alternativa(a, b));

    return 0;
}
