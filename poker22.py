#!/usr/bin/python

import sys
from defs_lambs import *
from pokerhand import *
from cartas_valid import *

# Função principal e entry point do programa Poker22
# Neste código temos:
#	1) Verificação dos argumentos da linha de comando
#	2) Validação da mão de cartas (contra cartas inválidas, repetidas etc)
#	3) Execução efetiva do ranking
#
# Este programa é executado pela linha de comando como:
#  > python poker22  <parametros>
# Exemplo:
#  > python poker22 --help
#	

def main():

# Verificação dos parametros, versão, helps e etc
# definições se encontram no módulo defs_lambs.py

  args = sys.argv[1:]

  if not args:
    sair_com_codigo(1)

  if args[0] == '--help':
    sair_com_codigo(0)

  if args[0] == '--versao':
    print ("\n\n", versao, versao1)
    sys.exit(0)

  if args[0] == '--minhamao':
    minhamao = args[1]
    del args[0:2]
    print ("\n\nMinha mão =>\t\t\t", minhamao)

  if not len(args) == 2:
    sair_com_codigo(1)
  
  if args[0] == '--advmao':
    advmao = args[1]
    del args[0:2]
    print ("Adversário mão =>\t\t", advmao)

  else: 
    sair_com_codigo(1)

# Validação das Cartas através da classe  ValidMao

  if not ValidMao(minhamao).AmI() or not ValidMao(advmao).AmI():
    print (" \nErro: Mãos não estão formadas corretamente!!!\nExemplo de Mão: 'KS KH KD 2C 2D'\n")
    sys.exit(1)

  if not ValidMao(minhamao).Entremaos(advmao):
    print (" \nErro: Adversários tem cartas iguais!!!\n")
    sys.exit(1)

  print ("Mãos válidas!!!")     

# Execute o ranking
  minha_x_adv = PokerHand(minhamao).compare_with(PokerHand(advmao))
  print ("Resultado  minhamao x  advmao => ", Resultado_string[minha_x_adv])


if __name__ == "__main__":
  main()

