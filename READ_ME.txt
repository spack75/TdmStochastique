---CONTENU---

Ce dossier contient les fichiers pythons suivants : 

deterministe_case.py : contient les fonctions requises pour la résolution du système d'équations déterministe
etude.py             : contient et met en jeux les fonctions codées dans les différents fichiers python (sauf le main !) pour réaliser les études liées aux différents modèles.
gillespie.py         : contient les fonctions requises pour l'utilisation du modèle de la Chaîne de Markov à temps continue
interpreteur.py      : contient les fonctions requises pour la lecture d'un fichier texte
main.py              : contient les appels pour lancer la simulation
representation.py    : contient les fonctions pour obtenir les tracés
diffusive_case.py    : contient les fonctions requises pour l'étude 


Ce dossier contient le fichier texte suivant (autre que celui-ci) :

settings.txt : contient toutes les données requises pour lancer la simulation


---METHODE D'EMPLOI---

Régler les paramètres du fichier settings.txt en adéquation avec l'étude souhaitée. Pour une utilisation simple, il ne faut ni créer ni supprimer de ligne.

Pour une simple utilisation, et en l'absence d'executable, il n'est pas necessaire de modifier un fichier autre que main.py.
En se rendant sur celui-ci, commenter ou retirer les commentaires d'une ligne pour lancer spécifiquement une simulation. 

Dans chacun des appels, on veillera à ne rien laisser en argument si l'on ne veut pas sauvegarder d'image. Le cas contraire, mettre True comme premier argument et entre guillemets le nom que vous souaiter donner à la figure. 
Pour les fonction etude_GammaBeta_2D, et etude_beta_gamma_diff, puisqu'elles renvoient deux tracés, il faudra mettre True, True, "nom1", "nom2".

Les images s'enregistrent dans le dossier Pictures.
