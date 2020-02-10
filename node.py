# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:07:07 2020

@author: nepaulr
"""

class Noeud():
    
    def __init__ (self, nom, pred=[], succ=[], lignes=[]):
        self.nom = nom
        self.lignes = lignes
        

    def setSucc(self,succ):
        self.succ = succ
    
    def setPred(self,pred):
        self.pred = pred
        
        
    def getNom(self):
        return self.nom
    
    def getLigne(self):
        return self.lignes
    
    def getPred(self):
        return self.pred.getNom()
    
    def getSucc(self):
        return self.succ.getNom()
    
    
    def __str__(self):
        return self.nom


n=Noeud('Meythet')
n1=Noeud('Vernod')
n2=Noeud('Gare')

n.setPred(n1)
n.setSucc(n2)

print(n.getSucc())