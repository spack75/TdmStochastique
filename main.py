import etude as e


e.etude_Gillespie(True,"toto")#cet appel tracera les resultats d'une etude epidemiologique par la methode de la chaîne de Markov à temps continue.
e.etude_un_cas()#cet appel tracera les resultats d'une etude epidemiologique par la resolution du modèle deterministe.
e.etude_R0()#cet appel tracera l'issue d'une epidemie (pourcentage de rescapes à l'instant t final) en fonction du nombre de reproduction R0 .
e.etude_GammaBeta_2D()#cet appel tracera deux contours : les contours 2D de l'issue d'une epidemie avec le taux de recuperation comme abscisse et le taux de transmission comme ordonnee; et le contours de R0 pour les mêmes coordonnees.
