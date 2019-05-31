def position_mine():
    import random

    liste_mine = []

    for x in range (0,10):
        liste_mine.append(0)

    for x in range (0,54):
        liste_mine.append(1)

    random.shuffle(liste_mine)

    return(liste_mine)

