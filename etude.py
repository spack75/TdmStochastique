from interpreteurtxt import Param
from deterministe_case import deterministe_case
from numpy import meshgrid
from representation import ploteur2d, ploteur
from gillespie import T_plus_Delta_T
from diffusive_case import Diffusive_case,variance_temps,temps_moyen


N     = Param["population"]      
beta  = Param["transmission"]
gamma = Param["recuperation"]
Tf    = Param["temps de simulation"]
N0    = Param["population saine initiale"]
NP    = Param["nombre d'evaluations"]
Ret   = Param["population retablie initiale"]


def etude_un_cas(save = False,
                 nom  = "Deterministe"
                 ):

    """
    Description : Ensemble d'operations permettant de resoudre le système d'equations deterministe à partir des fonctions du fichier deterministe.py .
    ---
    Variables d'entree : 
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le dossier "Pictures".
    """

    (S,I,V,t) = deterministe_case()
    ploteur([t,t,t],[S,I,V],["individus sains","individus infectes","individus retablis"],["-","-","-"],"temps","population",nom,save)


def etude_R0(save = False,
             nom  = "R0"):

    """
    Description : Ensemble d'operations permettant d'etudier l'issue de l'epidemie par approche deterministe. La methode utilisee ici est de fixer beta (respectivement gamma) et de faire varier gamme (respectivement beta) pour faire evoluer R0.
    ---
    Variables d'entree : 
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le même dossier d'execution de main.py .
    """
    ##declaration des variables 
    taux_S_sur_N_gamma_cte = [] #creation de la liste des individus sains à l'issue de la simulation à gamma = cte et beta variable
    taux_S_sur_N_beta_cte  = [] #creation de la liste des individus sains à l'issue de la simulation à beta = cte et gamma variable
    R0=[i/50 for i in range(1,151)] #creation de l'intervalle du nombre R0

    ##operations 
    for i in R0:
        taux_S_sur_N_beta_cte.append(deterministe_case(beta=i*gamma,Renvoie_liste=False))  #simulation à beta = cte
        taux_S_sur_N_gamma_cte.append(deterministe_case(gamma=beta/i,Renvoie_liste=False)) #simulation à gamma = cte

    ##traces 
    ploteur([R0,R0],[taux_S_sur_N_beta_cte,taux_S_sur_N_gamma_cte],["à beta constant", "à gamma constant"],["x","."],"R0","Proportion de population",nom,save) #trace


def etude_GammaBeta_2D(save1 = False,
                       save2 = False,
                       nom1 = "issue_epidemie",
                       nom2 = "R0_2D"
                       ):

    """
    Description : Ensemble d'operations permettant d'etudier l'issue de l'epidemie par approche deterministe. La methode utilisee ici est de faire varier beta ET gamma dans le but de tracer S(t=tfinal) = f(beta,gamma).
    ---
    Variables d'entree : 
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le même dossier d'execution de main.py .
    """
    ##declaration des variables 
    gamma2d = [0.1*i for i in range(1,20)] #creation de l'intervalle gamma
    beta2d  = [0.1*i for i in range(1,20)] #creation de l'intervalle beta
    X,Y     = meshgrid(gamma2d, beta2d) #creation du maillage, noms X et Y pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    Z=[] #futur tableau contenant les issues, nom Z pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    RZ=[]#futur tableau contenant les R0, nom RZ pour coincider avec les conventions numpy et matplotlib (RZ=f(X,Y))

    ##operations 
    for i in beta2d: #parcours sur gamma puis sur beta
        temp=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à Z = f(X,Yi)
        tempR=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à RZ = f(X,Yi)
        for j in gamma2d:
            temp.append(deterministe_case(beta=i,gamma=j,Renvoie_liste=False)) #remplissage de temp
            tempR.append(i/j) #remplissage de tempR
        Z.append(temp) #injection de temp pour completer une ligne de Z à l'issue de la boucle imbriquee 
        RZ.append(tempR) #injection de tempR pour completer une ligne de RZ à l'issue de la boucle imbriquee 

    ##traces 
    ploteur2d(X,Y,Z,"taux de recuperation","taux de transmission",nom1,save1) #trace
    ploteur2d(X,Y,RZ,"taux de recuperation","taux de transmission",nom2,save2) #trace


