import matplotlib.pyplot as plt

def ploteur2d(X,Y,Z,titreX = "titreX",titreY = "titreY",nom = "figure",save=False):
    """
    Description : Réalise un tracé contour à partir des listes fournies.
    ---
    variables d'entrée : 
    X      : tableau contenant les positions x du domaine à représenter.
    Y      : tableau contenant les positions y du domaine à représenter.
    Z      : tableau contenant les valeurs z du domaine à représenter.
    titreX : titre de l'axe x. "titreX" par défaut.
    titreY : titre de l'axe y. "titreY" par défaut.
    nom    : non de l'image sous laquelle elle sera enregistrée. "figure" par défaut.
    save   : booléen. False par défaut.
    ---
    variables de sortie :
    Si save est False, affiche une figure .
    Si save est True, enregistre l'image au nom de la variable nom.
    """
    plt.figure()
    plt.contourf(X,Y,Z,200)
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    cbar=plt.colorbar()
    cbar.set_label("proportion d'individus sains")
    if not save:
        plt.show()
    else :
        plt.savefig("Pictures/"+nom)


def ploteur(X,Y,labels,format,titreX="titreX",titreY="titreY",nom="figure",save=False):
    """
    Description : Réalise un tracé à partir des listes fournies.
    ---
    variables d'entrée : 
    X      : tableau contenant les positions x du domaine à représenter. Chaque ligne correspond à un jeu de données.
    Y      : tableau contenant les positions y du domaine à représenter. Chaque ligne correspond à un jeu de données.
    titreX : titre de l'axe x. "titreX" par défaut.
    titreY : titre de l'axe y. "titreY" par défaut.
    nom    : non de l'image sous laquelle elle sera enregistrée. "figure" par défaut.
    save   : booléen. False par défaut.
    ---
    variables renvoyées :
    Si save est False, affiche une figure.
    Si save est True, enregistre l'image au nom de la variable nom.
    """
    n=len(X)
    plt.figure()
    for i in range(n):
        plt.plot(X[i],Y[i],format[i],label=labels[i])
    plt.grid()
    plt.legend()
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    if not save:
        plt.show()
    else :
        plt.savefig("Pictures/"+nom)

def histogramme(X,N,Xlabel,nom):
    """
    Description : Fonction dessinant l'histogramme d'une liste X pour N intervalles
    ---
    variables d'entrée : 
    X    : Liste contenant les valeurs à afficher dans l'histogramme
    N    : Entier contenant le nombre d'intervalle de l'histogramme
    nom  : Nom de la figure dans les dossier
    ---
    variables renvoyées :
    L'image de l'histogramme est stockée sous format .png dans le dossier 'data'.

    """
    plt.figure()
    plt.hist(X, range = (min(X),max(X)) , bins = (N))
    plt.xlabel(Xlabel)
    plt.ylabel("Nombre de simulations")
    plt.savefig("Pictures/"+ nom)

