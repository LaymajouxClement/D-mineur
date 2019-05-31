def retirer_case():
    if x%8 == 0:
        if x == 0:
            window.blit(liste_image[x+1],a[x+1])
            window.blit(liste_image[x+8],a[x+8])
            window.blit(liste_image[x+9],a[x+9])

        if x == 56 :
            window.blit(liste_image[x+1],a[x+1])
            window.blit(liste_image[x-8],a[x-8])
            window.blit(liste_image[x-7],a[x-7])
    n = x
    if (n+1)%8 == 0:
        if x == 7:
            window.blit(liste_image[x-1],a[x-1])
            window.blit(liste_image[x+7],a[x+7])
            window.blit(liste_image[x+8],a[x+8])

        if x == 63:
            window.blit(liste_image[x-1],a[x-1])
            window.blit(liste_image[x-8],a[x-8])
            window.blit(liste_image[x-9],a[x-9])

        if (x!=63 and x!=7):
            window.blit(liste_image[x-1],a[x-1])
            window.blit(liste_image[x-9],a[x-9])
            window.blit(liste_image[x-8],a[x-8])
            window.blit(liste_image[x+7],a[x+7])
            window.blit(liste_image[x+8],a[x+8])

    if x >= 1 and x <=6:
        window.blit(liste_image[x+1],a[x+1])
        window.blit(liste_image[x-1],a[x-1])
        window.blit(liste_image[x+7],a[x+7])
        window.blit(liste_image[x+8],a[x+8])
        window.blit(liste_image[x+9],a[x+9])

    if x >= 57 and x <=62:
        window.blit(liste_image[x+1],a[x+1])
        window.blit(liste_image[x-1],a[x-1])
        window.blit(liste_image[x-7],a[x-7])
        window.blit(liste_image[x-8],a[x-8])
        window.blit(liste_image[x-9],a[x-9])

    if( x>8 and x<55 and (x+1)%8 !=0 and x%8 != 0 ):
        window.blit(liste_image[x+1],a[x+1])
        window.blit(liste_image[x-1],a[x-1])
        window.blit(liste_image[x-7],a[x-7])
        window.blit(liste_image[x-8],a[x-8])
        window.blit(liste_image[x-9],a[x-9])
        window.blit(liste_image[x+7],a[x+7])
        window.blit(liste_image[x+8],a[x+8])
        window.blit(liste_image[x+9],a[x+9])