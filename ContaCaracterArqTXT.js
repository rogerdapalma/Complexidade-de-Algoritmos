// Importando os módulos necessários
const fs = require("fs");
const { performance } = require("perf_hooks");

// Iniciando o contador de tempo
let tempoInicio = performance.now();

// Lendo o conteúdo do arquivo de forma síncrona
let texto = fs.readFileSync("texto_contagem.txt", "utf8");

// Variável de contagem de letras
let contagemLetras = {};

// Loop para percorrer o texto
for (let i = 0; i < texto.length; i++) {
  let letra = texto[i];
  // Verificar se a letra já existe no objeto contagemLetras
  if (contagemLetras[letra]) {
    contagemLetras[letra]++;
  } else {
    contagemLetras[letra] = 1;
  }
}

// Imprimir o resultado
console.log("Contagem de letras:");
for (let letra in contagemLetras) {
  console.log(`${letra}: ${contagemLetras[letra]}`);
}

// Finalizando o contador de tempo
let tempoFim = performance.now();

// Calculando e imprimindo o tempo total de execução
console.log(
  `Tempo de execução: ${(tempoFim - tempoInicio).toFixed(2)} milissegundos`,
);
console.log(
  `Tempo de execução: ${((tempoFim - tempoInicio) * 1000000).toFixed(
    2,
  )} nanosegundos`,
);
