# Arquivo contém dados utilizados para testes, exemplos ou desenvolvimento.

# Símbolos dos resultados finais do programa
# Como método ou como propriedade
class Result():
  WIN=1
  LOSS=2
  TIE=3

Result.WIN=1
Result.LOSS=2
Result.TIE=3


# ---- lista tc ------
# tc é uma lista com mãos exemplificativas. Foi utilizado no desenvolvimento.
# Estas cartas são exemplos de cada tipo de ranking do poker  RSF, SF etc . tem mais de um por
# tipo porque colocou-se algumas que gerariam situações de uso de critérios de empate

def tcexemplos():

  tc=["" for z in range(30)]

# RSF    ok
# tie (S > H > D > C)

  tc[0]="TS JS QS KS AS"
  tc[1]="TH JH QH KH AH"
  tc[2]="TD JD QD KD AD"
  tc[3]="TC JC QC KC AC"

# SF   ok
# tie (HCard  and SUITS)
  tc[4]= "9C TC JC QC KC"
  tc[5]="2H 3H 4H 5H 6H"
  tc[6]="2H 3H 4H 5H 6H"
  tc[7]="7H 8H 9H TH JH"
  tc[8]="9H TH JH QH KH"

# 4K    ok
# tie Hcard
  tc[9]= "9S 9H 9D 9C KC"
  tc[10]= "QS QH QD QC KC"

# FULL HOUSE  tie => hc3
  tc[11] = "QS QH QD 2C 2D"
  tc[12] = "KS KH KD 2C 2D"

# FLUSH
# TIE hc then hc2
  tc[13]= "KD TD 7D 6D 3D"
  tc[14]=  "TH 4H 3H 2H 5H"

# STRAIHGT 
# tie   hc then suits
  tc[15] =  "2H 3D 4S 5H 6S"
  tc[16] =  "3D 4S 5H 6S 7D"
  tc[17] =  "KD 9S QH TS JH"

# 3K
# tie hc
  tc[18] = "QS QH QD 1C 3D"
  tc[19] = "KS KH KD TC 3D"

# 2P
# tie hc2 hc1 5th  suit
  tc[20] = "QS QH JD 2C 2D"
  tc[21] = "KS KH 9D 2C 2D"
  tc[22] = "KD KC 9D 3C 3D"
  tc[23] = "KD KC 8D 3S 3H"

# 1P  hc then hc
  tc[24] = "QS QH JD 2C 5D"
  tc[25] = "JS JH TD 5C 2D"
  tc[26] = "JD QC QD 3C 2D"

# HC
# tie next hc
  tc[27] = "JD JC QD 3C 2D"
  tc[28] = "JD KC QD 3C 2D"
  tc[29] = "JD KC TD 2C 5D"
  return (tc)


#------ invalid_cards -------
# Neste invalid_cards podemos testar o módulo cartas_valid para verificar a acuracidade do TDD.
# Estas cartas são basicamente as propostas pelo examinador. Podem ser feitas alterações nas cartas para # verificar o unitttest  (ex. "JS JX AS KC TD" ou "JSJC AS KC TD" que são inválidas, notando o"X" e a # ausencia de espaço na segunda)

def invalid_cards():
  invalid = [ "TS TD KC JC 7C"  , "JS JD AS KC TD"  , \
"7H 7C QC JS TS"  , "7D 7C JS TS 6D"  , \
"5S 5D 8C 7S 6H"  , "7D 7S 5S 5D JS"  , \
"AS AD KD 7C 3D"  , "AD AH KD 7C 4S"  ,\
"TC TH 5C 5H KH"  , "9C 9H 5C 5H AC"  ,\
"TS JS QS KS AS"  , "AC AH AD AS KS"  ,\
"TS JS QS KS AS"  , "TC JS QC KS AC"  ,\
"TS JS QS KS AS"  , "QH QS QC AS 8H"  ,\
"AC AH AD AS KS"  , "TC JS QC KS AC"  ,\
"AC AH AD AS KS"  , "QH QS QC AS 8H"  ,\
"TC JS QC KS AC"  , "QS QD QC AS 8H"  ,\
"7H 8H 9H TH JH"  , "JH JC JS JD TH"  ,\
"7H 8H 9H TH JH"  , "4H 5H 9H TH JH"  ,\
"7H 8H 9H TH JH"  , "7C 8S 9H TH JH"  ,\
"7H 8H 9H TH JH"  , "TS TH TD JH JD"  ,\
"7H 8H 9H TH JH"  , "JH JD TH TC 4C"  ,\
"JH JC JS JD TH"  , "4H 5H 9H TH JH"  ,\
"JH JC JS JD TH"  , "7C 8S 9H TH JH"  ,\
"JH JC JS JD TH"  , "TS TH TD JH JD"  ,\
"JH JC JS JD TH"  , "JH JD TH TC 4C"  ,\
"4H 5H 9H TH JH"  , "7C 8S 9H TH JH"  ,\
"4H 5H 9H TH JH"  , "TS TH TD JH JD"  ,\
"4H 5H 9H TH JH"  , "JH JD TH TC 4C"  ,\
"7C 8S 9H TH JH"  , "TS TH TD JH JD"  ,\
"7C 8S 9H TH JH"  , "JH JD TH TC 4C"  ,\
"TS TH TD JH JD"  , "JH JD TH TC 4C"  ]
  return invalid

