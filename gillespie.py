from interpreteurtxt import Param
import random as rd
import math as m

### Dans ce fichier, on rentrera le code qui sera impliqué pour la question 6

# def lambd(S,I,N = Param["population"],beta = Param["transmission"],gamma = Param["recuperation"]):
#   """
#   fonction calculant lambda
#   """
#   lambd = beta/N*S*I + gamma*I
#   return lambd

# def calcul_dt(lambd):
#   dt = -m.log(rd.random())/lambd
#   return dt

# def choix_infecte_guerit(S,I,R,lambd,N = Param["population"],beta = Param["transmission"]):
#   Pi = beta/N*S*I/lambd
#   u2 = rd.random()
#   if (u2 <= Pi):
#     S.append(S(-1) - 1)
#     I.append(I(-1) + 1)
#   else:
#     I.append(I(-1) - 1)
#     R.append(R(-1) + 1)




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
  Variables d'entrée :
  S     : nombre d'individus sains.
  I     : nombre d'individus infectées.
  N     : population totale.
  beta  : Taux de transmission de la maladie. Fixé par défaut dans le fichier texte.
  gamma : Taux de récupération de la maladie. Fixé par défaut dans le fichier texte.
  ---
  Variables renvoyées : 
  lambda.
  ---
  lambda = beta S I/N + gamma I
  C'est le paramètre définissant la densité de probabilité du pas de temps delta_T
  """
  return beta/N*S*I+gamma*I # calcul de lambda à partir de la formule (8) 

#question b
def Delta_T(lamb):
  """
  Description : Calcule un incrément temporel aléatoirement tiré d'une distribution exponentielle dont la densité de
  probabilité vaut P(t) = lambda exp(-lambda t) que l'on approche par la formule : delta_T = -ln(u1)/lmabda
  où u1 est une variable aléatoire tirée d'une loi uniforme.
  ---
  Variables d'entrée :
  lamb : lambda.

  Variables renvoyées :
  L'incrément de temps.
  """
  return -m.log(rd.random())/lamb #calcul de DT à partir de la note 3 

# partiellement question c 
def pi(S,
       I,
       N     = Param["population"],
       beta  = Param["transmission"],
       gamma = Param["recuperation"]
       ):
  """
  Description : Calcule la probabilité de l'evenement "pendant l'instant Delta t, il y a eu unne infection".
  ---
  Variables d'entrée
  S     : Nombre d'individus sains.
  I     : Nombre d'individus infectés.
  N     : Population totale.
  beta  : Facteur de transmission.
  gamma : Facteur de recuperation.
  ---
  Variables renvoyées
  la probabilité pi.
  """
  return beta*S*I/N/lambd(S,I,N,beta,gamma) # calcul de pi 


#fin de la question c et questions d et e 
def T_plus_Delta_T(t,
                   S,
                   I,
                   N     = Param["population"],
                   beta  = Param["transmission"],
                   gamma = Param["recuperation"]
                   ):
  """
  Description : fait évoluer la situation de l'épidémie à l'instant t à celui t+dt
  ---
  Variables d'entrée :
  t     : instant où la fonction est appelée.
  S     : Nombre d'individus sains.
  I     : Nombre d'individus infectés.
  N     : Population totale.
  beta  : Facteur de transmission.
  gamma : Facteur de recuperation.
  ---
  Variables renvoyées : 
  tuple contenant respectivement le vecteur (S,I,R) à l'instant t+dt et t+dt
  """
  if rd.random() < pi(S,I,N,beta,gamma): #Disjonction de cas 
    return((S-1,I+1,N-S-I),t + Delta_T(lambd(S,I,N,beta,gamma)))
  return((S,I-1,N-S-I+1),t + Delta_T(lambd(S,I,N,beta,gamma)))