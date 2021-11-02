#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:46:10 2021
https://fr.wikipedia.org/wiki/Risk
@author: TP
"""

import random as rd
import time as time


#Utile aussi de préparer des tuples d'autres formes tels que
IA_mode = (
  'attack/defense',    #0
  'attack',            #1
  'defense'            #2
  #etc...
  )

pause_secondes = 0.001


############# class Player_RISK pour encapsuler toutes les données propres à un joueur ###############
#__init__ est la fonction (constructeur) qui automatiquement appelée lors de la construction d'un objet de la class
#Par exemple lorsqu'on exécute : p = Player_RISK('IA', 2, name='Deep Blue', mode_IA='attack')
#Il est donc possible de passer d'autres éléments tels que la matrice de jeu, la carte objectif etc
#pour que les méthodes de la class Player_RISK puissent y accéder à n'importe quel moment
#la création d'attribut self.xxx = ... permet de créer des champs internes qui se conserveront pendant toute
#la durée de vie de l'objet (voir par ex. self.type_player, self.tag, self.name ci-dessous)
class Player_RISK():
  '''
  class encapsulant toutes les données définissant un joueur
  self.type_player élément de ['IA', 'Human']
  '''
  nb_player_max = 6 #constante commune à tous les instances de la class (pas de self devant)
  
  def __init__(self, type_player, tag, name=None, mode_IA=None):
    self.type_player = type_player
    self.tag = tag
    self.name = name
    if mode_IA == None:
      self.mode_IA = 'attack/defense'
    else:
      self.mode_IA = mode_IA
    self.territory_cards = set()
    self.objective_card = None #A initialiser lors d'un tirage ou bien à la construction de l'objet
    self.eliminated = False
    
  def __str__(self): #représentation sous forme de string de l'objet (appelée par exemple par print)
    return 'Player #{0:d}, name: {1}, type: {2}, mode IA: {3}'.format(self.tag, self.name, self.type_player, self.mode_IA)
  
  def play_turn(self):
    print("player #{0:d} '{1}' has played dice : ".format(self.tag, self.name), end='')
    #code du déroulement d'un tour de jeu
    #ici exemple d'un tirage de dés (si 2 -> éliminé)
    dice = rd.randint(2,12)
    self.eliminated = dice == 2 #si le joueur fait 2 son statut 'eliminated' passe à True
    if self.eliminated:
      print('{0:d} | eliminated'.format(dice))
    else:
      print('{0:d}'.format(dice))
    #fin code du déroulement d'un tour de jeu
    time.sleep(pause_secondes) #pour voir l'affichage progresser (le temps de pause est en secondes)
    return self.eliminated #on retourne le statut 'eliminated' pour utilisation avec un if (voir dans launch_game)
###################----- end class Player_RISK -----#######################
###########################################################################


if __name__ == '__main__':
  print(Player_RISK.nb_player_max)