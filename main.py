from deterministe import *

N = Param["population"]      
beta = Param["transmission"]
gamma = Param["recuperation"]
Tf = Param["temps de simulation"]
N0 = Param["population saine initiale"]
NP = Param["nombre d'évaluations"]
Ret = Param["population rétablie initiale"]

def etude_un_cas(save=False,nom="figure"):
    (S,I,V,t) = deterministe_case()
    ploteur([t,t,t],[S,I,V],["individus sains","individus infectés","individus rétablis"],[".",".","."],save=save,nom=nom)

def etude_R0(save=False,nom="figure"):
    taux_S_sur_N_gamma_cte=[] 
    taux_S_sur_N_beta_cte=[] 
    R0=[i/50 for i in range(1,151)]
    for i in R0:
        taux_S_sur_N_beta_cte.append(deterministe_case(beta=i*gamma,Renvoie_liste=False))
        taux_S_sur_N_gamma_cte.append(deterministe_case(gamma=beta/i,Renvoie_liste=False))
    ploteur([R0,R0],[taux_S_sur_N_beta_cte,taux_S_sur_N_gamma_cte],["à beta constant", "à gamma constant"],["x","."],save=save,nom=nom)

etude_un_cas()
etude_R0()
