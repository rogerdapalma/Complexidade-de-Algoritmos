#include <stdio.h>

int main(void) 
{
    int fib = 0, fib_next = 1; // Atribuição inicial
    int temp; // Declaração de variável

    printf("Sequência de Fibonacci até 1000:\n");

    while(fib <= 1000) // Loop até que fib seja maior que 1000
    { 
        printf("%d, ", fib); // Imprime o número atual de Fibonacci
        temp = fib + fib_next; // Calcula o próximo número de Fibonacci
        fib = fib_next; // Atualiza o número atual para o próximo na sequência
        fib_next = temp; // O próximo número é o calculado anteriormente
    }

    return 0;
}
//Atribuições: 2 (inicial) + 2 * n (dentro do loop) = 2 + 2n
//5n + 3