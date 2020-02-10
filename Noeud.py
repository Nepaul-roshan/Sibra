# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:48:20 2020

@author: Kévin
"""

G1= dict()
G1['LYCÉE_DE_POISY + POISY_COLLÈGE'] = [' ', 'Vernord']
G1['Vernod'] = ['LYCÉE_DE_POISY + POISY_COLLÈGE','Meythet_Le_Rabelais']
G1['Meythet_Le_Rabelais'] = ['Vernod','Chorus']
G1['Chorus'] = ['Meythet_Le_Rabelais','Mandallaz']
G1['Mandallaz'] = ['Chorus','GARE']
G1['GARE'] = ['Mandallaz','France_Barattes']
G1['France_Barattes'] = ['GARE','C.E.S._Barattes']
G1['C.E.S._Barattes'] = ['France_Barattes','VIGNIÈRES']
G1['VIGNIÈRES'] = ['C.E.S._Barattes','Ponchy']
G1['Ponchy'] = ['VIGNIÈRES','PARC_DES_GLAISINS']
G1['PARC_DES_GLAISINS'] = ['Ponchy', ' ']

G2 = dict()
G2['PISCINE-PATINOIRE'] = [' ','Arcadium']
G2['Arcadium'] = ['PISCINE-PATINOIRE','Parc_des_Sports']
G2['Parc_des_Sports'] = ['Arcadium','Place_des_Romains']
G2['Place_des_Romains'] = ['Parc_des_Sports','Courier']
G2['Courier'] = ['Place_des_Romains','GARE']
G2['GARE'] = ['Courier','Bonlieu']
G2['Bonlieu'] = ['GARE','Préfecture_Pâquier']
G2['Préfecture_Pâquier'] = ['Bonlieu','Impérial']
G2['Impérial'] = ['Préfecture_Pâquier','Pommaries']
G2['Pommaries'] = ['Impérial','VIGNIÈRES']
G2['VIGNIÈRES'] = ['Pommaries', 'CAMPUS']
G2['CAMPUS'] = ['VIGNIÈRES', ' ' ]

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

n10.setSucc(n11)
n11.setPred(n10)
n11.setSucc(n12)
n12.setPred(n11)
n12.setSucc(n13)
n13.setPred(n12)
n13.setSucc(n14)
n14.setPred(n13)
n14.setSucc(n15)
n15.setPred(n14)
n15.setSucc(n16)
n16.setPred(n15)
n16.setSucc(n17)
n17.setPred(n16)
n17.setSucc(n18)
n18.setPred(n17)
n18.setSucc(n19)
n19.setPred(n18)
n19.setSucc(n110)
n110.setPred(n19)