#------ testes_antecipados_propostos ------------------
# Esta lista contém os testes passados pelo examinador. Apenas incorporamos a string do tipo de teste 
# ( Ex.  ' two pair x two pair') como primeiro elemento da lista.
# É utilizada no módulo pokerhand em um for que percorre toda a lista e executa os testes.
# obs. o último elemento desta lista foi incorporado depois. É um exemplo de highcard x highcard.

testes_antecipados_propostos= [ ( ' two pair x two pair' ,  ' self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5D 5S AC")) == Result.WIN )'  ),
( ' one pair x one pair' ,  ' self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JD AS KC TH")) == Result.LOSS )'  ),
( ' one pair x one pair' ,  ' self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7S JH TH 6D")) == Result.WIN )'  ),
( ' one pair x two pair' ,  ' self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7H 5H 5C JS")) == Result.LOSS )'  ),
( ' one pair x one pair' ,  ' self.assertTrue(PokerHand("AS AC KH 7D 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS )'  ),
( ' royal straight flush x four of a kind' ,  ' self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("9C 9H 9S 9D KH")) == Result.WIN )'  ),
( ' royal straight flush x straight' ,  ' self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JD QC KC AC")) == Result.WIN )'  ),
( ' royal straight flush x three of a kind' ,  ' self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QC QD AD 8H")) == Result.WIN )'  ),
( ' four of a kind x straight' ,  ' self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("9C TC JS QC KS")) == Result.WIN )'  ),
( ' four of a kind x three of a kind' ,  ' self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("QH QS QC KD 8H")) == Result.WIN )'  ),
( ' straight x three of a kind' ,  ' self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QD AS 8H")) == Result.WIN )'  ),
( ' straight flush x four of a kind' ,  ' self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("KH KC KS KD TD")) == Result.WIN )'  ),
( ' straight flush x flush' ,  ' self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4C 5C 9C TC JC")) == Result.WIN )'  ),
( ' straight flush x straight' ,  ' self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9S TC JC")) == Result.WIN )'  ),
( ' straight flush x full house ' ,  ' self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN )'  ),
( ' straight flush x two pair' ,  ' self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JC JD TD TC 4C")) == Result.WIN )'  ),
( ' four of a kind x flush' ,  ' self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H QH KH")) == Result.WIN )'  ),
( ' four of a kind x straight' ,  ' self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("5C 6S 7H 8H 9H")) == Result.WIN )'  ),
( ' four of a kind x full house' ,  ' self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TC TD KH KD")) == Result.WIN )'  ),
( ' four of a kind x two pair' ,  ' self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("QH QD TD TC 4C")) == Result.WIN )'  ),
( ' flush x straight' ,  ' self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9D TD JC")) == Result.WIN )'  ),
( ' flush x full house' ,  ' self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS )'  ),
( ' flush x two pair' ,  ' self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TS TC 4C")) == Result.WIN )'  ),
( ' straight x full house' ,  ' self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS )'  ),
( ' straight x two pair' ,  ' self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JC JD TS TC 4C")) == Result.WIN )'  ),
( ' three of a kind x two pair' ,  ' self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JS JC KC KC 4C")) == Result.WIN )'  ),
( ' Highcard x Highcard' ,  ' self.assertTrue(PokerHand("2S 3H 5D 9H KD").compare_with(PokerHand("KS 9C 5C 2C 4C")) == Result.LOSS )'  ) ]

