def coordonnee():

    liste_clic = []


    for y in range(2,640,80):
        for x in range (2,640,80):

            liste_clic.append((x,y))

    print(liste_clic)
    return(liste_clic)

