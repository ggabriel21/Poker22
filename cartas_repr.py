from defs_lambs import *
import numpy as np
import re

'''
Este módulo apresenta a classe Cartas5. Esta classe auxilia na representação da string de cartas (ex. "TS JS QS KS AS")  em formatos necessários ao trabalho de comparação e ranking.
'''

class Cartas5():

  def __init__(self, setinHand):

    self.mao=setinHand
    self.pcart=np.zeros([4,13], dtype=int)
    self.numeros=[]

# Construção de uma matriz bidimensional (numpy) para representação numérica das cartas.
#  linhas da matriz = naipes  , colunas da matriz = numeração da carta
#  na posição da carta na matriz tems-se n=1.
#
# self.pcart é a matriz numpy com a representação
# self.numeros é uma lista com os números das cartas (sem naipe)

    for i in range(5):
      x=naipe_carta(self.mao[symbolos_carta(i)[1]])
      y=numero_carta(self.mao[symbolos_carta(i)[0]])
      self.pcart[x,y]=1
      self.numeros.append(y+2)

# Retorna a própria string
  def get_cartas(self):
    return self.mao

# Retorna matriz numérica numpy
  def np_repr(self):
    return self.pcart 

# Retorna matriz numérica numpy  transposta
  def np_reprt(self):
    return self.pcart.T

# Retorna lista numérica com as 5 cartas
  def num(self):
    return sorted(self.numeros)

# Retorna representação numpy transformada em string
  def str_repr(self):
    mmao_total=[linha_string(x, self.pcart) for x in range(NAIPES)]
    return mmao_total

# Retorna representação numpy transformada em string  transposta
  def str_reprt(self):
    mmao_total=[linha_string(x, self.pcart.T) for x in range(NCARTAS)]
    return mmao_total

