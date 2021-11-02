#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:41:42 2021
http://jeuxstrategie.free.fr/Risk_complet.php
@author: TP
"""

import random as rd


objective_cards = { 
  0 : "Vous devez conquérir 18 territoires et occuper chacun d'eux avec deux armées au moins",
  1 : "Vous devez conquérir en totalité l'Amérique du Nord et l'Afrique",
  2 : "Vous devez conquérir en totalité l'Europe et l'Amérique du sud plus un troisième continent au choix",
  3 : "Vous devez conquérir en totalité l'Europe et l'Océanie plus un troisième continent au choix",
  4 : "Vous devez conquérir 24 territoires aux choix",
  5 : "Vous devez conquérir en totalité l'Amérique du Nord et l'Océanie",
  6 : "Vous devez conquérir en totalité l'Asie et l'Afrique",
  7 : "Vous devez conquérir en totalité l'Asie et l'Amérique du sud",
  8 : "Vous devez détruire les armées jaunes. Si vous êtes vous même le propriétaire des armées jaunes ou si le joueur qui en est "
      "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires.",
  9 : "Vous devez détruire les armées rouges. Si vous êtes vous même le propriétaire des armées rouges ou si le joueur qui en est "
      "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires.",
  10 : "Vous devez détruire les armées bleues. Si vous êtes vous même le propriétaire des armées bleues ou si le joueur qui en est "
       "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires.",
  11 : "Vous devez détruire les armées noires. Si vous êtes vous même le propriétaire des armées noires ou si le joueur qui en est "
       "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires.",
  12 : "Vous devez détruire les armées violettes. Si vous êtes vous même le propriétaire des armées violettes ou si le joueur qui en est "
       "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires.",
  13 : "Vous devez détruire les armées vertes. Si vous êtes vous même le propriétaire des armées vertes ou si le joueur qui en est "
       "propriétaire est éliminé par un autre joueur, votre but devient automatiquement de conquérir 24 territoires."
  }


if False:
  (fantassin, cavalier, canon) = (0, 1, 2)
else:
  (fantassin, cavalier, canon) = ('fantassin', 'cavalier', 'canon')

territory_cards = {
  'Afghanistan'           : fantassin,
  'Afrique du Nord'       : fantassin,
  'Afrique du Sud'        : canon,
  "Afrique de l'Est"      : canon,#ou 'Afrique orientale' dans certains plateaux
  'Alaska'                : fantassin,
  'Alberta'               : fantassin,
  'Amérique Centrale'     : cavalier,
  'Argentine'             : fantassin,
  'Australie Occidentale' : canon,
  'Australie Orientale'   : fantassin,
  'Brésil'                : canon,
  'Chine'                 : cavalier,
  'Congo'                 : cavalier,
  'Égypte'                : fantassin,
  "États de l'Est"        : canon,
  "États de l'Ouest"      : fantassin,
  'Europe du Nord'        : cavalier,
  'Europe du Sud'         : cavalier,
  'Europe Occidentale'    : fantassin,
  'Grande-Bretagne'       : cavalier,
  'Groenland'             : cavalier,
  'Inde'                  : fantassin,
  'Indonésie'             : cavalier,
  'Islande'               : fantassin,
  'Japon'                 : fantassin,
  'Kamtchatka'            : cavalier,
  'Madagascar'            : fantassin,
  'Mongolie'              : canon,
  'Moyen-Orient'          : canon,
  'Nouvelle-Guinée'       : cavalier,
  'Ontario'               : cavalier,
  'Oural'                 : cavalier,
  'Pérou'                 : cavalier,
  'Québec'                : canon,
  'Scandinavie'           : canon,
  'Siam'                  : canon,
  'Sibérie'               : canon,
  'Tchita'                : fantassin,
  'Territoires du Nord-Ouest' : canon,
  'Ukraine'               : canon,
  'Venezuela'             : canon,
  'Yakoutie'              : cavalier
  }


def random_cards(set_of_cards, n):
  sub_set_keys = set()
  card_keys = tuple(rd.sample(tuple(set_of_cards), n))
  sub_set_keys.update(card_keys)
  return sub_set_keys
  
  


if __name__ == '__main__':
  print('Cartes objectifs: --------------------')
  for key, value in objective_cards.items():
    print(key, value)
  print()
  print('Cartes Territoires: ------------------')
  for i, (key, value) in enumerate(territory_cards.items()):
    print(i, key, value)
  print()
  n = 5
  print('Tirage de {0} carte objectif:'.format(1), random_cards(objective_cards,1))
  print('Tirage de {0} cartes territoire:'.format(n), random_cards(territory_cards,n))
  