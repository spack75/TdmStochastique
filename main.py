import etude as e


#e.etude_Gillespie(save = False, nom = "Gillespie")#cet appel tracera les resultats d'une etude epidemiologique par la methode de la chaîne de Markov à temps continue.
#e.etude_un_cas(save = False, nom = "Deterministe")#cet appel tracera les resultats d'une etude epidemiologique par la resolution du modèle deterministe.
#e.etude_R0(save = False, nom = "R0")#cet appel tracera l'issue d'une epidemie (pourcentage de rescapes à l'instant t final) en fonction du nombre de reproduction R0 .
#e.etude_GammaBeta_2D(save1 = False,save2 = False,nom1 = "issue_epidemie",nom2 = "R0_2D")#cet appel tracera deux contours : les contours 2D de l'issue d'une epidemie avec le taux de recuperation comme abscisse et le taux de transmission comme ordonnee; et le contours de R0 pour les mêmes coordonnees.
#e.etude_Diffusion(save = False, nom = "diffus")#cet appel tracera pour n simulations S en fonction de t. Il donnera aussi la moyenne et la variance du temps de fin de l'epidemie 
#e.etude_beta_gamma_diff(save1 = False, save2 = False, nom1 = "moy", nom2 = "var")#cet appel tracera le contour du temps moyen d'extinctions de l'epidemie pour alpha et beta variables 
#e.etude_gillesplie_statistique()#cet appel realisera l'etude statistique du schema de gillespie, il creera trois histogrammes dans le dossier Pictures 
