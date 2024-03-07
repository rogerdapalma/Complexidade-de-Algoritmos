var mensagem = "Roger";
var numeroDeCaracteres = mensagem.length;
console.log(numeroDeCaracteres);

/*
 variavel 16 bits = 32 bits + TAM 80 bits
 instrução 16 bits = 48 bits
 Total bits = 160 bits
 ___________________________________________
| Variável            | Tipo               |
|---------------------|--------------------|
| mensagem            | string   +  TAM    |
| numeroDeCaracteres  | const              |             
| Instrução           | atribuição         |
|                     | chamada de método  |
|                     | impressão          |
 -------------------------------------------
*/
