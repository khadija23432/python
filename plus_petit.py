from random import randint
point=10
nb_secret= randint(1, 1000)
while point>0 :
    x=int(input("saisi un nb : "))
    if x>nb_secret :
        print("plus grand")
        point=point-1
    elif x<nb_secret :
        print("plus petit")
        point=point-1
    else :
        print("bravo")

    print("point :", point)