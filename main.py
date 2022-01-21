from Interpreteurtxt import Param
from deterministe import *
from representation import *



N     = Param["population"]      
beta  = Param["transmission"]
gamma = Param["recuperation"]
Tf    = Param["temps de simulation"]
N0    = Param["population saine initiale"]
NP    = Param["nombre d'évaluations"]
Ret   = Param["population rétablie initiale"]

def etude_un_cas(save=False,nom="figure"):
    """
    Description : Ensemble d'opérations permettant de résoudre le système d'équations déterministe à partir des fonctions du fichier deterministe.py .
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py.
    """
    (S,I,V,t) = deterministe_case()
    ploteur([t,t,t],[S,I,V],["individus sains","individus infectés","individus rétablis"],[".",".","."],save=save,nom=nom)

def etude_R0(save=False,nom="figure"):
    """
    Description : Ensemble d'opérations permettant d'étudier l'issue de l'épidémie par approche déterministe. La méthode utilisée ici est de fixer beta (respectivement gamma) et de faire varier gamme (respectivement beta) pour faire évoluer R0.
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py .
    """
    taux_S_sur_N_gamma_cte = [] #creation de la liste des individus sains à l'issue de la simulation à gamma = cte et beta variable
    taux_S_sur_N_beta_cte  = [] #creation de la liste des individus sains à l'issue de la simulation à beta = cte et gamma variable

    R0=[i/50 for i in range(1,151)] #creation de l'intervalle du nombre R0

    for i in R0:
        taux_S_sur_N_beta_cte.append(deterministe_case(beta=i*gamma,Renvoie_liste=False))  #simulation à beta = cte
        taux_S_sur_N_gamma_cte.append(deterministe_case(gamma=beta/i,Renvoie_liste=False)) #simulation à gamma = cte
    ploteur([R0,R0],[taux_S_sur_N_beta_cte,taux_S_sur_N_gamma_cte],["à beta constant", "à gamma constant"],["x","."],save=save,nom=nom) #tracé

def etude_GammaBeta_2D():
    """
    Description : Ensemble d'opérations permettant d'étudier l'issue de l'épidémie par approche déterministe. La méthode utilisée ici est de faire varier beta ET gamma dans le but de tracer S(t=tfinal) = f(beta,gamma).
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py .
    """

    gamma2d = [0.1*i for i in range(1,20)] #création de l'intervalle gamma
    beta2d  = [0.1*i for i in range(1,20)] #création de l'intervalle beta
    X,Y     = np.meshgrid(gamma2d, beta2d) #création du maillage, noms X et Y pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    Z=[] #futur tableau contenant les issues, nom Z pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    RZ=[]
    for i in gamma2d: #parcours sur gamma puis sur beta
        temp=[] #tableau qui à l'issue de l'a boucle contiendra une ligne correspondant à Z = f(X,Yi)
        tempR=[]
        for j in beta2d:
            temp.append(deterministe_case(beta=j,gamma=i,Renvoie_liste=False)) #remplissage de temp
            tempR.append(i/j)
        Z.append(temp)
        RZ.append(tempR)
    ploteur2d(X,Y,Z,titreX="beta",titreY="gamma") #tracé
    ploteur2d(X,Y,RZ,titreX="beta",titreY="gamma") #tracé

etude_un_cas()
etude_R0()
etude_GammaBeta_2D()
