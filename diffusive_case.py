from interpreteurtxt import Param
from random import gauss
from math import sqrt


def Diffusive_case(beta=Param["transmission"],
                   gamma=Param["recuperation"],
                   S_0=Param["population saine initiale"],
                   I_0=Param["population"]-Param["population saine initiale"]-Param["population retablie initiale"],
                   N=Param["population"], 
                   N_sim=Param["nombre de simulations"],
                   N_cal=Param["nombre d'evaluations"],
                   T=Param["temps de simulation"],
                   ):
    """
    Description : Lance une simulation d'epidemie par la resolution du système d'equations stochastiques.
    ---
    Variables d'entree : 
    S_0           : Population saine initiale. Fixe par defaut dans le fichier texte.
    I_0           : Population infectee initiale. Fixe par defaut dans le fichier texte.
    N             : Population totale. Fixe par defaut dans le fichier texte.
    N_sim         : Nombre de simulations. Fixe par defaut dans le fichier texte.
    N_cal         : Nombre d'evaluations (nombre de caluls). Fixe par defaut dans le fichier texte.
    T             : Temps final de la simulation. Fixe par defaut dans le fichier texte.
    beta          : Taux de transmission de la maladie. Fixe par defaut dans le fichier texte.
    gamma         : Taux de recuperation de la maladie. Fixe par defaut dans le fichier texte.
    ---
    Variables renvoyees :
    vecteur (S,I,T) où X correspond à un tableau de tableaux contenant (X(t=ti)) pour la simulation j.
    """
    ## creation des variables intermediaires 
    dt = T/(N_cal-1) # calcul de l'increment de temps 
    S_return=[[S_0] for i in range(N_sim)] # creation d'autant de cas initial qu'il y a de simulations
    I_return=[[I_0] for i in range(N_sim)] # creation d'autant de cas initial qu'il y a de simulations
    T=[[0] for i in range(N_sim)] # creation de l'echelle de temps
    
    ## calcul du schema   
    for i in range(N_sim): # realisation de N_sim simulations
        for j in range(N_cal-1): # realisation de N_cal-1 calculs (nous connaissons l'instant initial)
            dWi=gauss(0,dt) # calcul des bruits d'infection
            dWg=gauss(0,dt) # calcul des bruits de guerison
            if S_return[i][j]>0 and I_return[i][j]>0: # si l'epidemie ne s'arrete pas prematurement 
                # utilisation du schema pour calculer S 
                S_return[i].append(S_return[i][j]-beta/N*I_return[i][j]*S_return[i][j]*dt+sqrt(beta/N*I_return[i][j]*S_return[i][j])*dWi) 
                # utilisation du schema pour calculer I
                I_return[i].append(I_return[i][j]+(beta/N*I_return[i][j]*S_return[i][j]-gamma*I_return[i][j])*dt+sqrt(gamma*I_return[i][j])*dWg-sqrt(beta/N*I_return[i][j]*S_return[i][j])*dWi)
                T[i].append(dt*(j+1)) # increment de temps 
            else : # si l'epidemie s'arrete prematurement 
                break
    return(S_return,I_return,T) 

def temps_de_fin(S,T,pourcent=0.01):
    """
    Description : Determine le temps de fin d'une epidemie.
    ---
    Variables d'entree : 
    S             : Tableau contenant l'evolution temporelle des individus sains au cours d'une epidemie.
    T             : Tableau contenant les instants ou sont evalues les elements de S.
    pourcent      : pourcentage qui determine quand une epidemie se termine (quand S passe en dessous ce dit pourcentage vis a vis de sa premiere valeur).
    ---
    Variables renvoyees :
    Le temps ou l'epidemie est decretee finie.
    """
    SO=S[0] # condition initiale 
    limite = pourcent*SO # passe du pourcentage au S limite 
    for i in range(1,len(S)): # parcours de chacun des elements 
        if abs(S[i]-S[i-1])<0.01:
            return(T[i])
        if S[i]<limite:
            return(T[i]) 
    return 0

def temps_moyen(S,T):
    """
    Description : Determine le temps moyen de fin d'une epidemie.
    ---
    Variables d'entree : 
    S             : Tableau de tableaux contenant l'evolution temporelle des individus sains au cours d'une epidemie.
    T             : Tableau de tableaux contenant les instants ou sont evalues les elements de S.
    ---
    Variables renvoyees :
    Le temps moyen ou l'epidemie est decretee finie.
    """
    tm=0 # initialisation de la moyenne 
    n=len(S) 
    for i in range(n): # sommation des temps de fin de chacune des moyennes 
        tm=tm+temps_de_fin(S[i],T[i])
    return tm/n
    
def variance_temps(S,T):
    """
    Description : Determine la variance du temps moyen de fin d'une epidemie.
    ---
    Variables d'entree : 
    S             : Tableau de tableaux contenant l'evolution temporelle des individus sains au cours d'une epidemie.
    T             : Tableau de tableaux contenant les instants ou sont evalues les elements de S.
    ---
    Variables renvoyees :
    La variance temps moyen ou l'epidemie est decretee finie.
    """
    n = len(S)
    t=[temps_de_fin(S[i],T[i]) for i in range(n)] # obtention des temps de fin de chacune des simulations 
    m=temps_moyen(S,T) # calcul de la moyenne 
    moment =[(j-m)**2 for j in t] # calcul des moments 
    var = 1/n*sum(moment) # application de la formule de la variance 
    return var



