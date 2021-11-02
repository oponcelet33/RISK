#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:33:34 2021
https://fr.wikipedia.org/wiki/Risk
@author: TP
"""

#dictionnaire du monde (dictionnaire de dictionnaires):
# 1er niveau de clé : continent
# 2e niveau de clé : territoire
# valeurs : liste des territoires en contact avec le territoire de la seconde clé
WORLD = {
  'EUROPE' : {
    'Grande-Bretagne'    : ('Islande', 'Europe du Nord', 'Scandinavie', 'Europe Occidentale'),
    'Islande'            : ('Grande-Bretagne', 'Groenland'),
    'Europe du Nord'     : ('Grande-Bretagne', 'Scandinavie', 'Europe du Sud', 'Ukraine', 'Europe Occidentale'),
    'Scandinavie'        : ('Grande-Bretagne', 'Islande', 'Europe du Nord', 'Ukraine'),
    'Europe du Sud'      : ('Europe du Nord', 'Ukraine', 'Europe Occidentale', 'Moyen-Orient', 'Égypte'),
    'Ukraine'            : ('Europe du Nord', 'Scandinavie', 'Europe du Sud', 'Afghanistan', 'Moyen-Orient', 'Oural'),
    'Europe Occidentale' : ('Grande-Bretagne', 'Europe du Nord', 'Europe du Sud', 'Afrique du Nord')
    },
  'ASIE' : {
    'Afghanistan' : (),
    'Chine' : (),
    'Inde' : (),
    'Tchita' : (),
    'Japon' : (),
    'Kamtchatka' : (),
    'Moyen-Orient' : (),
    'Mongolie' : (),
    'Siam' : (),
    'Sibérie' : (),
    'Oural' : (),
    'Yakoutie' : ()
    },
  'AMÉRIQUE DU NORD' : {
    'Alaska' : (),
    'Alberta' : (),
    'Amérique Centrale' : (),
    "États de l'Est" : (),
    'Groenland' : (),
    'Territoires du Nord-Ouest' : (),
    'Ontario' : (),
    'Québec' : (),
    "États de l'Ouest" : ()
    },
  'AMÉRIQUE DU SUD' : {
    'Argentine' : (),
    'Brésil' : (),
    'Pérou' : (),
    'Venezuela' : ()
    },
  'AFRIQUE' : {
    'Congo' : (),
    "Afrique de l'Est" : (),#ou 'Afrique orientale' dans certains plateaux
    'Égypte' : (),
    'Madagascar' : (),
    'Afrique du Nord' : (),
    'Afrique du Sud' : ()
    },
  'OCÉANIE' : {
    'Australie Orientale' : (),
    'Indonésie' : (),
    'Nouvelle-Guinée' : (),
    'Australie Occidentale' : ()
    } 
  }


def get_list_territories(W, continents=None):
  '''
  continents : liste de noms de continents à partir desquels construire la liste, par exemple ['AMÉRIQUE DU NORD', 'OCÉANIE']
               si = None alors on prend tous les continents du monde
  '''
  territories = list()
  #on récupère la liste des noms des continents pour extraction de leurs territoires
  if continents == None: continent_names = tuple(W.keys())
  else: continent_names = continents
  #on itère sur chaque continent concerné
  for c_name in continent_names:
    #W[c_name] est le sous-dictionnaire stocké à la clé-continent cname
    #list(W[c_name]) retourne la liste des clés de ce dictionnaire (les noms des territoires)
    territories.extend(list(W[c_name])) #on ajoute les éléments à la liste (attention à ne pas utiliser append qui lui rajoute la liste comme un nouvel élément)
  return tuple(territories)


def get_continent(W, territory):
  for continent_name, continent_dict in W.items():
    if territory in continent_dict:
      return continent_name

def get_list_contacts(W, territory):
  continent_name = get_continent(W, territory)
  return W[continent_name][territory]

    

if __name__ == '__main__':
  print('Liste des continents:', list(WORLD.keys()))
  print()
  print('Liste des territoires pas continent:')
  for continent_name, territories in WORLD.items():
    print('Territoires de {0}:'.format(continent_name), list(territories.keys()))
  print()
  print('Liste des contacts de chaque territoire ---------------------')
  for continent_name, territories in WORLD.items():
    print('Territoires de {0}:'.format(continent_name))
    for territory_name, contacts in territories.items():
      print('Contacts de {0}:'.format(territory_name), contacts)
    print('END de {0}:------'.format(continent_name))
  
  print()
  L = get_list_territories(WORLD)
  print('Liste complète des {0} territoires ({1} continents):'.format(len(L), len(WORLD.keys())), L)
  L = get_list_territories(WORLD, ['EUROPE', 'OCÉANIE'])
  print('Liste complète des {0} territoires ({1} continents):'.format(len(L), '2'), L)
  
  print(get_continent(WORLD, 'Kamtchatka'))
  print(get_continent(WORLD, 'Madagascar'))
  print(get_continent(WORLD, 'Europe du Sud'))
  print(get_continent(WORLD, 'Nouvelle-Guinée'))
  print(get_list_contacts(WORLD, 'Grande-Bretagne'))
  print(get_list_contacts(WORLD, 'Scandinavie'))
  print(get_list_contacts(WORLD, 'Europe du Sud'))
  print(get_list_contacts(WORLD, 'Europe du Nord'))