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