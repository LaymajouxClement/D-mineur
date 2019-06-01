from random import randrange
from coordonnees_clic import coordonnee
from liste_mine import position_mine
import pygame
import sys
from pygame.locals import *


a = coordonnee()        # liste comprenant (x,y) et (x',y')
liste = position_mine()
print(liste) # liste comprenant les mines == 0 et rien == 1
liste_image =[]

coordonnee_x_y = a[0]
coordonnee_x_y_prime = a[1]
pygame.init()

window = pygame.display.set_mode((640,640))

fond = pygame.image.load("map.png").convert()

mine = pygame.image.load(r"image\mine.jpg").convert_alpha()
drapeau = pygame.image.load(r"image\drapeau.jpg").convert_alpha()
vide = pygame.image.load(r"image_nombre\vide.jpg").convert_alpha()
un = pygame.image.load(r"image_nombre\un.jpg").convert_alpha()
deux =pygame.image.load(r"image_nombre\deux.jpg").convert_alpha()
trois =pygame.image.load(r"image_nombre\trois.jpg").convert_alpha()
quatre =pygame.image.load(r"image_nombre\quatre.jpg").convert_alpha()
cinq =pygame.image.load(r"image_nombre\cinq.jpg").convert_alpha()
six =pygame.image.load(r"image_nombre\six.jpg").convert_alpha()
sept =pygame.image.load(r"image_nombre\sept.jpg").convert_alpha()
huit =pygame.image.load(r"image_nombre\huit.jpg").convert_alpha()
perdu = pygame.image.load(r"perdu.png").convert()
noir = pygame.image.load(r'noir.png').convert()
gagné = pygame.image.load(r'gagne.png')

liste_drapeau =[]

for y in range(0,64):
    coordonnee_mine = a[y]
    window.blit(vide,coordonnee_mine)

for z in range (0,64):
    liste_drapeau.append(1)

for x in range (0,64):
    recup = liste[x] # 0 ou 1
    coordonnee_mine = a[x]

    if recup == 0:
        coordonnee_mine = a[x]
        window.blit(mine,coordonnee_mine)
        liste_image.append(mine)
    if recup == 1:
        nombre_mine = 0
        if x%8 == 0:
            if x == 0:

                lire_case1= liste[x+1]
                liste_case2=liste[x+8]
                liste_case3=liste[x+9]
                nombre = lire_case1 +liste_case2 + liste_case3

                if nombre == 0:

                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

                if nombre == 1:

                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

                if nombre == 2:

                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

                if nombre == 3:

                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

            if x == 56 :

                lire_case1 =liste[x+1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-7]
                nombre = lire_case1 +lire_case2 + lire_case3

                if nombre == 0:

                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

                if nombre == 1:

                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

                if nombre == 2:

                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

                if nombre == 3:

                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

            if (x !=0 and x != 56) :

                lire_case1 =liste[x+1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-7]
                lire_case4 =liste[x+9]
                lire_case5 =liste[x+8]
                nombre =lire_case5 +lire_case4+lire_case3+lire_case2+lire_case1

                if nombre == 0:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(cinq,coordonnee_vide)
                        liste_image.append(cinq)

                if nombre == 1:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(quatre,coordonnee_vide)
                        liste_image.append(quatre)

                if nombre == 2:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(trois,coordonnee_vide)
                        liste_image.append(trois)

                if nombre == 3:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(deux,coordonnee_vide)
                        liste_image.append(deux)

                if nombre == 4:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(un,coordonnee_vide)
                        liste_image.append(un)

                if nombre == 5:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(vide,coordonnee_vide)
                        liste_image.append(vide)
        n = x
        if (n+1)%8 == 0:
            if x == 7:

                lire_case1 =liste[x-1]
                lire_case2 =liste[x+8]
                lire_case3 =liste[x+7]
                nombre = lire_case1 +lire_case2 + lire_case3

                if nombre == 0:

                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

                if nombre == 1:

                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

                if nombre == 2:

                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

                if nombre == 3:

                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

            if x == 63:

                lire_case1 =liste[x-1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-9]
                nombre = lire_case1 +lire_case2 + lire_case3

                if nombre == 0:

                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

                if nombre == 1:

                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

                if nombre == 2:

                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

                if nombre == 3:

                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

            if (x!=63 and x!=7):

                lire_case1 =liste[x-1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-9]
                lire_case4 =liste[x+7]
                lire_case5 =liste[x+8]
                nombre =lire_case5 +lire_case4+lire_case3+lire_case2+lire_case1

                if nombre == 0:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(cinq,coordonnee_vide)
                        liste_image.append(cinq)

                if nombre == 1:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(quatre,coordonnee_vide)
                        liste_image.append(quatre)

                if nombre == 2:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(trois,coordonnee_vide)
                        liste_image.append(trois)

                if nombre == 3:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(deux,coordonnee_vide)
                        liste_image.append(deux)

                if nombre == 4:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(un,coordonnee_vide)
                        liste_image.append(un)

                if nombre == 5:
                    if x !=0:
                        coordonnee_vide = a[x]
                        window.blit(vide,coordonnee_vide)
                        liste_image.append(vide)

        if x >= 1 and x <=6:
            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x+9]
            lire_case4 =liste[x+7]
            lire_case5 =liste[x+8]
            nombre =lire_case5 +lire_case4+lire_case3+lire_case2+lire_case1

            if nombre == 0:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(cinq,coordonnee_vide)
                    liste_image.append(cinq)

            if nombre == 1:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(quatre,coordonnee_vide)
                    liste_image.append(quatre)

            if nombre == 2:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

            if nombre == 3:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

            if nombre == 4:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

            if nombre == 5:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

        if x >= 57 and x <=62:
            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x-9]
            lire_case4 =liste[x-7]
            lire_case5 =liste[x-8]
            nombre =lire_case5 +lire_case4+lire_case3+lire_case2+lire_case1

            if nombre == 0:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(cinq,coordonnee_vide)
                    liste_image.append(cinq)

            if nombre == 1:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(quatre,coordonnee_vide)
                    liste_image.append(quatre)

            if nombre == 2:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

            if nombre == 3:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

            if nombre == 4:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

            if nombre == 5:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)

        if( x>8 and x<55 and (x+1)%8 !=0 and x%8 != 0 ):

            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x-9]
            lire_case4 =liste[x-7]
            lire_case5 =liste[x-8]
            lire_case6 =liste[x+9]
            lire_case7 =liste[x+7]
            lire_case8 =liste[x+8]
            nombre =lire_case5 +lire_case4+lire_case3+lire_case2+lire_case1+lire_case6+lire_case7+lire_case8

            if nombre == 0:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(huit,coordonnee_vide)
                    liste_image.append(huit)

            if nombre == 1:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(sept,coordonnee_vide)
                    liste_image.append(sept)

            if nombre == 2:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(six,coordonnee_vide)
                    liste_image.append(six)

            if nombre == 3:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(cinq,coordonnee_vide)
                    liste_image.append(cinq)

            if nombre == 4:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(quatre,coordonnee_vide)
                    liste_image.append(quatre)

            if nombre == 5:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(trois,coordonnee_vide)
                    liste_image.append(trois)

            if nombre == 6:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(deux,coordonnee_vide)
                    liste_image.append(deux)

            if nombre == 7:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(un,coordonnee_vide)
                    liste_image.append(un)

            if nombre == 8:
                if x !=0:
                    coordonnee_vide = a[x]
                    window.blit(vide,coordonnee_vide)
                    liste_image.append(vide)
