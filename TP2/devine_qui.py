from random import shuffle, sample

from personnages import CARACTERISTIQUES


def types_caracteristiques_ordre_aleatoire(): #TESTED AND FONCTIONNAL
    """
    Donne les types de caractéristiques dans un ordre aléatoire.

    Indices:
    - Vous pouvez obtenir le dictionnaire de caractéristiques en important CARACTERISTIQUES
        du module personnages.
    - Vous pouvez obtenir la liste des clés d'un dictionnaire avec list(dictionnaire.keys())
    - Utilisez la fonction shuffle importée pour mélanger l'ordre de la liste (Attention:
        shuffle ne retourne rien, mais modifie directement la liste en argument)

    Returns:
        list: La liste des types de caractéristiques
    """
    listeShuffelledTypes = list(CARACTERISTIQUES.keys())
    shuffle(listeShuffelledTypes)
    
    return listeShuffelledTypes


def valeurs_ordre_aleatoire(type_caracteristique): #TESTED AND FONCTIONNAL
    """
    Donne les valeurs de caractéristiques dans un ordre aléatoire,
    pour un type de caractéristique donné.

    Attention!! Si vous utilisez shuffle directement sur la liste de valeurs,
    celles-ci sera modifiée pour la suite du programme (il ne faut pas).
    Faites-en d'abord une copie avec liste.copy()

    Args:
        type_caracteristique (string): Le type de caractéristique

    Returns:
        list: La liste des valeurs possibles pour ce type de caractéristique
    """
    listeShuffelledValues = CARACTERISTIQUES[type_caracteristique]
    return sample(listeShuffelledValues, len(listeShuffelledValues))


def possede(donnees_personnage, type_caracteristique, valeur_caracteristique): #TTESTED AND FONCTIONNAL
    """
    Indique si la valeur de caractéristique fait partie des données du personnage.

    Attention! Si le type de caractéristique est accessoires ou pilosite, il faut vérifier
    que la valeur cherchée EST DANS les données du personnage pour ce type, tandis que
    si le type est autre chose, il faut vérifier que la valeur cherchée EST la donnée du personnage
    pour ce type.

    Args:
        donnees_personnage (dict): Les données (sous forme type:valeur) pour un personnage
        type_caracteristique: Le type de caractéristique analysé
        valeur_caracteristique: La valeur de la caractéristique recherchée

    Returns:
        bool: True si le personnage possède la caractéristique, False sinon.
    """
    return (donnees_personnage[type_caracteristique] == valeur_caracteristique)


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
    # CODE HERE


def mettre_a_jour_hypotheses(personnages_restants, type_caracteristique, valeur_caracteristique, reponse):
    """
    Retourne un dictionnaire basé sur le dictionnaire de personnages restants en paramètre, dans
    lequel on enlève les personnages qui possèdent ou ne possèdent pas la caractéristique en paramètres.

    Args:
        personnages_restants (dict): Les personnages préalablement restants
        type_caracteristique (string): Le type de la caractéristique dont on
                                       veut conserver/enlever ceux qui l'ont
        valeur_caracteristique (string): La valeur de la caractéristique dont
                                   on veut conserver/enlever ceux qui l'ont
        reponse (bool): True si on doit conserver les personnages qui possèdent la caractéristique,
                        False si on doit conserver ceux qui ne la possèdent pas.

    Note: cette fonction devrait appeler la fonction possede.

    Returns:
        dict: Le dictionnaire de personnages restants mis à jour.
    """
    # VOTRE CODE ICI


if __name__ == '__main__':
    print("Tests unitaires...")

    # Test de la fonction types_caracteristiques_ordre_aleatoire
    assert len(types_caracteristiques_ordre_aleatoire()) == len(CARACTERISTIQUES)

    # Test de la fonction valeurs_ordre_aleatoire
    assert len(valeurs_ordre_aleatoire("cheveux")) == len(CARACTERISTIQUES["cheveux"])

    # Tests de la fonction possede
    donnees = {"cheveux": "bruns", "accessoires": ["chapeau"]}
    assert possede(donnees, "cheveux", "bruns")
    assert not possede(donnees, "accessoires", "bijoux")

    # Tests de la fonction score_dichotomie
    personnages = {'Bernard': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Claire': {'genre': 'femme', 'accessoires': ['chapeau']},
                   'Eric': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'George': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Maria': {'genre': 'femme', 'accessoires': ['chapeau']}}
    assert score_dichotomie(personnages, 'genre', 'homme') == 2  # = 5 - max(3, 2)
    assert score_dichotomie(personnages, 'accessoires', 'chapeau') == 0  # = 5 - max(5, 0)

    # Aucun test n'est fourni pour selectionner_caracteristiques

    # Tests de la fonction mettre_a_jour_hypotheses
    # assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
    # assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2

    print("Tests réussis!")
