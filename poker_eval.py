from defs_lambs import *
import numpy as np
import re

# Este módulo hospeda as classes relativas aos tipos de mãos de poker
# seguem abaixo em ordem de "poder"



#---------- RSF ----------
# Para reconhecimento deste tipo usaremos Regular Expressions em uma string de cartas
# Deve reconhecer "11111" no final da string. Note que a classe retorna o naipe, que não é usado

class RSF():
  def __init__(self, mao):
    self.mao=mao
    self.naipe=0
  def AmI(self):
    for self.naipe in range(NAIPES):
      match=re.search("^0+11111$", self.mao[self.naipe])
      if (match):
        return (True, self.naipe)
    return (False,-1)



#---------- SF ----------
# Para reconhecimento deste tipo usaremos Regular Expressions em uma string de cartas
# Deve reconhecer "11111" em qualquer parte da string, menos no final. Note que a classe retorna o naipe,
# que não é usado

class SF():
  def __init__(self, mao):
    self.mao=mao
    self.naipe=0
  def AmI(self):
    for self.naipe in range(NAIPES):
      match=re.search("^0*(11111)0+$", self.mao[self.naipe])
      if (match):
        return (True, match.start(1) , self.naipe)
    return (False, -1, -1)



#---------- Four Kind ----------
# Para reconhecimento deste tipo usaremos Regular Expressions em uma string de cartas em formato
# transposto. A transposição expõe os naipes das cartas.
# Deve reconhecer "1111" em qualquer numero de cartas (naipe completo)

class FKind():
  def __init__(self, maoT):
    self.maoT=maoT
    self.ncartas=0
  def AmI(self):
    for self.ncartas in range(NCARTAS):
      match=re.search("1111", self.maoT[self.ncartas])
      if (match):
        return (True, self.ncartas)
    return (False,-1)



#---------- Full House ----------
# Para reconhecimento deste tipo usaremos "count" para contar a ocorrencia de uma mesma carta. Sendo 3 x uma carta e 2 x outra.
# A representação é string transposta

class FullHouse():
  def __init__(self, maoT):
    self.maoT=maoT
    self.ncartas=0
    self.found3=0
    self.found2=0
  def AmI(self):
    for self.ncartas in range(NCARTAS):
      if self.found3 and self.found2:
         return (True, self.found3-1, self.found2-1)
      if not (self.found3) and (self.maoT[self.ncartas].count("1")==3):
        self.found3=self.ncartas+1
        continue
      if not (self.found2) and (self.maoT[self.ncartas].count("1")==2):
        self.found2=self.ncartas+1
        continue
    return (False, -1, -1)


#---------- Flush ----------
# Para reconhecimento deste tipo usaremos "count" para contar na mesmo naipe a ocorrencia de 5 cartas, que não estarão na sequencia. Note que a garantia da não sequencia é a filtragem pelas classes anteriores
# A representação é string naipes x numeros. retorna também o último elemento da sequencia

class Flush():
  def __init__(self, mao):
    self.mao=mao
    self.naipe=0
  def AmI(self):
    for self.naipe in range(NAIPES):
      if (self.mao[self.naipe].count("1")==5):
        return(True, self.mao[self.naipe].rfind("1") )
    return (False, -1)


#---------- Straight ----------
# Para reconhecimento deste tipo usaremos "range". Este método gera uma lista com números em sequencia, que pode ser usado para comparação com a mão.
# A representação da mão é em números .

class Straight():
  def __init__(self, lnum):
    self.numeros=lnum
  def AmI(self):  
    if (self.numeros == list(range(self.numeros[0],self.numeros[0]+5))):
      return(True, self.numeros[4])
    return (False, -1)



#---------- Three Kind ----------
# Para reconhecimento deste tipo usaremos count. Utilizando uma representação transposta contaremos 3 ocorrencias. Esta classe é um sub-set da full house.
# A representação da mão é em string transposta. Retorna a carta repetida

class ThKind():
  def __init__(self, maoT):
    self.maoT=maoT
  def AmI(self):
    for self.ncartas in range(NCARTAS):
      if (self.maoT[self.ncartas].count("1")==3):
        return(True, self.ncartas)
    return (False, -1)
 


#---------- Twpairs ----------
# Esta classe é semelhante a full house mas aqui procuramos 2 ocorrencias de 2 cartas iguais (2 pairs)
# Para reconhecimento deste tipo usaremos "count" para contar a ocorrencia de uma mesma carta. Sendo 2 x uma carta e 2 x outra.
# A representação é string transposta . Utilizamos tb representação numérica para efeito de desempate

class Twpairs():
  def __init__(self, maoT, lnum):
    self.maoT=maoT
    self.ncartas=0
    self.found2=0
    self.found2a=0
    self.numeros=lnum
  def AmI(self):
    for self.ncartas in range(NCARTAS):
      if self.found2 and self.found2a:
         return ([True, max(self.found2-1, self.found2a-1), min(self.found2-1, self.found2a-1), sum(self.numeros)] )
      if not (self.found2) and (self.maoT[self.ncartas].count("1")==2):
        self.found2=self.ncartas+1
        continue
      if not (self.found2a) and (self.maoT[self.ncartas].count("1")==2):
        self.found2a=self.ncartas+1
        continue
    return (False, -1, -1)


#---------- Onepair ----------
# Para reconhecimento deste tipo usaremos count. Utilizando uma representação transposta contaremos 2 
# ocorrencias. Esta classe é um sub-set da full house. No entanto, aqui usamos tb a representação
# numerica para efeito de desempate (ver fórmula de desempate em highcard abaixo)
# A representação da mão é em string transposta. Retorna a carta repetida

class Onepair():
  def __init__(self, maoT, lnum):
    self.maoT=maoT
    self.numeros=lnum
  def AmI(self):
    for self.ncartas in range(NCARTAS):
      if (self.maoT[self.ncartas].count("1")==2):
        return([True, self.ncartas, sum([soma_q(i, self.numeros) for i in range(5)])])
    return (False, -1)


#---------- HighCard ----------
# Aqui a sequencia restante será avaliada pelas cartas maiores. Para evitar o loop entre as cartas para
# verificar a maior em caso de desempate, adotamos a seguinte fórmula: (sequencia sorteada crescente)
# Soma_mao_ = c1 * 14**0 + c2 * 14**1 + c3* 14**2 + c4* 14**3 + c5* 14**4
#  Quem tiver a maior soma vence.

class HighCard():
  def __init__(self, lnum):
    self.numeros=lnum
  def AmI(self):
    return(True, sum([soma_q(i, self.numeros) for i in range(5)]))

