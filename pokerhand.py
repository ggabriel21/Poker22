from samples import *
from cartas_repr import *
from poker_eval import *
import unittest

# Este módulo hospeda a classe principal do programa (PokerHand). Ela é responsável pelas comparações
# entre os ratings de poker (RSF, SF etc)

# Classe Pokerhand
# Apresenta os métodos:
# - compare_with	=> efetua o ranking propriamente dito. Faz o reconhecimento do tipo e avalia.
# - str_carta		=> Apenas devolve a pŕopria mão da classe

# Tem-se ainda a classe PokerHandTest  para TDD.

# Complementa o módulo duas funções auxiliares para comparaçoes entre cartas:
#
# - teste_empate
# - Teste_Rating
#

#---------- Classe PokerHand ---------

class PokerHand():
  def __init__(self, mao):
    self.mao = mao

  def compare_with(self, objmao):

# Instanciar os objetos 5cartas:
# Tanto para minha_mão como para adversário

    cartas5_minha=Cartas5(self.mao)

    cartas5_adver=Cartas5(objmao.str_carta())

#   Acessar representações das 5 cartas:  Como matriz de strings, strings transpostas ou numericas
#  Estas representações serão extensivamente utilizadas. Portanto faremos todas aqui.

    MinhaMaostring = cartas5_minha.str_repr() 	 # formato string 
    AdvMaostring   = cartas5_adver.str_repr()  
    MinhaMaostringT = cartas5_minha.str_reprt()	# formato string matriz transposta
    AdvMaostringT   = cartas5_adver.str_reprt()
    MinhaMaostringN = cartas5_minha.num()  	# formato numérico
    AdvMaostringN   = cartas5_adver.num()

# Lista de Classes e métodos com tipos de maos. Esta lista será percorrida na ordem para o ranking

    Work2Do = [
("RSF",RSF, MinhaMaostring, AdvMaostring),
("SF", SF, MinhaMaostring, AdvMaostring),
("FourKind", FKind, MinhaMaostringT, AdvMaostringT),
("FullHouse", FullHouse, MinhaMaostringT, AdvMaostringT),
("Flush",Flush, MinhaMaostring, AdvMaostring),
("Straight",Straight, MinhaMaostringN, AdvMaostringN),
("ThreeKind", ThKind, MinhaMaostringT, AdvMaostringT)
]

# o loop a seguir percorre a lista e executa os rankings necessários:

# Am I RSF, SF, FKind, FullHouse, Flush, Straight, ThKind    and what about my opponent  ?

    for tipo_mao in Work2Do:
      sfx= Teste_Rating( tipo_mao[1], tipo_mao[2] , tipo_mao[3] ) 
      gan=teste_empate(sfx[0], sfx[1])

      if gan[0] != Indefinido:
        print("Ganhador => ", tipo_mao[0]," Mão:", gan[0],"\n")
        return(gan[0])      

#--------- Twoo Pairs -----------
# Am I Twpairs  and what about my opponent  ?
# twpairs necessida de uma mecanica diferente das anteriores por causa do desempate:

    sfI= Twpairs(MinhaMaostringT,MinhaMaostringN).AmI()
    sfY= Twpairs(AdvMaostringT, AdvMaostringN).AmI()
    gan=teste_empate(sfI, sfY)

# se empate no par superior teste com o par inferior

    if gan[0]==Empatou:
      sfI[1]=sfI[2]
      sfY[1]=sfY[2]
      gan=teste_empate(sfI, sfY)

# Se empate com o par inferior teste com a carta 5
    if gan[0]==Empatou:
      sfI[1]=sfI[3]
      sfY[1]=sfY[3]
      gan=teste_empate(sfI, sfY)

    if gan[0] != Indefinido:
      print("Ganhador => ", "Twoopairs "," Mão:",gan[0],"\n")
      return(gan[0])

#--------- One Pair -----------

# Am I Onepair  and what about my opponent  ?

    sfI= Onepair(MinhaMaostringT, MinhaMaostringN).AmI()
    sfY= Onepair(AdvMaostringT, AdvMaostringN).AmI()
    gan=teste_empate(sfI, sfY)
#   print(" op ", sfI[1], "  ", sfY[1] )

# Se empate com o par teste com as outras 3 cartas
    if gan[0]==Empatou:
      sfI[1]=sfI[2]
      sfY[1]=sfY[2] 
      gan=teste_empate(sfI, sfY)
#     print(" op ", sfI[1], "  ", sfY[1] )
    if gan[0] != Indefinido:
      print("Ganhador => ", "Onepair "," Mão:",gan[0],"\n")
      return(gan[0])

#--------- HighCard -----------

  # Am I  HighCard  and what about my opponent  ?

    sfx= Teste_Rating( HighCard, MinhaMaostringN , AdvMaostringN ) 
    gan=teste_empate(sfx[0], sfx[1])

#    print(" hc ", sfx[0], "  ", sfx[1] )
       
    if gan[0] != Indefinido:
      print("Ganhador => ", "HighCard "," Mão:",gan[0],"\n")
      return(gan[0])

# Não conseguir estabelecer o que as cartas representavam:

    return(Indefinido)

  def str_carta(self):
    return (self.mao)


# o retorno das classes de teste é comparado aqui para verificar o vencedor

def teste_empate(sf1, sf2):
  gan = Ganhador[(sf1[0], sf2[0] )]
  if gan[0]==Empatou:
    if sf1[1] > sf2[1]:
      gan= (EuGanhei,"Após desempate sou Vencedor!")
    elif sf1[1] < sf2[1]:
      gan= (AdGanhou,"Após desempate Adversário ganhou!")
  return(gan)   


# rating é o nome da classe de teste entre (RSF, SF ..etc)

def Teste_Rating( rating, minha , adv ): 
  sfI1= rating(minha).AmI()
  sfY1= rating(adv).AmI()
  return ([sfI1, sfY1])


#------- TDD ---------------
#  tdd para auxílio no desenvolvimento desta classe
# Os testes são os propostos pelos examinadores. Encontram-se no módulo samples.py 
# Foram colocados em uma lista chamada testes_antecipados_propostos e são executados com um for.

class PokerHandTest(unittest.TestCase):
   def testcards(self):
    for tdd in testes_antecipados_propostos:
      print(tdd[0])
      eval(tdd[1])


if __name__ == "__main__":
  unittest.main()
