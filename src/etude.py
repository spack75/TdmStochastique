from interpreteurtxt import Param
from deterministe_case import *
from representation import *
from gillespie import *


N     = Param["population"]      
beta  = Param["transmission"]
gamma = Param["recuperation"]
Tf    = Param["temps de simulation"]
N0    = Param["population saine initiale"]
NP    = Param["nombre d'évaluations"]
Ret   = Param["population rétablie initiale"]


def etude_un_cas(save = True,
                 nom  = "deterministe_basique"
                 ):

    """
    Description : Ensemble d'opérations permettant de résoudre le système d'équations déterministe à partir des fonctions du fichier deterministe.py .
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py représentant les grandeurs
    de personnes saines, infectées et rétablies en fonction du temps.
    """

    (S,I,V,t) = deterministe_case()
    ploteur([t,t,t],[S,I,V],["individus sains","individus infectés","individus rétablis"],["-","-","-"],"temps","population",nom,save)


def etude_R0(save = True,
             nom  = "deterministe_variation_R0"):

    """
    Description : Ensemble d'opérations permettant d'étudier l'issue de l'épidémie par approche déterministe. La méthode 
    utilisée ici est de fixer beta (respectivement gamma) et de faire varier gamme (respectivement beta) pour faire évoluer R0.
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py .
    """
    ## déclaration des variables 
    taux_S_sur_N_gamma_cte = [] # creation de la liste des individus sains à l'issue de la simulation à gamma = cte et beta variable
    taux_S_sur_N_beta_cte  = [] # creation de la liste des individus sains à l'issue de la simulation à beta = cte et gamma variable
    R0 = [i/50 for i in range(1,151)] # creation de l'intervalle du nombre R0 = beta/gamma

    ## opérations 
    for i in R0:
        taux_S_sur_N_beta_cte.append(deterministe_case(beta=i*gamma,Renvoie_liste=False))  # simulation à beta = cte
        taux_S_sur_N_gamma_cte.append(deterministe_case(gamma=beta/i,Renvoie_liste=False)) # simulation à gamma = cte

    ## tracés 
    ploteur([R0,R0],[taux_S_sur_N_beta_cte,taux_S_sur_N_gamma_cte],["à beta constant", "à gamma constant"],["x","."],"R0","Proportion de population",nom,save) #tracé


def etude_GammaBeta_2D(save1 = True,
                       save2 = True,
                       nom1 = "figure",
                       nom2 = "figure"
                       ):

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
    ##déclaration des variables 
    gamma2d = [0.1*i for i in range(1,20)] #création de l'intervalle gamma
    beta2d  = [0.1*i for i in range(1,20)] #création de l'intervalle beta
    X,Y     = np.meshgrid(gamma2d, beta2d) #création du maillage, noms X et Y pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    Z=[] #futur tableau contenant les issues, nom Z pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    RZ=[]#futur tableau contenant les R0, nom RZ pour coincider avec les conventions numpy et matplotlib (RZ=f(X,Y))

    ##opérations 
    for i in beta2d: #parcours sur gamma puis sur beta
        temp=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à Z = f(X,Yi)
        tempR=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à RZ = f(X,Yi)
        for j in gamma2d:
            temp.append(deterministe_case(beta=i,gamma=j,Renvoie_liste=False)) #remplissage de temp
            tempR.append(i/j) #remplissage de tempR
        Z.append(temp) #injection de temp pour completer une ligne de Z à l'issue de la boucle imbriquée 
        RZ.append(tempR) #injection de tempR pour completer une ligne de RZ à l'issue de la boucle imbriquée 

    ##tracés 
    ploteur2d(X,Y,Z,"taux de recuperation","taux de transmission",nom1,save1) #tracé
    ploteur2d(X,Y,RZ,"taux de recuperation","taux de transmission",nom2,save2) #tracé

def maxi_IT(I,T):
    I_max = []
    for i in range(len(I)):
        if (max(I) == I[i]):
            I_max = I[i]
            T_max = T[i]
    return(I_max,T_max)

def etude_Gillespie(save = False, nom = "figure"):

    """
    Description : Ensemble d'opérations permettant d'étudier l'issue de l'épidémie par approche des chaînes de Markov à temps continue.
    ---
    Variables d'entrée : 
    save : Booléen, False par défaut. Détermine si le graphique généré par l'appel sera enregistré (True) ou non (False).
    nom  : texte, "figure" par défaut. Détermine, le cas échéant, le nom du fichier sauvegardé. 
    ---
    Variables renvoyées :
    une image affichée à l'écran ou enregistrée dans le même dossier d'execution de main.py .
    """
    ## déclaration des variables
    T = [0] # liste des temps 
    St = [N0] # liste des populations saines à l'instant t 
    It = [N-N0-Ret] # liste des populations infectées à l'instant t 
    Rt = [Ret] # liste des populations rétablies à l'instant t 

    cpt = 0     # compteur d'itération
    ## opérations 
    while T[-1] < Tf and It[-1] != 0: # cas d'arret = le temps final est dépassé ou bien il n'y a plus d'infecté  
        temp = T_plus_Delta_T(T[-1],St[-1],It[-1]) # si le cas d'arret n'est pas vérifié, on établit la situation à l'instant d'après 
        T.append(temp[1])
        St.append(temp[0][0])
        It.append(temp[0][1])
        Rt.append(temp[0][2])
        cpt = cpt + 1       # incrémentation du compteur
     ## Temps d'arrêt
        if (It[-1] == 0):
            print("\n")
            print("Temps d'arrêt de l'épidémie = ",int(T[-1]*1e5)/1e5,"s\n")
    ## tracés 
    ploteur([T,T,T],[St,It,Rt],["individus sains","individus infectés","individus rétablis"],["-","-","-"],"temps","population",nom,save)

    ## pic d'infecté
    [I_max,T_max] = maxi_IT(It,T)
    print("----------------------------------------")
    print("Nombre d'infecté maximal : I max = ", I_max)
    print("Temps du pic maximal : T max = ", int(T_max*1e5)/1e5)
    print("Temps final : T_end = ", int(T[-1]*1e5)/1e5)
    print("Nombre de pas de temps = ", cpt)
    print("----------------------------------------")
    return(I_max,T_max,T[-1],cpt)