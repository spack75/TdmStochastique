from etude import *


#etude_un_cas(False)#cet appel tracera les résultats d'une étude épidémiologique par la résolution du modèle déterministe.
#etude_R0(False)#cet appel tracera l'issue d'une épidémie (pourcentage de rescapés à l'instant t final) en fonction du nombre de reproduction R0 .
#etude_GammaBeta_2D(False,False)#cet appel tracera deux contours : les contours 2D de l'issue d'une épidémie avec le taux de récupération comme abscisse et le taux de transmission comme ordonnée; et le contours de R0 pour les mêmes coordonnées.
#etude_Gillespie(False)#cet appel tracera les resultats d'une étude épidémiologique par la méthode de la chaîne de Markov à temps continue.


## campagne de simulation de la chaîne de Markov
N = 100     # nombre de simulation que l'on souhaite réaliser
I_max_list = []
T_max_list = []
T_end_list = []
cpt_list = []
for i in range(N):
    [I_max,T_max,T_end,cpt] = etude_Gillespie(True)
    I_max_list.append(I_max)
    T_max_list.append(T_max)
    T_end_list.append(T_end)
    cpt_list.append(cpt)

# écriture dans des fichiers
f = open("data/T_max","w")
for i in range(N):
    f.write(str(int(T_max_list[i]*1e5)/1e5)+ "\n")
f.close

f = open("data/I_max","w")
for i in range(N):
    f.write(str(int(I_max_list[i]*1e5)/1e5)+ "\n")
f.close

f = open("data/T_end","w")
for i in range(N):
    f.write(str(int(T_end_list[i]*1e5)/1e5)+ "\n")
f.close

f = open("data/compteur","w")
for i in range(N):
    f.write(str(cpt_list[i])+ "\n")
f.close