from random import randint


def creer_paquet():
    cartes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    return cartes


def tirer_carte(cartes):
    indice = randint(0, len(cartes) - 1)
    carte = cartes[indice]
    cartes.remove(carte)

    return carte


def distribuer_cartes(cartes):
    joueur = []
    banque = []

    joueur.append(tirer_carte(cartes))
    joueur.append(tirer_carte(cartes))

    banque.append(tirer_carte(cartes))
    banque.append(tirer_carte(cartes))

    return joueur, banque

def calculer_score(main):
    total = 0
    nombre_as = 0

    for carte in main:
        total = total + carte

        if carte == 11:
            nombre_as = nombre_as + 1

    while total > 21 and nombre_as > 0:
        total = total - 10
        nombre_as = nombre_as - 1

    return total


def jouer_joueur(cartes, joueur):
    choix = "oui"

    while choix == "oui":
        print("Vos cartes :", joueur)
        print("Votre score :", calculer_score(joueur))

        if calculer_score(joueur) > 21:
            print("Vous avez dépassé 21. Vous avez perdu")
            break

        choix = input("Voulez-vous tirer une carte ? (oui/non) : ")

        if choix == "oui":
            joueur.append(tirer_carte(cartes))

    return joueur

def jouer_banque(cartes, banque):
    total = calculer_score(banque)

    while total <= 16:
        banque.append(tirer_carte(cartes))
        total = calculer_score(banque)

    return banque


def est_blackjack(main):
    if len(main) == 2 and calculer_score(main) == 21:
        return True
    else:
        return False

    
def determiner_resultat(joueur, banque):
    score_joueur = calculer_score(joueur)
    score_banque = calculer_score(banque)

    blackjack_joueur = est_blackjack(joueur)
    blackjack_banque = est_blackjack(banque)

    if blackjack_joueur:
        print("Blackjack ! Vous avez gagné")
        return "Gain"

    elif blackjack_banque:
        print("La banque a un Blackjack. Vous avez perdu")
        return "Perte"

    elif score_joueur > 21:
        print("Vous avez dépassé 21. Vous avez perdu")
        return "Perte"

    elif score_banque > 21:
        print("La banque a dépassé 21. Vous avez gagné")
        return "Gain"

    elif score_joueur > score_banque:
        print("Vous avez gagné")
        return "Gain"

    elif score_joueur == score_banque:
        print("Égalité")
        return "Égalité"

    else:
        print("Vous avez perdu")
        return "Perte"


def modifier_argent(argent, resultat, mise):
    if resultat == "Gain":
        argent = argent + mise

    elif resultat == "Perte":
        argent = argent - mise

    return argent

def choisir_mise(argent):
    mise = int(input("Combien voulez-vous miser ? "))

    while mise <= 0 or mise > argent:
        print("Mise incorrecte.")
        mise = int(input("Combien voulez-vous miser ? "))

    return mise

argent = 100

print("Vous avez", argent, "€.")

mise = choisir_mise(argent)

print("Mise :", mise)

cartes = creer_paquet()

joueur, banque = distribuer_cartes(cartes)

print("Vos cartes :", joueur)
print("Carte visible de la banque :", banque[0])

joueur = jouer_joueur(cartes, joueur)

if calculer_score(joueur) <= 21:
    banque = jouer_banque(cartes, banque)

resultat = determiner_resultat(joueur, banque)

argent = modifier_argent(argent, resultat, mise)

print("Votre argent :", argent, "€")

