# Complexidade de Algoritmos - Aula 03

**Professor:** Mirkos O. Martins  
**Email:** mirkos@ufn.edu.br

## Complexidade de Espaço

### Cálculo de Memória Utilizada por um Programa

- Quanto ocupa em memória uma variável?
- Quanto ocupa em memória uma instrução?

### Um Exemplo

Construa um programa que some dois valores inteiros recebendo-os como parâmetro e retorne o valor calculado.

- O valor de memória utilizado será sempre o mesmo?
- Existe dependência do tipo de linguagem utilizada para escrever o programa?

### Implementação SOMA

```c
int soma(int a, int b) {
    return a + b;
}

void main(void) {
    int x = soma(5, 10);
}
```
### Tipos de Utilização de Memória
- Declarações
- Atribuições
- Retornos de função
- Passagem de parâmetros
#### Exercício
- Faça um programa que retorne o maior valor em uma lista de números inteiros.

- Qual o tamanho de memória utilizado no programa?
Você consegue otimizar esse número?