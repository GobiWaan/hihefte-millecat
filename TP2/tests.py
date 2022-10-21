from random import shuffle, sample
from devine_qui import types_caracteristiques_ordre_aleatoire, valeurs_ordre_aleatoire

from personnages import CARACTERISTIQUES, lire_entree, charger_personnages

# CARACTERISTIQUES = {
#     "genre": ["homme", "femme"],
#     "cheveux": ["noirs", "bruns", "blonds", "blancs", "roux"],
#     "yeux": ["bruns", "bleus"],
#     "nez": ["petit", "gros"],
#     "accessoires": ["chapeau", "bijoux", "lunettes"],
#     "pilosite": ["barbe", "moustache", "calvitie"]

# 2/6 TESTED AND FONCTIONNAL


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
    

personnages = {'Bernard': {'genre': 'homme', 'accessoires': 'chapeau'},
                   'Claire': {'genre': 'femme', 'accessoires': 'chapeau'},
                   'Eric': {'genre': 'homme', 'accessoires': 'chapeau'},
                   'George': {'genre': 'homme', 'accessoires': 'lunette'},
                   'Maria': {'genre': 'femme', 'accessoires': 'chapeau'}}




def score_dichotomie(personnages_restants, type_caracteristique, valeur_caracteristique): #TESTED AND FONCTIONNAL
    """
    Retourne un score en fonction du nombre de personnages restants ayant ou n'ayant pas la
    caractéristique en paramètres. Ce score est élevé pour les caractéristiques divisant les personnages
    en deux parties le plus égales possibles, et est faible pour les caractéristiques divisant les
    personnages en parties inégales.

    Le score est calculé selon la formule suivante:
    nombre de personnages total - maximum(nombre de personnages ayant la caractéristique,
                                          nombre de personnages n'ayant pas la caractéristique)

    Exemple:
    En début de partie, il y 5 femmes sur 24 personnages. Le score de la caractéristique ayant le type genre
    et la valeur femme est donc 24 - maximum(5, 19), c'est-à-dire 5.
    En revanche, ce score peut changer en cours de partie. Par exemple supposons qu'il ne reste que
    les personnages ayant des chapeaux. Il y a alors 2 femmes sur 5 personnages. Le score
    de la caractéristique femme est donc 5 - maximum(2, 3), donc 2. Le score de la caractéristique
    lunettes serait quant à lui 5 - maximum(1, 4), c'est-à-dire 1. Cela indique que, parmi les personnages
    ayant des chapeaux, la caractéristique femme divise mieux l'ensemble que la caractéristique lunettes.

    Note: cette fonction devrait appeler la fonction possede.

    Args:
        personnages_restants (dict): L'ensemble des personnages n'ayant pas été éliminés encore.
        type_caracteristique (string): Le type de la caractéristique dont on veut connaître le score
        valeur_caracteristique (string): La valeur de la caractéristique dont on veut connaître le score

    Returns:
        int: Le score
    """
    nombrePersonnagesTotal = len(personnages_restants)
    avecCaracteristique = 0
    sansCaracteristique = 0

    for personne in personnages_restants.values():
        if personne[type_caracteristique] == valeur_caracteristique:
            avecCaracteristique += 1
        else:
            sansCaracteristique += 1
    
    score = nombrePersonnagesTotal - max(avecCaracteristique, sansCaracteristique)

    return score

print(score_dichotomie(personnages, 'genre', 'homme'))  # = 5 - max(3, 2))
print(score_dichotomie(personnages, 'accessoires', 'chapeau'))
print(score_dichotomie(personnages, 'accessoires', 'lunettes'))



    
