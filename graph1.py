# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:07:22 2020

@author: nepaulr
"""

from node import Noeud

class Graph(Noeud):
    def __init__(self,nodes=[]):
        self.nodes=nodes
 
"""Ligne 1"""
       
n10=Noeud('LYCÉE_DE_POISY + POISY_COLLÈGE')
n11=Noeud('Vernod')
n12=Noeud('Meythet_Le_Rabelais')
n13=Noeud('Chorus')
n14=Noeud('Mandallaz')
n15=Noeud('GARE')
n16=Noeud('France_Barattes')
n17=Noeud('C.E.S._Barattes')
n18=Noeud('VIGNIÈRES')
n19=Noeud('Ponchy')
n110=Noeud('PARC_DES_GLAISINS')

"""Ligne 2 """

n20= Noeud('PISCINE-PATINOIRE')
n21= Noeud('Arcadium')
n22= Noeud('Parc_des_Sports')
n23= Noeud('Place_des_Romains')
n24= Noeud('Courier')
n25= Noeud('GARE')
n26= Noeud('Bonlieu')
n27= Noeud('Préfecture_Pâquier')
n28= Noeud('Impérial')
n29= Noeud('Pommaries')
n210= Noeud('VIGNIÈRES')
n211= Noeud('CAMPUS')

"""Ligne 1"""

n10.setSucc(n11)
n11.setPred(n10)
n11.setSucc(n12)
n12.setPred(n11)
n12.setSucc(n13)
n13.setPred(n12)
n13.setSucc(n14)
n14.setPred(n13)
n14.setSucc(n15)
n15.setPred([n24,n14])
n15.setSucc([n26,n16])
n16.setPred(n15)
n16.setSucc(n17)
n17.setPred(n16)
n17.setSucc(n18)
n18.setPred([n29,n17])
n18.setSucc([n211,n19])
n19.setPred(n18)
n19.setSucc(n110)
n110.setPred(n19)
        
        
"""Ligne 2 """

n20.setSucc(n21)
n21.setPred(n20)
n21.setSucc(n22)
n22.setPred(n21)
n22.setSucc(n23)
n23.setPred(n22)
n23.setSucc(n24)
n24.setPred(n23)
n24.setSucc(n25)
n25.setPred([n24,n14])
n25.setSucc([n26,n16])
n26.setPred(n25)
n26.setSucc(n27)
n27.setPred(n26)
n27.setSucc(n28)
n28.setPred(n27)
n28.setSucc(n29)
n29.setPred(n28)
n29.setSucc(n210)
n210.setPred([n29,n17])
n210.setSucc([n211,n19])
n211.setPred(n210)