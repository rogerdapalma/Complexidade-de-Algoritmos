# Contagem de Instruções do Código em C

```c
#include <stdio.h>                           // 1: Instrução de pré-processamento para incluir a biblioteca padrão de entrada/saída

int main() {                                 // 2: Declaração da função principal
    int numero_secreto = 7;                  // 3: Declaração e inicialização da variável numero_secreto
    int tentativa;                           // 4: Declaração da variável tentativa

    // Laço do-while
    do {                                     // 5: Início do laço do-while
        printf("Adivinhe o numero secreto (entre 1 e 10): ");  // 6: Chamada de função para imprimir a mensagem
        scanf("%d", &tentativa);             // 7: Chamada de função para ler a tentativa do usuário

        if (tentativa != numero_secreto) {   // 8: Início da estrutura condicional if
            printf("Errado! Tente novamente.\n"); // 9: Chamada de função para imprimir a mensagem de erro
        }                                    // 10: Fim da estrutura condicional if

    } while (tentativa != numero_secreto);   // 11: Condição de continuação do laço do-while

    printf("Parabéns! Você adivinhou o número secreto.\n"); // 12: Chamada de função para imprimir a mensagem de sucesso

    return 0;                                // 13: Retorno da função principal
}
```
# Contagem das Instruções

Vamos definir \( N \) como o número de iterações do laço `do-while`.

1. `#include <stdio.h>`: Instrução de pré-processamento (1 instrução).
2. `int main() {`: Declaração da função principal (1 instrução).
3. `int numero_secreto = 7;`: Declaração e inicialização da variável `numero_secreto` (1 instrução).
4. `int tentativa;`: Declaração da variável `tentativa` (1 instrução).

**Dentro do laço `do-while`:**

5. `do {`: Início do laço `do-while` (1 instrução).
6. `printf("Adivinhe o numero secreto (entre 1 e 10): ");`: Chamada de função para imprimir a mensagem (N instruções).
7. `scanf("%d", &tentativa);`: Chamada de função para ler a tentativa do usuário (N instruções).
8. `if (tentativa != numero_secreto) {`: Início da estrutura condicional `if` (N instruções).
9. `printf("Errado! Tente novamente.\n");`: Chamada de função para imprimir a mensagem de erro (executada \( N-1 \) vezes, já que na última iteração a condição será falsa, resultando em \( N-1 \) instruções).
10. `}`: Fim da estrutura condicional `if` (N instruções).
11. `} while (tentativa != numero_secreto);`: Condição de continuação do laço `do-while` (N instruções).

**Fora do laço `do-while`:**

12. `printf("Parabéns! Você adivinhou o número secreto.\n");`: Chamada de função para imprimir a mensagem de sucesso (1 instrução).
13. `return 0;`: Retorno da função principal (1 instrução).

## Total de Instruções

- Instruções fora do laço `do-while`: 1 + 1 + 1 + 1 + 1 = 5
- Instruções dentro do laço `do-while`:
  - `printf("Adivinhe o numero secreto (entre 1 e 10): ");`: N
  - `scanf("%d", &tentativa);`: N
  - `if (tentativa != numero_secreto) {`: N
  - `printf("Errado! Tente novamente.\n");`: \( N-1 \)
  - `}`: N
  - `} while (tentativa != numero_secreto);`: N

Total: \( 5 + N + N + N + (N-1) + N + N + 1 + 1 = 7N + 7 \)

o código possui um total de \( 7N + 7 \) instruções, onde \( N \) é o número de iterações do laço `do-while`.