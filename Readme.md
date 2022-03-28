# Programa Poker22 - Ranking de mãos de Poker


## Índice

1. Introdução

2. Getting Started NOW

3. Observações sobre execução

4. Explicação dos módulos

5. Testes Antecipados

6. Futuro



## 1. Introdução

O código neste pacote é solução para um desafio de Poker, qual seja determinar a mão ganhadora entre dois adversários, em posição final de etapa, quando as mãos são reveladas. O desafio foi proposto pela empresa Data H AI, Autor Marcelo Piovan e se encontra na versão 1.2. Este documento faz parte deste pacote.

Para solução do desafio as regras de Poker foram codificadas de forma a permitir a análise das mãos (conjunto de cinco cartas) algoritmicamente e verificação do vencedor. Isto corresponde ao objetivo deste algoritmo.

A solução apresentada objetiva simplicidade e clareza. Tentou-se um equilíbrio entre eficiência de código Python e entendimento do mesmo. O programa é desenhado para execução com entrada via linha de comando. A execução batch pode ser fácilmente implementada, uma vez que já é utilizada nos testes antecipados (TDD).  

A presente solução comporta uma evolução para game "ingênuo" e didático como descrito no item "Futuro" abaixo. 



## 2. Getting Started NOW!!!


**==> Programa Principal  _poker22.py_**

*Os arquivos a seguir são parte do projeto Poker22:*

- poker22.py        	 **<=== Programa "main"** 
- cartas_valid.py
- defs_lambs.py
- cartas_repr.py
- pokerhand.py
- poker_eval.py
- samples.py

O programa principal é o *poker22.py*. Este deve ser manipulado em linha de comando e de forma interpretada ( # python poker22.py) para o objetivo do exercício. Os demais são componentes auxiliares. Apenas *pokerhand.py* e *cartas_valid.py* podem ser utilizados de forma standalone e para finalidade de TDD.


**==> Execução do programa:  (Sem parâmetros)**

``` 
<prompt >  python poker22.py

usage: [--minhamao 'mao' --advmao 'mao'] [--versao] [--help] 
Este programa deve ser utilizado com 2 parametros:

--minhamao	=>	Mão do oponente 1. Conhecida como "Minha mão"

--advmao	=>	Mão do oponente 2. Conhecida como "Adversário mão"

Exemplo:
# python poker22.py --minhamao "9C 9H 2C 2H TC" --advmao "9D 9S 2S 2D 7S"


Exemplos de Mãos que podem ser utilizadas para exercitar o programa:
(Sugestão: experimente pegar daqui com cut+modify+paste  !!!   )

Royal Straight Flush	=> "TS JS QS KS AS" ou "TH JH QH KH AH"
Straight Flush		=> "9C TC JC QC KC" ou "7H 8H 9H TH JH"
Four Kind		=> "9S 9H 9D 9C KC" ou "QS QH QD QC KC"
Full House		=> "QS QH QD 2C 2D" ou "KS KH KD 2C 2D"
Flush			=> "KD TD 7D 6D 3D" ou "TH 4H 3H 2H 5H"
Straight		=> "2H 3D 4S 5H 6S" ou "KD 9S QH TS JH"
Three Kind		=> "QS QH QD 1C 3D" ou "KS KH KD TC 3D"
2 Pairs			=> "QS QH JD 2C 2D" ou "KD KC 8D 3S 3H"
1 Pair			=> "QS QH JD 2C 5D" ou "JD QC QD 3C 2D"
Highcard		=> "JD 5C QD 3C 2D" ou "JD KC TD 2C 5D"
```

**==> Execução do programa: (Com parametrização)**

```
# python poker22.py --minhamao "9C 9H 2C 2H TC" --advmao "9D 9S 2S 2D 7S"


Minha mão =>			 9C 9H 2C 2H TC
Adversário mão =>		 9D 9S 2S 2D 7S
Mãos válidas!!!
Ganhador =>  Twpairs   Mão: 1
Resultado  minhamao x  advmao =>  Sou Vencedor!
```


## 3. Observações sobre execução:

1) **Executar o código de forma interpretada** (# python poker22.py). 

Não existem restrições para atribuição do código +x (chmod +x) , no entanto, para facilidade de desenvolvimento e como não temos problemas de performance, sempre utilizamos o interpretador.


2) Desenvolvido em Ubuntu 18.x LTS , Python 3.x.


3) **Todos os arquivos auxiliares devem estar no diretório de execução** . Não usamos estruturas de diretórios devido à simplicidade da estrutura.



## 4. Explicação dos Módulos

