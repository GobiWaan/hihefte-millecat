from random import shuffle, sample
from devine_qui import possede, types_caracteristiques_ordre_aleatoire, valeurs_ordre_aleatoire, score_dichotomie

from personnages import CARACTERISTIQUES, lire_entree, charger_personnages

# CARACTERISTIQUES = {
#     "genre": ["homme", "femme"],
#     "cheveux": ["noirs", "bruns", "blonds", "blancs", "roux"],
#     "yeux": ["bruns", "bleus"],
#     "nez": ["petit", "gros"],
#     "accessoires": ["chapeau", "bijoux", "lunettes"],
#     "pilosite": ["barbe", "moustache", "calvitie"]

# 2/6 TESTED AND FONCTIONNAL

personnages = charger_personnages()

def selectionner_caracteristique(personnages_restants):
    """
    Parmi tous les couples type/valeur de caractéristiques, retourne
    celui qui présente le meilleur score de dichotomie. Les types et valeurs doivent être
    itérées en ordre aléatoire (utilisez les fonctions à cet effet déclarées précédemment)

    Note: cette fonction devrait appeler les fonctions
        types_caracteristiques_ordre_aleatoire, valeurs_ordre_aleatoire et score_dichotomie.

    Args:
        personnages_restants (dict): Les personnages à considérer pour les scores.

    Returns:
        (string, string): Le type et la valeur ayant le meilleur score dichotomique
    """
    dicCompteur = {}

    for t in types_caracteristiques_ordre_aleatoire():
        for v in valeurs_ordre_aleatoire(t):
            dicCompteur[(t, v)] = score_dichotomie(personnages, t, v)
    highScore = max(dicCompteur, key=lambda key: dicCompteur[key])

    return highScore


print(selectionner_caracteristique(personnages))