def etude_Gillespie(save = False, nom = "Gillespie"):

    """
    Description : Ensemble d'operations permettant d'etudier l'issue de l'epidemie par approche des chaînes de Markov à temps continue.
    ---
    Variables d'entree : 
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le dossier "Pictures" .
    """
    ##declaration des variables
    T = [0] #liste des temps 
    St = [N0] #liste des populations saines à l'instant t 
    It = [N-N0-Ret] #liste des populations infectees à l'instant t 
    Rt = [Ret] #liste des populations retablies à l'instant t 

    ##operations 
    while T[-1]<Tf and It[-1]!=0: #cas d'arret = le temps final est depasse ou bien il n'y a plus d'infecte  
        temp = T_plus_Delta_T(T[-1],St[-1],It[-1]) #si le cas d'arret n'est pas verifie, on etablit la situation à l'instant d'après 
        T.append(temp[1])
        St.append(temp[0][0])
        It.append(temp[0][1])
        Rt.append(temp[0][2])

    ##traces 
    ploteur([T,T,T],[St,It,Rt],["individus sains","individus infectes","individus retablis"],["-","-","-"],"temps","population",nom,save)

def etude_Diffusion(save=False,nom="diffus"):
    """
    Description : Ensemble d'operations permettant d'etudier l'issue de l'epidemie par approche du systeme d'equations stochastiques.
    ---
    Variables d'entree : 
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le dans le dossier "Pictures".
    """
    ##declaration des variables
    [Sdif,Idif,T] = Diffusive_case() #obtention des vecteurs solutions
    
    ##traces
    if len(Sdif)==1: #si on a une seule courbe, on fait le trace de l'epidemie complete car la lisibilite le permet
        Rdif=[[N-Sdif[0][i]-Idif[0][i]for i in range(len(Sdif[0]))]]
        Y=Sdif+Idif+Rdif
        print(Y[2])
        ploteur(3*T,Y,["individus sains","individus infectes","individus retables"],["-","-","-"],"temps","population",nom,save,False)
    else: #sinon on ne superpose que les courbes du meme type
        Ftot=["-" for i in range(Param["nombre de simulations"])] 
        ploteur(T,Idif,Ftot,Ftot,"temps","population",nom,save,False)
        ploteur(T,Sdif,Ftot,Ftot,"temps","population",nom,save,False)
    

    


def etude_beta_gamma_diff(precision = 0.5,
                       nb_calculs = 400,
                       save1 = False,
                       save2 = False,
                       nom1 = "moy",
                       nom2 = "var"
                       ):
    """
    Description : Ensemble d'operations permettant d'etudier les grandeurs statistiques standardes de l'epidemie (moyenne et variance du temps final).
    ---
    Variables d'entree : 
    precision : Reel determinant la precision du trace contour.
    nb_calculs : Entier determinant le nombre de calcul fait pour chaque x et chaque y du contour, il y aura donc nb_calculs*nb_calculs calculs en tout.
    save : Booleen, False par defaut. Determine si le graphique genere par l'appel sera enregistre (True) ou non (False).
    nom  : texte, "figure" par defaut. Determine, le cas echeant, le nom du fichier sauvegarde. 
    ---
    Variables renvoyees :
    une image affichee à l'ecran ou enregistree dans le dossier "Pictures" .
    """                   
    gamma2d = [precision*i for i in range(1,nb_calculs)] #creation de l'intervalle gamma !!! bien faire varier precision et nb_calculs pour choisir l'intervalle (borne sup = nb_calculs*precision-1)
    beta2d  = [precision*i for i in range(1,nb_calculs)] #creation de l'intervalle beta
    X,Y     = meshgrid(gamma2d, beta2d) #creation du maillage, noms X et Y pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    Z=[] #futur tableau contenant les issues, nom Z pour coincider avec les conventions numpy et matplotlib (Z=f(X,Y))
    VZ=[] 

    for i in beta2d: #parcours sur gamma puis sur beta
        print(i)
        tempm=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à Z = f(X,Yi)
        tempv=[] #tableau qui à l'issue de la boucle contiendra une ligne correspondant à RZ = f(X,Yi)
        for j in gamma2d:
          #  if j>i:
          #      tempm.append(0)  #remplissage de tempm
          #      tempv.append(0) #remplissage de tempv     
          #  else:          
                [Sdif,Idif,T] = Diffusive_case(beta=i,gamma=j)
                tempm.append(temps_moyen(Sdif,T))  #remplissage de tempm
                tempv.append(variance_temps(Sdif,T)) #remplissage de tempv

        Z.append(tempm) #injection de temp pour completer une ligne de Z à l'issue de la boucle imbriquee 
        VZ.append(tempv) #injection de temp pour completer une ligne de Z à l'issue de la boucle imbriquee 

    ploteur2d(X,Y,Z,"taux de recuperation","taux de transmission","moyenne (en s)",nom1,save1) #trace
    ploteur2d(X,Y,VZ,"taux de recuperation","taux de transmission","variance (en s^2)",nom2,save2) #trace
