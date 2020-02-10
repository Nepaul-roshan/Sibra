# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:39:47 2020

@author: Roshan
"""
from Lignes import Lignes
import data2py as data

class Arret(Lignes):
    
    def __init__ (self, nom, direction, lignes=[], horaires=[]):
    
        self.horaires = horaires
        self.direction = direction
        self.nom = nom
        self.lignes = lignes
    
    
    def getDirection(self):
        return self.direction
    
    def getNom(self):
        return self.nom
    
    def getLigne(self, ligne:Lignes):
      liste= ligne.getNom_arrets()
      for arret in liste:
          if arret == self.nom:
              self.lignes.append(ligne.numero)
              return self.lignes
            
             
    def getHoraire_aller(self, ligne:Lignes):
        nom =ligne.getNom_arrets()
        for name in nom:
            if name == self.getNom():
                self.horaires = data.regular_date_go[name]
        return self.horaires
            
    def getHoraire_retour(self, ligne:Lignes):
        nom =ligne.getNom_arrets()
        for name in nom:
            if name == self.getNom():
                self.horaires = data.regular_date_back[name]
        return self.horaires    
    

    
    
arret = Arret('Meythet_Le_Rabelais','direct')
lig=Lignes(1) 
aa=arret.getHoraire_retour(lig)
#print(conversion(aa[0]))