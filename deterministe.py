import numpy as np
import math as m
import Interpreteurtxt as i
import scipy.integrate as sp
import matplotlib.pyplot as plt

def lecture(entree="settings.txt"):
    """
    Crée un dictionnaire à partir d'un fichier texte

    Reçoit en argument le nom du fichier à importer, nommé par défaut 'settings.txt'

    Renvoie un dictionnaire contenant l'ensemble des données du fichier d'entrée
    """
    sortie=i.LireSettings(entree)
    return sortie

def ploteur(X,Y,labels,format,titreX="titreX",titreY="titreY",nom="figure",save=False):
    """
    Réalise un tracé à partir des listes fournies. Attention aux paramètres d'entrée :

    X et Y sont des listes de listes : pour un seul tracé on mettra [[points]] pour X et Y.
    Pour plusieurs tracés ce sera :[[points figure 1],[points figure 2],...,[points figure 3]]  


    titreX et titreY sont les titres que prendront les axes x et y.

    format : forme que prennent les courbes et les points. Pour en savoir plus, consulter https://www.w3schools.com/python/matplotlib_markers.asp
    
    nom est le nom que possédera la figure si elle est enregistrée

    save est un booléen qui s'il est vrai fera que ploteur enregistrera l'image au nom renseigné. L'image sera affiché à l'écran sinon.
    """
    n=len(X)
    plt.figure()
    for i in range(n):
        plt.plot(X[i],Y[i],format[i],label=labels[i])
    plt.grid()
    plt.legend()
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    if not save:
        plt.show()
    else :
        plt.savefig(nom)

Param=lecture()
def deterministe_case(
                      N = Param["population"],        
                      beta = Param["transmission"],
                      gamma = Param["recuperation"],
                      Tf = Param["temps de simulation"],
                      N0 = Param["population saine initiale"],
                      NP = Param["nombre d'évaluations"],
                      Ret = Param["population rétablie initiale"],
                      Renvoie_liste=True
                      ):
    """Lance une simulation d'épidémie. Les paramètres sont à modifier directement dans le fichier texte.
    
    Il n'y a pas besoin de les rentrer lors de l'appel de la fonction sauf si il y a une valeur particulière à modifier.
     
    Dans quel cas renseigner : deterministe_case(paramètre_à_changer = valeur)

    Si Renvoie_liste est réglé sur True, renvoie les listes S,I,R.
    Si Renvoie_liste est réglé sur False, renvoie seulement le rapport S(t=Tf)/N
    """

    I0 = N - N0 - Ret
    def pend(y,t,beta,gamma,N):
        S, I, R = y
        dydt = [-beta/N*I*S,beta/N*I*S-gamma*I,gamma*I]
        return dydt
    t = np.linspace(0,Tf,NP)
    y0 = [N0,I0,Ret]
    sol = sp.odeint(pend,y0,t,args=(beta,gamma,N))

    S = [i[0] for i in sol]
    I = [i[1] for i in sol]
    R = [i[2] for i in sol]
    if Renvoie_liste:
        return(S,I,R,t)
    else:
        return S[-1]/N 