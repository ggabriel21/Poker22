from defs_lambs import *
from samples import *
import unittest


''' 
Esta classe é utilizada para testar a validade do string de cartas no formato acordado.
Também verifica cartas inexistentes ou duplicadas, inclusive entre as mãos dos adversários

Esta classe pode ser testada antecipadamente:

# python cartas_valid.py

É fornecido um set de cartas para verificação (invalid_cards em samples.py). Para verificar a atuação do tdd podem ser introduzidos erros nas cartas em invalid_cards

'''


class ValidMao():
  def __init__(self, mao):
    self.mao=mao

  def AmI(self):

# string de cartas tem um lenght definido
    if len(self.mao) != LEN_MAO:
      return (False)

# Naipe não existe
    for i in range(CARTAS_NA_MAO):

      if self.mao[symbolos_carta(i)[1]] not in SUITS:
        return(False)

# Numero de carta não existe
      if self.mao[symbolos_carta(i)[0]] not in CARDS_NUMBERS:
        return(False)

# formato não é "JH JC 3D 2C KD"
      if i!= CARTAS_NA_MAO-1 and self.mao[pos_espaco(i)] !=" ":
        return(False)

# cartas repetidas em uma mão
      if len(self.mao.split(" ")) != len(set(self.mao.split(" "))):
        return(False)
    return(True)

# método para detectar cartas repetidas entre as mãos
  def Entremaos(self, adv):
    if len(self.mao.split(" ")+ adv.split(" ")) != len(set(self.mao.split(" ")+ adv.split(" "))): 
      return(False)
    return(True)

# testes antecipados de validade de mãos. Temos o set de cartas  invalid_cards localizado em samples. Todas as cartas estão validas. Mas podem ser introduzidas cartas erradas para "testar o teste"

class ValidMaoTest(unittest.TestCase):
  def setUp(self):
    self.inv=invalid_cards()

  def testargs(self):
    for i in range(len(self.inv)):
      print(i, end=" ")
      self.assertTrue(ValidMao(self.inv[i]).AmI() ==True )

if __name__ == "__main__":
  unittest.main()


