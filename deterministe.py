import numpy as np
import math as m
from Interpreteurtxt import Param
import scipy.integrate as sp

### Ce fichier contient le code necessaire pour la réalisation du modèle deterministe


def deterministe_case(
                      N = Param["population"],        
                      beta = Param["transmission"],
                      gamma = Param["recuperation"],
                      Tf = Param["temps de simulation"],
                      N0 = Param["population saine initiale"],
                      NP = Param["nombre d'évaluations"],
                      Ret = Param["population rétablie initiale"],
                      Renvoie_liste = True
                      ):
    """
    Description : Lance une simulation d'épidémie par la résolution du système d'équations déterministe.
    ---
    Variables d'entrée : 
    N             : Population totale. Fixé par défaut dans le fichier texte.
    beta          : Taux de transmission de la maladie. Fixé par défaut dans le fichier texte.
    gamma         : Taux de récupération de la maladie. Fixé par défaut dans le fichier texte.
    Tf            : Temps final de la simulation. Fixé par défaut dans le fichier texte.
    N0            : Population saine initiale. Fixé par défaut dans le fichier texte.
    Np            : Nombre d'évaluations (nombre de caluls). Fixé par défaut dans le fichier texte.
    Ret           : Population rétablie initiale. Fixé par défaut dans le fichier texte.
    Renvoie_liste : Boléen décidant du contenu renvoyé par l'appel. True par défaut.
    ---
    Variables renvoyées :
    Si Renvoie_liste est réglé sur True, renvoie les listes S,I,R..
    Si Renvoie_liste est réglé sur False, renvoie seulement le rapport S(t=Tf)/N.
    """

    I0 = N - N0 - Ret #calcul du nombre d'infectés initialement par conservation de la population

    def pend(y,t,beta,gamma,N): #fonction aux notations adaptées à la convention scipy. Sert à créer le système d'équation (se référer à la documentation scipy via help(sp.odeint))
        S, I, R = y
        dydt = [-beta/N*I*S,beta/N*I*S-gamma*I,gamma*I]
        return dydt

    t = np.linspace(0,Tf,NP) #création de l'intervalle de temps
    y0 = [N0,I0,Ret] #création du vecteur de conditions initiales (convention scipy)
    sol = sp.odeint(pend,y0,t,args=(beta,gamma,N)) #résolution du système d'équation

    S = [i[0] for i in sol] #vecteur contenant le nombre de personnes saines pour chaque instant de calcul
    I = [i[1] for i in sol] #vecteur contenant le nombre de personnes infectées pour chaque instant de calcul
    R = [i[2] for i in sol] #vecteur contenant le nombre de personnes rétablies pour chaque instant de calcul
    if Renvoie_liste: #conditionnement pour le renvoi 
        return(S,I,R,t)
    else:
        return S[-1]/N 
