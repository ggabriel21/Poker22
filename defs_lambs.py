# Arquivo contém a maior parte das definições necessárias para o programa poker22
# Estão concentradas aqui para facilitar o desenvolvimento e acuracidade do programa.

# Algumas definições podem, no entanto, estar em seus respectivos módulos, por fazer mais sentido dessa # forma

import sys

# Cartas apresentam símbolos tradicionais que correspodem a números. Este dicionário faz a tradução
sym2dec={"T":10, "J":11, "Q":12, "K":13, "A":14, "S":0, "H":1, "D":2, "C":3 } 

NAIPES = 4

# Cartas por naipe
NCARTAS = 13

RANKING_NAIPES = [ ]

# função que retorna o número normalizado de uma carta ( 0 a 12)
numero_carta = lambda x: sym2dec[x]-2 if x in "TJQKA" else int(x)-2

# número do naipe (0 a 3)
naipe_carta =  lambda x: sym2dec[x]

# Os símbolos de uma carta de encontram em posições 0,1..3,4..5,6  etc ("TS JS QS KS AS")
symbolos_carta= lambda x: [3*x, 3*x+1]

# esta função auxilia a transformação de representação de cartas de numérica para string
linha_string=lambda linha, mao: "".join([str(int(x)) for x in mao[linha] ])

# Para o ranking de cartas é utilizada esta função. Aplicada a todas as 5 cartas numéricas sorteadas ela # retorna um número que indica qual a mão tem elementos maiores que a outra (para 2pairs, 1 paris, 
# highcard. O número 14 é um inteiro escolhido acima da maior carta normalizada, que é 12)
soma_q= lambda ni, lin :  (14**ni)*lin[ni]

# Símbolos dos resultados
EuGanhei=1
AdGanhou = 2
Empatou = 3
Indefinido = 4

# mão de poker tem n cartas. A string geralmente tem 14 caracteres
CARTAS_NA_MAO =5
LEN_MAO =14

# símbolos dos naipes
SUITS = "SHDC"
CARDS_NUMBERS= "23456789TJQKA"

# Posição dos espaços na string de cartas ("TS JS QS KS AS")
pos_espaco = lambda x: 3*x+2


# Quando der indefinido é necessário verificar a próxima value rating de poker (RSF>SF>etc)
# Quando der Empate é necessário usar os critérios de empate que são bastante variáveis.
# Dicionário abaixo transforma resultados booleanos em resultados utilizáveis para display etc
Ganhador ={(True, False): (EuGanhei,"Sou Vencedor!")  , (True, True): (Empatou, "Empatamos!")  , (False, True): (AdGanhou,"Adversário ganhou!") , (False, False): (Indefinido,"") }

Resultado_string={ EuGanhei: "Sou Vencedor!",  Empatou: "Empatamos!", AdGanhou: "Adversário ganhou!", Indefinido: "Não consegui avaliar!" }


# auxiliares de help, versão e saídas com códigos de erro:

versao ="Versão:\t1.0\n Data:\t\tMar-2022\n Autor:\t\tDesenvolvimento de ggabriel21@gmail.com\n"
versao1= "SO de Desenvolvimento:\t\tUbuntu\n Python:\t\t\tversão 3.x\n Execução:\t\t\tInterpretado"

texto_explicativo = '''\
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
Three Kind		=> "QS QH QD 2C 3D" ou "KS KH KD TC 3D"
2 Pairs			=> "QS QH JD 2C 2D" ou "KD KC 8D 3S 3H"
1 Pair			=> "QS QH JD 2C 5D" ou "JD QC QD 3C 2D"
Highcard		=> "JD 5C QD 3C 2D" ou "JD KC TD 2C 5D"

'''

def sair_com_codigo(x):
  print ("\nusage: [--minhamao 'mao' --advmao 'mao'] [--versao] [--help] ") 
  print (texto_explicativo)
  sys.exit(x)
