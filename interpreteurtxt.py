# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:07:48 2021

@author: klq93
"""

### Ce fichier contient les fonctions necessaires à la lecture de fichiers textes






#T: texte --- R: reel --- N: entier --- B: booleen --- #: commentaire
def Decapsule(argument):
    """
    Description : Permet de convertir une ligne de texte avec la bonne convention en une variable avec son type equivalent. Elle est necessaire au bon fonctionnement de LireSettings().
    ---
    variables d'entree :
    argument : Ligne de texte qui sera convertie dans le bon type.
    ---
    Variables renvoyees :
    Argument dans son bon type.
    """
    if argument[0] == "T": #texte
        return(argument.split(":")[1][0:-1])
    if argument[0] == "R": #reel
        return(float(argument.split(":")[1]))
    if argument[0] == "N": #entier
        return(int(argument.split(":")[1]))
    if argument[0] == "B": #booleen
        return(argument.split(":")[1][0:-1] == "True")
    if argument[0] == "#": #commentaire
        return [False]
    
def LireSettings(Fichier):
    """
    Description : Fait la transcription d'un fichier texte en un doctionnaire.
    ---
    Variables d'entree :
    Fichier : texte correspondant au nom du fichier.
    ---
    Variables renvoyees : 
    Dictionnaire contenant les variables introduites par le fichier texte.
    """
    Settings={} # dictionnaire qui sera renvoye 
    fichier=open(Fichier,'r') # ouverture du fichier 
    for i in fichier: # conversion et ajout dans le dictionnaire de chacune des lignes du fichier texte
        if Decapsule(i) != [False]:
            Settings.update({i.split(":")[0][2:-1] : Decapsule(i)})
    fichier.close()
    return Settings

def Typeur(val):   
    """
    Description : Cree la cle necessaire à l'ecriture d'un dictionnaire dans un fichier texte.
    ---
    Variables d'entree :
    val : variable au sens de python à convertir.
    ---
    Variables renvoyees : 
    Le texte à la convention de lecture.
    """
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
    """
    Description : Cree un fichier texte à partir d'un dictionnaire.
    ---
    Variables d'entree :
    Dictionnaire : Le dictionnaire à convertir.
    Fichier : Le nom du fichier texte qui sera cree.
    ---
    Variables renvoyees : 
    Le fichier texte.
    """
    fichier = open(Fichier,"w")
    for cle, valeur in Dictionnaire.items():
        fichier.write(Typeur(valeur)+"-"+cle+" :"+str(valeur)+"\n")
    fichier.close()

Param=LireSettings("settings.txt")