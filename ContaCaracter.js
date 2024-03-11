// Importando a função performance
const { performance } = require("perf_hooks");

// Iniciando o contador de tempo
let tempoInicio = performance.now();

// Definindo o texto
let texto = `Um retrato das mulheres na pesquisa
Assessoria de Comunicação (ASSECOM) em 08/03/2024


Com objetivo de compreender como ocorreu a inserção de mulheres em organizações de pesquisa, com ênfase em suas trajetórias profissionais e tecnológicas, foi realizado o estudo ‘Mulheres nas ciências: análise da inserção e das trajetórias de cientistas em instituições de pesquisa (Rio Grande do Sul, 1950-1960)’. A pesquisa iniciou no ano de 2023, através da pesquisadora e docente da Universidade Franciscana, Daiane Silveira Rossi. 

A apuração priorizou um recorte temporal, o qual define as décadas de 1950 e 1960 como um marco inicial na produção científica, que corresponde também à década de criação da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) e do Conselho Nacional de Pesquisas (CNPq), sendo ambos tratados como símbolos da institucionalização das ciências no Brasil. Para Daiane, “a ideia de trabalhar com a temática de mulheres na ciência surgiu a partir da oportunidade de trabalhar no projeto já em andamento na época sobre ‘Mulheres na Fiocruz’. Com a oportunidade de vir trabalhar em Santa Maria, na UFN, resolvi também migrar a pesquisa, ou melhor, ampliá-la para o Rio Grande do Sul”. 

A pesquisa ressalta o contexto do processo de institucionalização e profissionalização das ciências no Brasil entre as mesmas décadas, que coincidiu com a ampliação do acesso de homens e mulheres ao ensino superior, cujo resultado foi o acentuado aumento do número de matriculados nesse nível de ensino. Essa ampliação do acesso à educação se deu a partir da criação das Faculdades de Filosofia no país. 


“A partir das Faculdades de Filosofia temos o ingresso em cursos como: Pedagogia, Letras, História, Geografia, Ciências Sociais, Matemática, Física, Química, Filosofia E História Natural (atual Biologia). A partir dessa diversidade de cursos, o país estava preparando uma mão de obra qualificada para, em primeiro lugar, a educação básica”, destaca a pesquisadora.

O estudo também ressalta que a partir das reformas educacionais dos anos 1930, o foco recaía sobre a ampliação do ensino para o que atualmente é conhecido como ensino fundamental completo. Diante disso, foi necessário professores capacitados em cada uma das disciplinas específicas. Para Daiane, o que alguns consideram o "efeito inesperado" das faculdades de filosofia, foi o ingresso em instituições científicas, sobretudo do público feminino. “Mulheres que antes possuíam apenas o Magistério ou nenhuma formação, agora tinham a possibilidade de concluir o ensino superior e a partir dele tanto dar aulas, quanto estagiar nos laboratórios de seus professores, como no caso das alunas de química, física e história natural”, afirma. 

O desenvolvimento do projeto possui duas frentes, uma direcionada a pesquisa sobre a presença de mulheres cientistas no Rio Grande do Sul voltada a investigar suas trajetórias profissionais. “O estudo busca compreender quem é esse público feminino pioneiro no estado, onde se formaram, em quais cursos e quais as principais linhas de atuação. A segunda fase, que se dará a partir do segundo semestre desse ano e próximo ano, diz respeito a divulgação dessas trajetórias, divulgação científica nas escolas, através de oficinas, palestras e distribuição de materiais educativos que ilustrem as trajetórias e inspirem mulheres e meninas a seguir a carreira científica”, acrescenta a docente.

O estudo, que ainda está em desenvolvimento, obteve como resultados parciais uma identificação de 42 mulheres em atuação em instituições científicas no Rio Grande do Sul. Segundo a pesquisadora, “conseguimos informações de 19 delas, sobre nascimento, local de atuação, área de pesquisa, instituição e curso de formação, principais publicações, entre outras. Já sabemos, por exemplo, que a maioria delas trabalhava na área de pesquisas em educação, mas que também havia mulheres atuando na Agronomia, Psicologia, Fisiologia, Física E Matemática”. No entanto, a pesquisa segue em desenvolvimento, com o objetivo de seguir os próximos passos em busca de registros diretamente nas instituições onde as pesquisadoras atuaram na década de 1950. 





UFN e a Pesquisa

A produção científica na Universidade Franciscana (UFN) se iniciou em meados de 2004, através da criação do Mestrado profissionalizante em Ensino de Física e de Matemática. A partir do crescimento em conjunto com a criação de processos, produtos e demais tecnologias, foi implantado, o Programa de Pós-graduação em Nanociências: mestrado (2006) e doutorado (2012). Em 2014, se fez a concretização do Programa de Pós-graduação em Ensino de Ciências e Matemática, nas modalidades Mestrado e Doutorado. No ano de 2015 se iniciou o funcionamento do Mestrado Profissional em Saúde Materno Infantil e, em 2016, Mestrado Acadêmico em Ciências da Saúde e da Vida e o Mestrado em Ensino de Humanidades e Linguagens.

Na Universidade Franciscana, o público feminino desempenha papéis de destaque em várias áreas acadêmicas. Em 2023 a UFN contava com um total de 346 pesquisadores, sendo eles docentes e discentes, desse grupo temos cerca de 244 mulheres. Para a Vice-reitora, pesquisadora e professora, Solange Binotto Fagan, um cenário de reconhecimento se faz perceptível diante das produções científicas. “Na área de Nanociências, aproximadamente 70% dos pesquisadores, incluindo docentes e estudantes, são mulheres, engajadas em atividades científicas de impacto internacional. Esses números refletem o ambiente propício à equidade de gênero e ao reconhecimento do talento das mulheres cientistas aqui na UFN”, finaliza a docente.`;

