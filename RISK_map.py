#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:29:00 2021
https://fr.wikipedia.org/wiki/Risk
@author: TP
"""
import RISK_data_map as risk_dm
import RISK_cards as risk_c


class Territory():
  def __init__(self, tag, name, continent_name, contact_names):
    self.tag = tag
    self.name = name
    self.continent_name = continent_name
    self.contact_names = contact_names

  def __str__(self): #fonction appelée lors de l'appel d'une représentation type texte de l'objet
    s = 'tag {0} / {1} - continent = {2}, contacts = {3}'.format(self.tag, self.name,
                                                                 self.continent_name, str(self.contact_names))
    return s
    
  def is_in_contact(self, territory_name):
    return territory_name in self.contact_names
##### END CLASS Territory #####


class Map_RISK():
  def __init__(self, world_map):
    self.world_map = world_map
    self.continent_names = tuple(world_map) #crée un tuple avec la liste des noms des continents
    territory_names = list() #liste des noms des territoires (liste indexée potentiellement utile plus tard)
    self.territories = dict() #dictionnaire des Territory avec comme clés leur nom (stockage non indexé)
    tag = 0
    for continent_name, continent in world_map.items(): #on construit le dictionnaire des objets Territory
      for territory_name, contacts in continent.items():
        territory_names.append(territory_name)
        self.territories[territory_name] = Territory(tag, territory_name, continent_name, contacts)
        tag += 1
    self.territory_names = tuple(territory_names) #tuple des noms des territoires (liste immuable)

  def __str__(self):
    s = '-------------------- WORLD CONSTITUTION --------------------\n'
    s += 'Continents: '
    s += str(self.continent_names) + '\n'
    s += '----- Territoires par continent -----\n'
    for continent_name, continent in self.world_map.items():
      s += continent_name + ': ' + str(tuple(continent)) + '\n'
    s += '--------------------\n'
    s += 'Liste complète des territoires:\n' + str(self.territory_names)
    s += '\n--------------------\n'
    s += 'Détails de chaque territoire:\n'
    for territory in self.territories.values():
      s += str(territory) + '\n'
    s += '------------------ END WORLD CONSTITUTION ------------------\n'
    return s
  
  def __getitem__(self, key):
    '''
    implémentation de l'opérateur Map_RISK[key] pour accéder en lecture seule
    à un Territory de la map, soit par son nom (key est une string) soit par son tag (key est un entier)
    '''
    if not isinstance(key, str):
      #key est alors un int
      key = self.territory_names[key]
    return self.territories[key]
  
  def __iter__(self):
    '''
    iterateur sur les objets Territory stockés dans la variable self.territories
    '''
    return iter(self.territories.values())
  
  def get_contacts(self, territory, level=1):
    '''
    crée la liste des contacts d'un territoire (sous forme d'un ensemble de string)
    jusqu'à une profondeur level.
    A VÉRIFIER SUR PLUSIEURS EXEMPLES POUR VOIR SI CELA FONCTIONNE BIEN 
    '''
    contacts = set()
    if level > 0: #si level == 0 -> on arrête la récursion
      if isinstance(territory, Territory):
        territory = territory.name #si territory est une instance de Territory
      else:
        pass #si territory est le nom sous forme de string du territoire ou son tag (int)
      for contact_name in self[territory].contact_names:
        contacts.update(self.get_contacts(contact_name, level-1))
        contacts.add(contact_name)
      #A cause de la récursion territory peut faire partie de la liste des contacts
      #on l'enlève en fin de traitement
      contacts.discard(self[territory].name)
    return contacts
        
##### END CLASS Map_RISK #####





if __name__ == '__main__':
  M = Map_RISK(risk_dm.WORLD)
  print(M)
  print()
  print(M['Ukraine'])
  print(M[5])
  print()
  territory = 0
  level = 0
  c = M.get_contacts(territory, level)
  print('Contacts de niveau {0} de {1}: '.format(0, M[territory].name), c)
  c = M.get_contacts(territory, level+1)
  print('Contacts de niveau {0} de {1}: '.format(1, M[territory].name), c)
  c = M.get_contacts(territory, level+2)
  print('Contacts de niveau {0} de {1}: '.format(2, M[territory].name), c)
  c = M.get_contacts(territory, level+3)
  print('Contacts de niveau {0} de {1}: '.format(3, M[territory].name), c)
  print()
  print('Vérification des cartes territoires -----')
  for i, t in enumerate(M):
    print("carte #{0} '{1}': {2}".format(i, t.name, risk_c.territory_cards[t.name]))
    