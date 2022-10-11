from doctest import UnexpectedException
from msilib.schema import Error
from urllib.request import UnknownHandler

#Puisque c'est un programme simple et linéaire, je n'ai pas vu l'utilité d'encapsuler le code dans des fonctions.

#Je n'était pas certain que nous avions vu les exceptions, mais j'ai senti le besoin d'en mettre sinon j'avais des sueurs froides...

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\n")
print("Bienvenue à la station d'essence IFT-1003!")
print("\n")

print("Configuration de l a pompe à essence . . .")
prixOrdinaire = float((input("Prix de l’essence ordinaire ($/L) : "))) # En $
prixDiesel = float((input("Prix de l'essence diesel ($/L) : "))) # En $
prixSupreme = 1.1 * prixOrdinaire 
codeSecret = input("Le code secret du jour est : ") #Chaine de caracteres arbitraire.
print(10*"*")


#2 Arrivée d'une automobile.
print("Une automobile arrive.")
tankCapacity = float(input("Le nombre de litres total de son réservoir est : ")) # En litre
tankStatus = float(input("et il en contient actuellement : ")) # En litre
print("\n")


#3 Demander le type d'essence.
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("- - -   Affichage sur la pompe                                                                - - -")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
prixPompe = 0.0 #Prix au compteur apres le choix d'essence du client.
print("Veuillez sélectionner le type d'essence parmi :")
print("- [O] rdinaire : {:.2f}$ / litre".format(prixOrdinaire))
print("- [S] uper : {:.2f}$ / litre".format(prixSupreme))
print("- [D] iesel : {:.2f}$ / litre".format(prixDiesel))
choixEssence = input("Votre choix (O, S ou D) : ").lower() # Choix du client.
if choixEssence == "o":
    prixPompe = prixOrdinaire
elif choixEssence == "s":
    prixPompe = prixSupreme
elif choixEssence == "d":
    prixPompe = prixDiesel
else:
    raise UnknownHandler



#4 Demander le plein ou un montant fixe.

choixFill = input("Souhaitez-vous faire le plein (P) ou choisir un montant fixe (M) ? ").lower()
gazQuantity = 0.0 # Quantité (En litre) maximale d'essence pouvant entrer dans la voiture selon le choix.
gazMoney = 0.0 # Aloocation d'une variable pour que l'usager puisse entrer le montant (en dollar) à convertir.

#Calcul de gazQuantity en fonction du choix de l'usager. Je veux seulement des litres, pas des dollars.
if choixFill == "p":  
    gazQuantity = tankCapacity - tankStatus
elif choixFill == "m":
    gazMoney = float(input("Veuillez inscrire le montant souhaité : "))
    gazQuantity = gazMoney / prixPompe
else:
    raise UnknownHandler


    

#5 Remplissage litre par litre.

print("Remplissage!")
gazBought = 0.0
cost = 0.0
print("État du réservoir d'essence : {:.2f}L sur {:.2f}L".format(tankStatus, tankCapacity))
print("Coût (jusqu'à maintenant) : {:.2f}$".format(cost))
stop = input("Appuyez sur entrée pour ajouter un litre (A pour arrêter) : " ).lower()

while stop != "a" and gazQuantity != 0.0 and tankStatus != tankCapacity: # Tant que les conditions necessitant l'arret ne sont pas rencontree.
    if gazQuantity > 1 and tankStatus + 1 < tankCapacity: #Reste-t-il au moins 1 litre à mettre et reste-t-il au moins un litre d'espace dans la tank. 
        gazBought += 1
        tankStatus += 1
        gazQuantity -= 1
    else:
        if gazQuantity < tankCapacity - tankStatus: #Il reste moins d'un litre à mettre et la tank à encore suffisament de place.
            gazBought += gazQuantity
            tankStatus += gazQuantity
            gazQuantity = 0.0
        else: #La tank est presque pleine
            gazBought += tankCapacity - tankStatus # On ajoute juste la bonne quantité d'essence.
            tankStatus = tankCapacity # La tank est pleine
    
    cost = gazBought * prixPompe
    print("État du réservoir d'essence : {:.2f}L sur {:.2f}L".format(tankStatus, tankCapacity))
    print("Coût (jusqu'à maintenant) : {:.2f}$".format(cost))
    if gazQuantity != 0 and tankStatus != tankCapacity:    
        stop = input("Appuyez sur entrée pour ajouter un litre (A pour arrêter) : " ).lower()

# C'est plus stylish si on connait la raison de l'arret
if stop == "a":                                   
    print("Remplissage manuellement arrêté par l'utilisateur...")
if tankCapacity == tankStatus:
    print("Votre réservoir est plein!")
if choixFill == "m" and gazQuantity == 0:
    print("Montant atteint!")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #Verification du code secret
print("Coût (jusqu'à maintenant) : {:.2f}$".format(cost))
codeEntre = input("Si vous connaissez le code promotionnel RABAIS+, entrez-le maintenant pour obtenir le 30% de rabais: ")
if codeEntre == codeSecret:
    print("Code valide")
    print("Vous avez économisé {:.2f}$".format(cost * 0.3))
    cost = cost*0.70
else:
    print("Code non valide")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #Affichage final
print("\n")
print("Le montant final est : {:.2f}$".format(cost))
print("\n")
print("Merci d'avoir fait affaire avec IFT-1003!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")