O programa *poker22.py* é composto dos seguintes modúlos:

poker22.py
--------------
Programa principal. Contém o "main" principal executado.
Apresenta interação mínima com o usuário. Praticamente necessitando apenas da indicação do conjunto de cinco cartas de jogador 1 e do jogador 2. 
Esta indicação se dá pela linha de comando mesmo (parâmetros --minhamao  --advmao).
Invoca a classe *ValidMao* para verificação da consistencia dos jogos apresentados. 
Uma vez validadas as cartas  o programa prossegue invocando a classe  *PokerHand* que efetivamente retorna a vencedora 
entre mão 1 (minha mão) e mão 2 (mão adversário)


cartas_valid.py 		
---------------
Esta classe é utilizada para validação do jogo de 5 cartas. É importante que a string representando a carta de um jogador esteja formatada da forma correta. Então os métodos dessa classe verificam a quantidade de caracteres, o set de caracteres utilizados e suas repetições não aceitáveis. Também verifica se existem repetições entre as cartas dos jogadores. (Ex de mão: "TS JS QS KS AS"). Esta classe dispõe de TDD.


defs_lambs.py
-------------
Este arquivo reúne definições, funções lambda, assim como constantes utilizadas nos módulos. Algumas definições, no entanto, foram mantidas em seus módulos originais, de forma a facilitar o entendimento dos mesmos.


cartas_repr.py
--------------
Esta classe é responsável por fornecer diferentes tipos de formatações da string de jogo (Ex de string "TS JS QS KS AS"). Assim, por exemplo, pode ser necessário uma representação numérica em matriz de naipes x números. Ou então uma representação transposta de números x naipes. Ou ainda representações em formato str (de forma a utilizar-se a imensa gama de métodos disponíveis para esses formatos)


pokerhand.py
------------
Este módulo hospeda a classe principal do programa. Ela, uma vez instanciada, cria um objeto "mão de 5 cartas", que dispõe de métodos para reconhecimento dos diferentes "Poker Hand Values" (Royal Straight Flush, Straight Flush..etc). Uma vez reconhecido o tipo de mão, os jogos entre adversários são rankeados. Neste módulo encontram-se ainda classes auxiliares como *teste_empate* e *Teste_rating* destinadas a testes de desempate entre jogos do mesmo tipo (Ex  jogo 1 é SF mas jogo 2 também é SF, tem que desempatar)


poker_eval.py
-------------
Este módulo hospeda classes para os diferentes tipos de jogos:  RSF, SF, FourofKind etc. Cada um destes corresponde a uma classe que reúne suas características e através de métodos faz o reconhecimento. Os métodos retornam a definição booleana se o jogo é desse tipo específico e no caso *True*, retornam elementos do jogo para um eventual desempate.

samples.py
----------
Este módulo contém os dados para teses de cartas inválidas e testes propostos pelo examinador para TDD




## 5. Testes Antecipados

Os módulos a seguir dispõe de TDD:

- cartas_valid.py

- pokerhand.py


 Para seu acionamento é só invocar na linha de comando:

- python cartas_valid.py

- python pokerhand.py


Exemplos e explicações dos comandos:

<prompt> python cartas_valid.py

```
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
```

**Os números mostrados correspondem aos testes (bem-sucedidos) realizados. O input para esses testes é a lista *invalid* dentro da função *invalid_cards* no módulo *samples.py*.  Esta lista pode ser modificada, criando-se tipos inválidos ou outros tipos válidos.**

  

<prompt> python pokerhand.py

 python pokerhand.py

```

 two pair x two pair
Ganhador =>  Twpairs   Mão: 1
 one pair x one pair
Ganhador =>  Onepair   Mão: 2
..... linhas deletadas...
 three of a kind x two pair
Ganhador =>  FullHouse  Mão: 1
 Highcard x Highcard
Ganhador =>  HighCard   Mão: 2
.
----------------------------------------------------------------------
Ran 1 test in 0.025s

OK
```

**Estes testes correspodem aos fornecidos pelo examinador e formulador do desafio. Os testes se encontram em *samples.py* na lista *testes_antecipados_propostos*.**



## 6. Futuro

Este código é bastante apropriado para inserção em um serviço de cloud. Pode ser colocado na Google Cloud Function. Simplesmente respondendo a uma requisição HTML e retornando o vencedor das cartas. É fácil construir uma interface gráfica atrativa em um APP para android ou iphone para que o usuário escolha cartas ou sejam escolhidas randomicamente. Pode se tornar um joguinho ingênuo e didático.

