from interpreteurtxt import Param
from random import random
from math import log

### Dans ce fichier, on rentrera le code qui sera implique pour la question 6


# question a
def lambd(S,
          I,
          N     = Param["population"],        
          beta  = Param["transmission"],
          gamma = Param["recuperation"],
        ):

  """
  Description : Calcule lambda.
  ---
  Variables d'entree :
  S     : nombre d'individus sains.
  I     : nombre d'individus infectees.
  N     : population totale.
  beta  : Taux de transmission de la maladie. Fixe par defaut dans le fichier texte.
  gamma : Taux de recuperation de la maladie. Fixe par defaut dans le fichier texte.
  ---
  Variables renvoyees : 
  lambda.
  """
  return beta/N*S*I+gamma*I #calcul de lambda à partir de la formule (8) 

#question b
def Delta_T(lamb):
  """
  Description : Calcule un increment temporel aleatoirement tire d'une distribution exponentielle.
  ---
  Variables d'entree :
  lamb : lambda.
  Variables renvoyees :
  L'increment de temps.
  """
  return -log(random())/lamb #calcul de DT à partir de la note 3 
# partiellement question c 
def pi(S,
       I,
       N     = Param["population"],
       beta  = Param["transmission"],
       gamma = Param["recuperation"]
       ):
  """
  Description : Calcule la probabilite de l'evenement "pendant l'instant Delta t, il y a eu unne infection".
  ---
  Variables d'entree
  S     : Nombre d'individus sains.
  I     : Nombre d'individus infectes.
  N     : Population totale.
  beta  : Facteur de transmission.
  gamma : Facteur de recuperation.
  ---
  Variables renvoyees
  la probabilite pi.
  """
  return beta*S*I/N/lambd(S,I,N,beta,gamma) #calcul de pi 


#fin de la question c et questions d et e 
def T_plus_Delta_T(t,
                   S,
                   I,
                   N     = Param["population"],
                   beta  = Param["transmission"],
                   gamma = Param["recuperation"]
                   ):
  """
  Description : fait evoluer la situation de l'epidemie à l'instant t à celui t+dt
  ---
  Variables d'entree :
  t     : instant où la fonction est appelee.
  S     : Nombre d'individus sains.
  I     : Nombre d'individus infectes.
  N     : Population totale.
  beta  : Facteur de transmission.
  gamma : Facteur de recuperation.
  ---
  Variables renvoyees : 
  tuple contenant respectivement le vecteur (S,I,R) à l'instant t+dt et t+dt
  """
  if random()<pi(S,I,N,beta,gamma): #Disjonction de cas 
    return((S-1,I+1,N-S-I),t+Delta_T(lambd(S,I,N,beta,gamma)))
  return((S,I-1,N-S-I+1),t+Delta_T(lambd(S,I,N,beta,gamma)))

def maxi_IT(I,T):
    I_max = []
    for i in range(len(I)):
        if (max(I) == I[i]):
            I_max = I[i]
            T_max = T[i]
    return(I_max,T_max)