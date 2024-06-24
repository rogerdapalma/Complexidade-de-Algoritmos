# Tratabilidade: Explorando as Classes P, NP e NP-Completo

## Autores
Roger Palma, Vitor Posebon

## Conceitos

### Classe P
Esta classe engloba os problemas que podem ser resolvidos rapidamente (em tempo polinomial) por uma máquina de Turing determinística. Um exemplo típico são os algoritmos de ordenação como o mergesort, que organizam dados de maneira eficiente e previsível, tornando-se fundamentais em operações do dia a dia, desde a organização de arquivos em um computador até a ordenação de transações bancárias.

### Classe NP
Compreende os problemas cujas soluções são verificáveis em tempo polinomial, mesmo que encontrar essas soluções possa ser extremamente desafiador. O problema do caixeiro-viajante é emblemático nesta classe: verificar se uma rota específica é a mais curta é rápido, mas descobrir qual é essa rota entre inúmeras possibilidades pode ser incrivelmente complexo.

### NP-Completo
Esses são os problemas mais desafiadores dentro de NP. Eles não são apenas difíceis de resolver, mas qualquer problema em NP pode ser transformado em um problema NP-Completo em tempo polinomial. O problema da satisfabilidade booleana (SAT), onde se busca atribuir valores que satisfaçam uma expressão lógica complexa, é um exemplo clássico.

## Discussão
A distinção entre P e NP é crucial para entender limites computacionais. A questão de se P é igual a NP permanece como um dos Problemas do Milênio não resolvidos.

### Redução Polinomial
Este é um conceito chave para entender como um problema pode ser considerado pelo menos tão difícil quanto outro. Através deste método, uma instância de um problema é transformada em outra de um tipo diferente, dentro do limite de tempo polinomial, demonstrando a equivalência em complexidade entre eles.

A distinção entre as classes P e NP é fundamental para entender os limites do que os computadores podem fazer eficientemente. A questão de se P é igual a NP é um dos Problemas do Milênio não resolvidos e tem implicações profundas. Na criptografia, por exemplo, se P fosse igual a NP, muitos dos sistemas de segurança que protegem informações confidenciais seriam comprometidos, pois os problemas que atualmente assumimos serem difíceis (e por isso seguros) poderiam ser resolvidos facilmente. Além disso, entender essas classes é crucial em áreas como o processamento de grandes volumes de dados e inteligência artificial, onde a escolha de algoritmos apropriados pode significar a diferença entre obter resultados em tempo útil ou enfrentar atrasos impraticáveis.

## Referências
- [Artigo RMU](https://rmu.sbm.org.br/wp-content/uploads/sites/27/2018/03/n05_Artigo03.pdf)
- [MSc Oliveira, Warwick](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/MSc-Oliveira.pdf)
