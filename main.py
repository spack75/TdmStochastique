from etude import *


#etude_un_cas(False)#cet appel tracera les résultats d'une étude épidémiologique par la résolution du modèle déterministe.
#etude_R0(False)#cet appel tracera l'issue d'une épidémie (pourcentage de rescapés à l'instant t final) en fonction du nombre de reproduction R0 .
#etude_GammaBeta_2D(False,False)#cet appel tracera deux contours : les contours 2D de l'issue d'une épidémie avec le taux de récupération comme abscisse et le taux de transmission comme ordonnée; et le contours de R0 pour les mêmes coordonnées.
#etude_Gillespie(False)#cet appel tracera les resultats d'une étude épidémiologique par la méthode de la chaîne de Markov à temps continue.


## campagne de simulation de la chaîne de Markov
N = 100     # nombre de simulation que l'on souhaite réaliser
I_max_list = []
T_max_list = []
#for i in range(N - 1):
    # [I_max,T_max] = etude_Gillespie(False)
    # I_max_list.append(I_max)
    # T_max_list.append(T_max)

etude_Gillespie(False)[1]