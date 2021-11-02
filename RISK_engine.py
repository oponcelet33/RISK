#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:07:13 2021
https://fr.wikipedia.org/wiki/Risk
@author: TP
"""

import RISK_player as risk_p





#cartes objectifs (la même chose pourrait être faite pour les objectifs)
#par exemple:
objective = (
  'full Asia',          #0
  'full Europa',        #1
  'full Africa'         #2
  #etc...
  )


type_end_list = (
  'Game completed',
  'Game interrupted'
  )


class RISK_engine():
  def __init__(self, round_max=-1, players_init=None):
    self.round_max = round_max
    self.players_init = players_init
 
  #Fonction pour définir un seul joueur à l'écran
  def setup_1player(self, tag):
    print()
    print('--- setup player #{0} ---'.format(tag), end='')
    type_player = int(input('Quelle est la nature du joueur #{0}? (IA:0, Human:1) :'.format(tag)))
    if type_player == 0:
      type_player = 'IA'
      mode_IA = int(input('Quel est le mode de cette IA? (attack/defense:0, attack:1, defense:2) :'))
    else:
      type_player = 'Human'
      mode_IA = None
    name = input('Quel est le nom du joueur #{0}? :'.format(tag))
    print('--- end setup player #{0}'.format(tag))
    return risk_p.Player_RISK(type_player, tag, name=name, mode_IA=mode_IA)


  #Fonction pour définir les paramètres du jeu
  def setup_players_in_consol(self):
    print('-------- Manual game setup --------', end='')
    nb_players = int(input('Combien de joueurs: '))
    print('-------------------')
    self.player_list = list()
    for tag in range(nb_players):
      self.player_list.append(self.setup_1player(tag))


  #Fonction pour le lancement des tours de jeu
  def launch_turns(self):
    players_in_game = list(range(len(self.player_list))) #liste des joueurs en lice (le numéro du joueur est stocké)
    type_end = type_end_list[0]
    stop = False
    current_round = 0
    
    while not stop: #moteur des tours de jeu
      current_round += 1
      print('----- round {0:d} -----'.format(current_round))
      for i, p in enumerate(self.player_list): #moteur d'un tour de jeu (sur chaque joueur initial)
        if not p.eliminated: #ne jouent que ceux encore en jeu
          if p.play_turn(): #tour de jeu d'un joueur (retourne l'issue de son tour: True si éliminé)
            players_in_game.remove(i)  #enlève le joueur de la liste en lice s'il a foiré
        if len(players_in_game) == 1: #on teste s'il ne reste plus qu'un joueur en lice avant que le tour de jeu ne soit terminé
          break #on sort de la boucle for si c'est le cas
      stop = (current_round == self.round_max) or (len(players_in_game) == 1) #on continue ou pas
      
    winner = self.player_list[players_in_game[0]] #player_in_game[0] est normalement l'ID du dernier et unique joueur en lice
    return winner, type_end, current_round #retourne une liste d'infos de fin de partie

  
  #Fonction pour lancer le jeu
  def RISK_setup_and_go(self):
    print('---------------------------------------------')
    print('----------------  RISK GAME  ----------------')
    print('---------------------------------------------')
    print()
    if self.players_init == None:
      self.setup_players_in_consol() #on passe par la console pour créer les joueurs
    else:
      print('------- Automatic game setup ------')
      self.player_list = list() #ici les joueurs sont créés automatiquement à partir du dict players_init
      for tag, p in enumerate(self.players_init): #on itère sur les éléments du dictionnaire 
        self.player_list.append(risk_p.Player_RISK(p[0], tag, name=p[1], mode_IA=p[2])) #on ajoute un objet Player_RISK(...) au set
      print('Nombre de joueurs: {0}'.format(len(self.player_list)))
    #
    # Code ici pour assigner des états, des objectifs aléatoirement aux players
    #
    print('------------ end setup ------------')
    print()
    #puis on lance le jeu
    nb_players_initial = len(self.player_list)
    winner, type_end, rounds = self.launch_turns()
    print('---------------------------------------------')
    print('----------------  GAME OVER  ----------------')
    print('---------------------------------------------')
    print('Nombre initial de joueurs:', nb_players_initial)
    print('Type end of game:', type_end)
    print('Nombre de tours:', rounds)
    print('The winner is: ', winner)
  
  

#une liste de joueurs prédéfinie pour éviter de remplir sans arrêt les input lors de tests
predefined_players = [
  ('IA', 'IA 0', risk_p.IA_mode[0]),
  ('Human', 'moi', None),
  ('Human', 'toi', None),
  ('IA', 'IA 1', risk_p.IA_mode[1]),
  ('IA', 'IA 2', risk_p.IA_mode[2]),
  ('Human', 'lui', None),
  ('Human', 'toto', None),
  ('IA', 'IA 3', risk_p.IA_mode[0])
  ]




if __name__ == '__main__':
  if True: #True pour la version liste de joueurs automatique / False pour appeler les input
    R = RISK_engine(100, predefined_players*(125))
  else:
    R = RISK_engine(25)
  
  R.RISK_setup_and_go()
  
  
  
  
  
  