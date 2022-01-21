from Interpreteurtxt import Param

### Dans ce fichier, on rentrera le code qui sera impliqué pour la question 6



def lambd(S,
          I,
          N = Param["population"],        
          beta = Param["transmission"],
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
  """
  return beta/N*S*I+gamma*I