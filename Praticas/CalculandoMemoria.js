// Função para calcular a soma
function soma(n1 = 0, n2 = 0) {
    return n1 + n2;
}

// Função para estimar o tamanho de uma variável em bytes
function estimatedSizeOf(variable) {
    const serializedVariable = JSON.stringify(variable);
    return Buffer.byteLength(serializedVariable, 'utf8');
}

// Função para medir o uso de memória antes e depois de uma operação
function measureMemoryUsage(operation, ...args) {
    const before = process.memoryUsage().heapUsed;
    operation(...args);
    const after = process.memoryUsage().heapUsed;
    return after - before; // Diferença no uso de memória em bytes
}

// Uso da função e medição da memória
console.log(`Resultado da soma: ${soma(2, 5)}`);

const memoryUsedBySoma = measureMemoryUsage(soma, 2, 5);
console.log(`Memória adicional utilizada pela função soma: ${memoryUsedBySoma} bytes`);

const variable = soma(2, 5);
const sizeOfVariable = estimatedSizeOf(variable);
console.log(`Tamanho estimado da variável (resultado da soma): ${sizeOfVariable} bytes`);

// Nota sobre a medição da memória usada por uma instrução
console.log("Medir a memória usada por uma instrução específica não é diretamente suportado em JavaScript devido à abstração da linguagem e ao gerenciamento de memória pelo ambiente de execução.");
