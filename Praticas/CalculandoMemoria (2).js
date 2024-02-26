function printMemoryUsage(label) {
  const used = process.memoryUsage();
  console.log(`${label}:`);
  for (let key in used) {
    console.log(
      `  ${key}: ${Math.round((used[key] / 1024 / 1024) * 100) / 100} MB`,
    );
  }
}

// Medindo o uso de memória do programa
printMemoryUsage("Uso de memória inicial");

// Declaração de uma variável
const largeArray = new Array(1000000).fill("string");
printMemoryUsage("Após declaração de largeArray");

// Executando uma instrução
let sum = 0;
for (let i = 0; i < 1000000; i++) {
  sum += i;
}
printMemoryUsage("Após execução do loop");

// Função exemplo
function somarDoisValores(valor1, valor2) {
  return valor1 + valor2;
}

const resultado = somarDoisValores(5, 3);
console.log(`Resultado da soma: ${resultado}`);
printMemoryUsage("Após a função somarDoisValores");


