from numpy import linspace
from interpreteurtxt import Param
from scipy.integrate import odeint

### Ce fichier contient le code necessaire pour la realisation du modèle deterministe


def deterministe_case(
                      N = Param["population"],        
                      beta = Param["transmission"],
                      gamma = Param["recuperation"],
                      Tf = Param["temps de simulation"],
                      N0 = Param["population saine initiale"],
                      NP = Param["nombre d'evaluations"],
                      Ret = Param["population retablie initiale"],
                      Renvoie_liste = True
                      ):
    """
    Description : Lance une simulation d'epidemie par la resolution du système d'equations deterministe.
    ---
    Variables d'entree : 
    N             : Population totale. Fixe par defaut dans le fichier texte.
    beta          : Taux de transmission de la maladie. Fixe par defaut dans le fichier texte.
    gamma         : Taux de recuperation de la maladie. Fixe par defaut dans le fichier texte.
    Tf            : Temps final de la simulation. Fixe par defaut dans le fichier texte.
    N0            : Population saine initiale. Fixe par defaut dans le fichier texte.
    Np            : Nombre d'evaluations (nombre de caluls). Fixe par defaut dans le fichier texte.
    Ret           : Population retablie initiale. Fixe par defaut dans le fichier texte.
    Renvoie_liste : Boleen decidant du contenu renvoye par l'appel. True par defaut.
    ---
    Variables renvoyees :
    Si Renvoie_liste est regle sur True, renvoie les listes S,I,R..
    Si Renvoie_liste est regle sur False, renvoie seulement le rapport S(t=Tf)/N.
    """

    I0 = N - N0 - Ret #calcul du nombre d'infectes initialement par conservation de la population

    def pend(y,t,beta,gamma,N): #fonction aux notations adaptees à la convention scipy. Sert à creer le système d'equation (se referer à la documentation scipy via help(sp.odeint))
        S, I, R = y
        dydt = [-beta/N*I*S,beta/N*I*S-gamma*I,gamma*I]
        return dydt

    t = linspace(0,Tf,NP) #creation de l'intervalle de temps
    y0 = [N0,I0,Ret] #creation du vecteur de conditions initiales (convention scipy)
    sol = odeint(pend,y0,t,args=(beta,gamma,N)) #resolution du système d'equation

    S = [i[0] for i in sol] #vecteur contenant le nombre de personnes saines pour chaque instant de calcul
    I = [i[1] for i in sol] #vecteur contenant le nombre de personnes infectees pour chaque instant de calcul
    R = [i[2] for i in sol] #vecteur contenant le nombre de personnes retablies pour chaque instant de calcul
    if Renvoie_liste: #conditionnement pour le renvoi 
        return(S,I,R,t)
    else:
        return S[-1]/N 