liste_vide = []
for x in range(0,64):
    recup =liste_image[x]
    if recup == vide:
        liste_vide.append(1)
    else:
        liste_vide.append(0)
print(liste_vide)
def supprimer_case(x):
    print("def supprimer case:",liste_vide[x])
    print(liste_vide)

    if liste_vide[x]==1:
        liste_vide[x]=0

        if x%8 == 0:
            if x == 0:

                lire_case1= liste[x+1]
                window.blit(liste_image[x+1],a[x+1])
                if liste_image[x+1] == vide:


                    supprimer_case(x+1)

                liste_case2=liste[x+8]
                window.blit(liste_image[x+8],a[x+8])
                if liste_image[x+8] == vide:

                    supprimer_case(x+8)

                liste_case3=liste[x+9]
                window.blit(liste_image[x+9],a[x+9])
                if liste_image[x+9] == vide:

                    supprimer_case(x+9)

            if x == 56 :

                lire_case1 =liste[x+1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-7]
                window.blit(liste_image[x+1],a[x+1])
                window.blit(liste_image[x-8],a[x-8])
                window.blit(liste_image[x-7],a[x-7])

                if liste_image[x+1] == vide:

                    supprimer_case(x+1)

                if liste_image[x-7] == vide:

                    supprimer_case(x-7)

                if liste_image[x-8] == vide:

                    supprimer_case(x-8)

            if (x !=0 and x != 56) :

                lire_case1 =liste[x+1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-7]
                lire_case4 =liste[x+9]
                lire_case5 =liste[x+8]
                window.blit(liste_image[x+1],a[x+1])
                window.blit(liste_image[x-8],a[x-8])
                window.blit(liste_image[x-7],a[x-7])
                window.blit(liste_image[x+9],a[x+9])
                window.blit(liste_image[x+8],a[x+8])


                if liste_image[x+1] == vide:

                    supprimer_case(x+1)

                if liste_image[x-7] == vide:

                    supprimer_case(x-7)

                if liste_image[x-8] == vide:

                    supprimer_case(x-8)

                if a[x+9] == vide:

                    supprimer_case(x+9)

                if liste_image[x+8] == vide:

                    supprimer_case(x+8)

        if (x+1)%8 == 0:
            if x == 7:

                lire_case1 =liste[x-1]
                lire_case2 =liste[x+8]
                lire_case3 =liste[x+7]
                window.blit(liste_image[x-1],a[x-1])
                window.blit(liste_image[x+7],a[x+7])
                window.blit(liste_image[x+8],a[x+8])

                if liste_image[x-1] == vide:

                    supprimer_case(x-1)

                if liste_image[x+7] == vide:

                    supprimer_case(x+7)

                if liste_image[x+8] == vide:

                    supprimer_case(x+8)

            if x == 63:

                lire_case1 =liste[x-1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-9]
                window.blit(liste_image[x-1],a[x-1])
                window.blit(liste_image[x-8],a[x-8])
                window.blit(liste_image[x-9],a[x-9])

                if liste_image[x-1] == vide:

                    supprimer_case(x-1)

                if liste_image[x-9] == vide:

                    supprimer_case(x-9)

                if liste_image[x-8] == vide:

                    supprimer_case(x-8)

            if (x!=63 and x!=7):

                lire_case1 =liste[x-1]
                lire_case2 =liste[x-8]
                lire_case3 =liste[x-9]
                lire_case4 =liste[x+7]
                lire_case5 =liste[x+8]
                window.blit(liste_image[x-1],a[x-1])
                window.blit(liste_image[x-8],a[x-8])
                window.blit(liste_image[x+7],a[x+7])
                window.blit(liste_image[x-9],a[x-9])
                window.blit(liste_image[x+8],a[x+8])

                if liste_image[x-1] == vide:

                    supprimer_case(x-1)

                if liste_image[x-9] == vide:

                    supprimer_case(x-9)

                if liste_image[x-8] == vide:

                    supprimer_case(x-8)

                if liste_image[x+8] == vide:

                    supprimer_case(x+8)

                if liste_image[x+7] == vide:

                    supprimer_case(x+7)

        if x >= 1 and x <=6:
            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x+9]
            lire_case4 =liste[x+7]
            lire_case5 =liste[x+8]

            if liste_image[x-1] == vide:

                    supprimer_case(x-1)

            if liste_image[x+1] == vide:

                supprimer_case(x+1)

            if liste_image[x+8] == vide:

                supprimer_case(x+8)

            if liste_image[x+7] == vide:

                supprimer_case(x+7)

            if liste_image[x+9] == vide:

                supprimer_case(x+9)

        if x >= 57 and x <=62:
            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x-9]
            lire_case4 =liste[x-7]
            lire_case5 =liste[x-8]
            window.blit(liste_image[x-1],a[x-1])
            window.blit(liste_image[x-8],a[x-8])
            window.blit(liste_image[x-7],a[x-7])
            window.blit(liste_image[x-9],a[x-9])
            window.blit(liste_image[x+1],a[x+1])

            if liste_image[x-1] == vide:

                    supprimer_case(x-1)

            if liste_image[x+1] == vide:

                supprimer_case(x+1)

            if liste_image[x-8] == vide:

                supprimer_case(x-8)

            if liste_image[x-7] == vide:

                supprimer_case(x-7)

            if liste_image[x-9] == vide:

                supprimer_case(x-9)

        if( x>8 and x<55 and (x+1)%8 !=0 and x%8 != 0 ):

            lire_case1 =liste[x-1]
            lire_case2 =liste[x+1]
            lire_case3 =liste[x-9]
            lire_case4 =liste[x-7]
            lire_case5 =liste[x-8]
            lire_case6 =liste[x+9]
            lire_case7 =liste[x+7]
            lire_case8 =liste[x+8]
            window.blit(liste_image[x+1],a[x+1])
            window.blit(liste_image[x-1],a[x-1])
            window.blit(liste_image[x-7],a[x-7])
            window.blit(liste_image[x-9],a[x-9])
            window.blit(liste_image[x-8],a[x-8])
            window.blit(liste_image[x+7],a[x+7])
            window.blit(liste_image[x+8],a[x+8])
            window.blit(liste_image[x+9],a[x+9])


            if liste_image[x-1] == vide:

                    supprimer_case(x-1)

            if liste_image[x+1] == vide:

                supprimer_case(x+1)

            if liste_image[x+8] == vide:

                supprimer_case(x+8)

            if liste_image[x+7] == vide:
                liste_vide[x+7]=0
                supprimer_case(x+7)

            if liste_image[x+9] == vide:

                supprimer_case(x+9)

            if liste_image[x-8] == vide:

                supprimer_case(x-8)

            if liste_image[x-7] == vide:

                supprimer_case(x-7)

            if liste_image[x-9] == vide:

                supprimer_case(x-9)



    if liste_vide[x]==0:
        return(x)



