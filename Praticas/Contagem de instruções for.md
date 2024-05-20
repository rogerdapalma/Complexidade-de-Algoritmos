```java
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {

    int[] lista = { 3, 5, 7, 10, 6, }; // 1 instrução

    // Chama o método para inverter o array
    invertArray(lista); // 1 instrução

    System.out.println("lista invertida: " + Arrays.toString(lista)); // 1 instrução
  }

  public static void invertArray(int[] array) {
    int size = array.length; // 1 instrução
    for (int i = 0; i < size / 2; i++) { // 1 + N/2 instruções

      int temp = array[i]; // N/2 instruções
      array[i] = array[size - 1 - i]; // N/2 instruções
      array[size - 1 - i] = temp; // N/2 instruções
    }
  }
}
```

```java
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {

    int[] lista = { 3, 5, 7, 10, 6 }; // 1

    // Chama o método para inverter o array
    invertArray(lista); // 1

    System.out.println("lista invertida: " + Arrays.toString(lista)); // 1
  }

  public static void invertArray(int[] array) {
    int size = array.length; // 1
    for (int i = 0; i < size / 2; i++) { // 1 + N/2 (o loop executa N/2 vezes)

      int temp = array[i]; // N/2
      array[i] = array[size - 1 - i]; // N/2
      array[size - 1 - i] = temp; // N/2
    }
  }
}
// total 3 + 1 + (3 * N/2) = 4 + (3/2)N
```
## Método Main:

- `int[] lista = { 3, 5, 7, 10, 6 };` : 1 instrução
- `invertArray(lista);` : 1 instrução
- `System.out.println("lista invertida: " + Arrays.toString(lista));` : 1 instrução
- **Total para o método main:** 3 instruções

## Método invertArray:

- `int size = array.length;` : 1 instrução
- `for (int i = 0; i < size / 2; i++) {` : 1 instrução (loop executado N/2 vezes)
  - Dentro do loop (cada uma executada N/2 vezes):
    - `int temp = array[i];` : N/2 instruções
    - `array[i] = array[ size - 1 - i ];` : N/2 instruções
    - `array[size - 1 - i] = temp;` : N/2 instruções
- **Total para o invertArray:** 1 + 1 (inicialização do loop) + 3*(N/2) = 2 + 3N/2 instruções

## Contagem Total de Instruções

- **Método Main:** 3 instruções
- **Método invertArray:** 2 + 3N/2 instruções

## Combinando ambos:

- **Total de instruções = 3 + 2 + 3N/2 = 5 + 3N/2**

Número total de instruções no código fornecido é 5 + 3N/2, onde N é o comprimento do array.

```java
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {

    int[] lista = { 3, 5, 7, 10, 6 }; // 1

    // Chama o método para inverter o array
    invertArray(lista); // 1

    System.out.println("Lista invertida: " + Arrays.toString(lista)); // 1

    // Chama o método para encontrar o maior número
    int maiorNumero = findMax(lista); // 1
    System.out.println("Maior número: " + maiorNumero); // 1
  }

  public static void invertArray(int[] array) {
    int size = array.length; // 1
    for (int i = 0; i < size / 2; i++) { // 1 + N (o loop executa N/2 vezes)

      int temp = array[i]; // N
      array[i] = array[size - 1 - i]; // N
      array[size - 1 - i] = temp; // N
    }
  }

  public static int findMax(int[] array) {
    int max = array[0]; // 1
    for (int i = 1; i < array.length; i++) { // 1 + N-1 (o loop executa N-1 vezes)
      if (array[i] > max) { // N-1
        max = array[i]; // K (K é o número de vezes que o máximo é atualizado)
      }
    }
    return max; // 1
  }
}
// total 3 + 1 + (3 * N) + 1 + 1 + (N - 1) + (N - 1) + K = 6 + 3N + 2N - 2 + K =
// 6 + 7N - 2 + K = 4 + 7N + K
```
## A contagem de operações adicionais para encontrar o maior número é:

- int max = array[0]; conta como 1 operação.
- O loop for (int i = 1; i < array.length; i++) executa N-1 vezes.
### Dentro do loop:
- if (array[i] > max) executa N-1 vezes.
- max = array[i]; executa K vezes, onde K é o número de vezes que o valor máximo é atualizado.
- Portanto, a contagem total de operações com o método findMax é:

- Operações fora do loop: 1 (inicialização do máximo) + 1 (retorno do máximo).
- Operações dentro do loop: (N-1) para a condição do if + K para a atualização do máximo.
- Então, a contagem total ajustada é:


- total 3 + 1 + (3 * N) + 1 + 1 + (N - 1) + (N - 1) + K = 6 + 3N + 2N - 2 + K = 6 + 7N - 2 + K = 4 + 7N + K


- Isso inclui todas as operações de ambos os métodos (invertArray e findMax).

