# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:20:11 2020

@author: nepaulr
"""
"""
importation de la librairie networkX
"""

import networkx as nx
import data2py as data


G = nx.Graph()
"""
Création des arcs entre les différents noeuds avec comme poids le temps entre chaque arrêts
"""

def createEdges():
    ligne1 = data.regular_path.split(" N ")
    ligne2 = data.regular_path2.split(" N ")
     
    for i in range(len(ligne1)-1):
        G.add_edge(ligne1[i], ligne1[i+1], nbarc = 1)
     
    for i in range(len(ligne2)-1):
        G.add_edge(ligne2[i], ligne2[i+1], nbarc = 1)

"""
Conversion d'une horaire passée en paramètres en format utilisé dans nos données (en seconde)
"""

def conversion(horaires):
    horaire=horaires.split(":")
    heure = int(horaire[0])
    heure = heure * 60
    minute = int(horaire[1])
    return heure + minute
        
"""
Conversion d'une horaire auformat des données en format utilisateur
"""
    
def conversionInverse(horaire):
    heure = horaire // 60
    minute = horaire %60
    return heure,minute
    
"""
Trouve l'horaire du prochain bus en fonction de l'arret, l'heure et la ligne où l'utilisateur se trouve  
"""

def trouveHoraire(départ):
    heure = input("Quelle heure est-il? \n")
    ligne = input("Sur quelle ligne êtes vous ? \n")
    direction = input("Dans quel sens voulez vous aller? \n")
    jour= input("Etes vous en vacances/week-end (oui ou non) ? \n")
    liste=[]
    hor=conversion(heure)
    if ligne == "1" and direction == "PARC_DES_GLAISINS" and jour == "non":
        date = data.regular_date_go0[0][départ]
    if ligne == "1" and direction == "LYCEE_DE_POISY" and jour == "non":   
        date = data.regular_date_back0[0][départ]
    if ligne == "1" and direction == "PARC_DES_GLAISINS" and jour=="oui":     
        date = data.we_holidays_date_go0[0][départ]
    if ligne == "1" and direction == "LYCEE_DE_POISY" and jour=="oui":   
        date = data.we_holidays_date_back0[0][départ]
    if ligne == "2" and direction == "CAMPUS" and jour == "non":
        date =  data.regular_date_go0[1][départ]
    if ligne == "2" and direction == "PISCINE-PATINOIRE" and jour == "non":
        date = data.regular_date_back0[1][départ]
    if ligne == "2" and direction == "CAMPUS" and jour=="oui":
        date = data.we_holidays_date_go0[1][départ]
    if ligne == "2" and direction == "PISCINE-PATINOIRE" and jour=="oui":
        date = data.we_holidays_date_back0[1][départ]
    for j in date:
        if j == "-":
            liste.append(".")
        else:
            liste.append(conversion(j))
    for elem in liste:
        if type(elem) != str:
            if (elem - hor > 0):
                return conversionInverse(elem)    
        
        
s
def conversionHorairesgo():
    for arret in data.regular_date_go0[0]:
        print(arret)
        liste=[]
        for j in data.regular_date_go0[0][arret]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(conversion(j))
                
        print(liste, end =",")
        print("\n")
        
    for arret in data.regular_date_go0[1]:    
        print(arret)
        liste=[]
        for j in data.regular_date_go0[1][arret]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(conversion(j))
       
        print(liste, end =",")
        print("\n")

def shortest(arret,arrive):
    return nx.shortest_path(G,arret,arrive)


if __name__ == "__main__":    
    createEdges()
    print(G.nodes)
    arret=input("A quel arrêt vous trouvez vous ? \n")
    arrive=input("A quel arrêt voulez vous aller ? \n")
    hor=trouveHoraire(arret)
    court=shortest(arret,arrive)
    print("Votre prochain bus passera à :",hor,end = "\n")
    print("Voici le chemin le plus court pour y arriver :", court)
    
    
    
  

    