case1  = liste_image[0]
case2  = liste_image[1]
case3  = liste_image[2]
case4  = liste_image[3]
case5  = liste_image[4]
case6  = liste_image[5]
case7  = liste_image[6]
case8  = liste_image[7]
case9  = liste_image[8]
case10 = liste_image[9]
case11 = liste_image[10]
case12 = liste_image[11]
case13 = liste_image[12]
case14 = liste_image[13]
case15 = liste_image[14]
case16 = liste_image[15]
case17 = liste_image[16]
case18 = liste_image[17]
case19 = liste_image[18]
case20 = liste_image[19]
case21 = liste_image[20]
case22 = liste_image[21]
case23 = liste_image[22]
case24 = liste_image[23]
case25 = liste_image[24]
case26 = liste_image[25]
case27 = liste_image[26]
case28 = liste_image[27]
case29 = liste_image[28]
case30 = liste_image[29]
case31 = liste_image[30]
case32 = liste_image[31]
case33 = liste_image[32]
case34 = liste_image[33]
case35 = liste_image[34]
case36 = liste_image[35]
case37 = liste_image[36]
case38 = liste_image[37]
case39 = liste_image[38]
case40 = liste_image[39]
case41 = liste_image[40]
case42 = liste_image[41]
case43 = liste_image[42]
case44 = liste_image[43]
case45 = liste_image[44]
case46 = liste_image[45]
case47 = liste_image[46]
case48 = liste_image[47]
case49 = liste_image[48]
case50 = liste_image[49]
case51 = liste_image[50]
case52 = liste_image[51]
case53 = liste_image[52]
case54 = liste_image[53]
case55 = liste_image[54]
case56 = liste_image[55]
case57 = liste_image[56]
case58 = liste_image[57]
case59 = liste_image[58]
case60 = liste_image[59]
case61 = liste_image[60]
case62 = liste_image[61]
case63 = liste_image[62]
case64 = liste_image[63]

