from random import randint
valeurs=["2","3","4","5","6","7","8","9","10","10","10","10","11"]
couleurs=["coeur","carreau","pique","trèfle"]
if joueur>21:
    print("perte")
elif joueur =="blackjack" :
    print ("gain de 3 pour 2")
elif 17<=joueur<=21 :
    print ("gain de 1 pour 1")
if banque>21:
    print("gain 1 pour 1")
elif joueur> banque :
    print ("gain de 1 pour 1")
elif 17<=banque<=21 :
    print ("gain de 1 pour 1")
elif banque==joueur :
    print ("égalité")


def creer_paquet() :
cartes=["2","3","4","5","6","7","8","9","10","10","10","10","11"]*4


return cartes

def tirer_carte(cartes):
    indice = randint(0, len(cartes) - 1) #py choisit entre 0 et 51 
    carte = cartes[indice] # on récupère la carte qui se trouve à cette position
    cartes.remove(carte) 


    return carte    #La fonction nous donne la carte tirée

