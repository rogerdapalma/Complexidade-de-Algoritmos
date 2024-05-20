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
