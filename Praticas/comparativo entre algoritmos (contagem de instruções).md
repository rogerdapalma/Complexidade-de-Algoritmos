# Exercicio
Resolver o código abaixo, contando o numero de instruções conforme visto na aula gravada.


```java
public void terceiro(int controle) {
    int x=0;
    do {
        System.out.println((controle-x)%2);
        for(int y=0; (controle-x)>0; y++) {
            System.out.println((controle-y)%2);
        }
    } while(x<controle);
}
```

## resolvendo:

1. `public void terceiro(int controle) {` - Definição do método com um parâmetro `controle`.
2. `    int x=0;` - Inicialização da variável `x` com valor 0.
3. `    do {` - Início do laço `do-while`.
4. `        System.out.println((controle-x)%2);` - Impressão do resultado de `(controle-x)%2`.
5. `        for(int y=0; (controle-x)>0; y++) {` - Início do laço `for`, que executa enquanto `(controle-x)` for maior que 0.
6. `            System.out.println((controle-y)%2);` - Impressão do resultado de `(controle-y)%2`.
7. `        }` - Fim do laço `for`.
8. `    } while(x<controle);` - Condição do laço `do-while`, que continua enquanto `x` for menor que `controle`.
9. `}` - Fim do método.