window.blit(fond,(0,0))
pygame.display.flip()

print(len(liste_image))
continu = True
'''try:'''
gagner = False
while continu == True:

    for event in pygame.event.get():

        if event.type == KEYDOWN :

            if event.type == QUIT or event.key == K_ESCAPE:

                continu = False
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 3:

                mouse_x_y = pygame.mouse.get_pos()
                liste_x_y =[]
                position_x = int((mouse_x_y[0])/80)
                position_y = int((mouse_x_y[1])/80)
                liste_x_y.append([(position_x*80)+2,(position_y*80)+2])
                liste_x_y_mouse =liste_x_y[0]
                liste_x =liste_x_y_mouse[0]
                liste_y = liste_x_y_mouse[1]
                liste_regroup =(liste_x,liste_y)
                print(liste_x_y_mouse,liste_regroup)

                for x in range (0,64):
                    if liste_regroup == a[x]:
                        if liste_drapeau[x]==1:
                            liste_drapeau[x]=0
                            window.blit(drapeau,a[x])
                        else:
                            liste_drapeau[x]=1
                            window.blit(noir,a[x])

                if liste_drapeau.count(0)==10:

                    for x in range (0,64):
                        print(liste_drapeau[x],liste[x])
                        if liste_drapeau[x] != liste[x]:
                            window.blit(perdu,(0,0))
                            gagner = False
                    if liste_drapeau == liste:
                        gagner = True

                    if gagner == True:
                        window.blit(gagné,(0,0))



            elif event.button == 1:

                mouse_x_y = pygame.mouse.get_pos()

                liste_x_y =[]
                position_x = int((mouse_x_y[0])/80)
                position_y = int((mouse_x_y[1])/80)
                liste_x_y.append([(position_x*80)+2,(position_y*80)+2])
                liste_x_y_mouse =liste_x_y[0]
                liste_x =liste_x_y_mouse[0]
                liste_y = liste_x_y_mouse[1]
                liste_regroup =(liste_x,liste_y)
                print(liste_x_y_mouse)


                for x in range(0,64):
                    if liste_regroup == a[x]:

                        if liste_image[x]==vide and liste_vide[x]==1:

                            window.blit(liste_image[x],a[x])
                            supprimer_case(x)

                        else :
                            window.blit(liste_image[x],a[x])
                            if liste_image[x]==mine:
                                window.blit(perdu,(0,0))
                                continu = False

    pygame.display.flip()

pygame.quit()
exit()
'''except:
    traceback.print_exc()
finally:
    pygame.quit()
    exit()'''
