import matplotlib.pyplot as plt

def ploteur2d(X,Y,Z,titreX="titreX",titreY="titreY",colorbar_nom="colorbar",nom="figure",save=False):
    """
    Description : Realise un trace contour à partir des listes fournies.
    ---
    variables d'entree : 
    X      : tableau contenant les positions x du domaine à representer.
    Y      : tableau contenant les positions y du domaine à representer.
    Z      : tableau contenant les valeurs z du domaine à representer.
    titreX : titre de l'axe x. "titreX" par defaut.
    titreY : titre de l'axe y. "titreY" par defaut.
    nom    : non de l'image sous laquelle elle sera enregistree. "figure" par defaut.
    save   : booleen. False par defaut.
    ---
    variables de sortie :
    Si save est False, affiche une figure .
    Si save est True, enregistre l'image au nom de la variable nom.
    """
    plt.figure()
    plt.contourf(X,Y,Z,1000)
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    cbar=plt.colorbar()
    cbar.set_label(colorbar_nom)
    if not save:
        plt.show()
    else :
        plt.savefig("Pictures/"+nom)


def ploteur(X,Y,labels,format,titreX="titreX",titreY="titreY",nom="figure",save=False,legend=True):
    """
    Description : Realise un trace à partir des listes fournies.
    ---
    variables d'entree : 
    X      : tableau contenant les positions x du domaine à representer. Chaque ligne correspond à un jeu de donnees.
    Y      : tableau contenant les positions y du domaine à representer. Chaque ligne correspond à un jeu de donnees.
    titreX : titre de l'axe x. "titreX" par defaut.
    titreY : titre de l'axe y. "titreY" par defaut.
    nom    : non de l'image sous laquelle elle sera enregistree. "figure" par defaut.
    save   : booleen. False par defaut.
    ---
    variables renvoyees :
    Si save est False, affiche une figure.
    Si save est True, enregistre l'image au nom de la variable nom.
    """
    n=len(X)
    plt.figure()
    for i in range(n):
        plt.plot(X[i],Y[i],format[i],label=labels[i])
    plt.grid()
    if legend:
        plt.legend()
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    if not save:
        plt.show()
    else :
        plt.savefig("Pictures/"+nom)