# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:07:48 2021

@author: klq93
"""

#### partie indépendante 1






#T: texte --- R: réel --- N: entier --- B: booléen --- L:
def Decapsule(argument):
    if argument[0] == "T":
        return(argument.split(":")[1][0:-1])
    if argument[0] == "R":
        return(float(argument.split(":")[1]))
    if argument[0] == "N":
        return(int(argument.split(":")[1]))
    if argument[0] == "B":
        return(argument.split(":")[1][0:-1] == "True")
#    if argument[0] == "L":
#        return listeur(argument.split(":")[1])
    if argument[0] == "#":
        return [False]
    
def LireSettings(Fichier):
    Settings={}
    fichier=open(Fichier,'r')
    for i in fichier:
        if Decapsule(i) != [False]:
            Settings.update({i.split(":")[0][2:-1] : Decapsule(i)})
    fichier.close()
    return Settings

def Typeur(val):
    if type(val) == str:
        return "T"
    if type(val) == bool:
        return "B"
    if type(val) == float:
        return "R"
    if type(val) == list:
        return "L"
    if type(val) == int:
        return "N"
    

def PushSettings(Dictionnaire,Fichier):
    fichier = open(Fichier,"w")
    for cle, valeur in Dictionnaire.items():
        fichier.write(Typeur(valeur)+"-"+cle+" :"+str(valeur)+"\n")
    fichier.close()

