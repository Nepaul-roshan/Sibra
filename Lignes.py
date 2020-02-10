# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:36:37 2020

@author: nepaulr
"""
import data2py as data

class Lignes():
    
    def __init__(self,numero,arrets=[]):
            self.numero = numero
            self.arrets = arrets
        
    def getNom_arrets(self):
        arret= data.regular_path.split(" N ")
        for a in arret:
            self.arrets.append(a)
        return self.arrets
    
    def getNumero(self):
        return self.numero

    def __str__(self):
        return self.arrets





aaaret = Lignes(1)
nomArret = aaaret.getNom_arrets()
#print(nomArret)