// Variável de contagem de letras
let contagemLetras = {
  // Letras maiúsculas
  A: 0,
  B: 0,
  C: 0,
  D: 0,
  E: 0,
  F: 0,
  G: 0,
  H: 0,
  I: 0,
  J: 0,
  K: 0,
  L: 0,
  M: 0,
  N: 0,
  O: 0,
  P: 0,
  Q: 0,
  R: 0,
  S: 0,
  T: 0,
  U: 0,
  V: 0,
  W: 0,
  X: 0,
  Y: 0,
  Z: 0,
  // Letras minúsculas
  a: 0,
  b: 0,
  c: 0,
  d: 0,
  e: 0,
  f: 0,
  g: 0,
  h: 0,
  i: 0,
  j: 0,
  k: 0,
  l: 0,
  m: 0,
  n: 0,
  o: 0,
  p: 0,
  q: 0,
  r: 0,
  s: 0,
  t: 0,
  u: 0,
  v: 0,
  w: 0,
  x: 0,
  y: 0,
  z: 0,
  // Letras com acentos e cedilha
  Á: 0,
  É: 0,
  Í: 0,
  Ó: 0,
  Ú: 0,
  À: 0,
  È: 0,
  Ì: 0,
  Ò: 0,
  Ù: 0,
  Â: 0,
  Ê: 0,
  Î: 0,
  Ô: 0,
  Û: 0,
  Ã: 0,
  Õ: 0,
  Ç: 0,
  á: 0,
  é: 0,
  í: 0,
  ó: 0,
  ú: 0,
  à: 0,
  è: 0,
  ì: 0,
  ò: 0,
  ù: 0,
  â: 0,
  ê: 0,
  î: 0,
  ô: 0,
  û: 0,
  ã: 0,
  õ: 0,
  ç: 0,
  // Números
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  // Símbolos
  "!": 0,
  "@": 0,
  "#": 0,
  $: 0,
  "%": 0,
  "^": 0,
  "&": 0,
  "*": 0,
  "(": 0,
  ")": 0,
  "-": 0,
  _: 0,
  "=": 0,
  "+": 0,
  "[": 0,
  "]": 0,
  "{": 0,
  "}": 0,
  ";": 0,
  ":": 0,
  "'": 0,
  '"': 0,
  ",": 0,
  "<": 0,
  ".": 0,
  ">": 0,
  "/": 0,
  "?": 0,
  "\\": 0,
  "|": 0,
  "`": 0,
};

// Loop para percorrer o texto
for (let i = 0; i < texto.length; i++) {
  let letra = texto[i];
  // Verificar se a letra já existe no objeto contagemLetras
  if (contagemLetras.hasOwnProperty(letra)) {
    contagemLetras[letra]++;
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
