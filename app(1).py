# on rajoute random
import pyxel, random

# taille de la fenetre 256x256 pixels   
# ne pas modifier
pyxel.init(256, 256, title="Racing cars")

pyxel.load("res.pyxres")

#lecture de la musique 0 en boucle
pyxel.playm(0,loop=True)


# origine des positions de chaque élément

voiture = [100,200]

arbre = [200,120]

arbre2 = [20,80]

arbre3 = [30,140]

grand_arbre = [220,170]

grand_arbre2 = [210,20]

grand_arbre3 = [20,30]

coeur1 = [210,5]

coeur2 = [220,5]

coeur3 = [230,5]

coeur4 = [240,5]

maison = [10,180]

maison2 = [200,50]

cactus = [40,40]

cactus2 = [150,180]

cactus3 = [70,200]

cactusL = [170,150]

cactusL2 = [80,50]

cactusL3 = [185,70]

grand_cactus = [160,20]

grand_cactus2 = [50,220]

# vies, points,tirs et initialisation des menu (=etat)
vies = 4
vies_2 = 1
point = 0
etat = 0

# initialisation des tirs
tirs_liste = []

# initialisation des ennemis
ennemis_liste = []

# initialisation des explosions
explosions_liste = []

# chargement des images
pyxel.load("res.pyxres")

#fonction menu qui permet de changer d'espace de jeu quand le joueur appuie sur une touche spécifique
def menu_etat():
    global etat,vies,vies_2,point
    print(etat)
    if etat == 0 and pyxel.btnr(pyxel.KEY_RETURN):
        etat = 1
    elif etat == 1 and pyxel.btnr(pyxel.KEY_F):
        etat = 2
    elif etat == 1 and pyxel.btnr(pyxel.KEY_D):
        etat = 3
    elif etat == 4 and pyxel.btnr(pyxel.KEY_R):
        etat = 1
        vies=4
        vies_2=1
        point = 0
    elif (vies == 0 or vies_2 == 0) and (etat == 2 or etat ==3) :
        etat = 4
    elif pyxel.btnr(pyxel.KEY_P): 
        etat = 5  
 

    
#fonctions de déplacement, de jeu, de suppression et création
def voiture_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if etat==2:
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 163) :
                x = x+3
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 70) :
                x = x-3
        if pyxel.btn(pyxel.KEY_UP):
           if (y>0):
                y=y-3
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y<240 ):
                y=y+3
    elif etat==3:
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 146) :
                x = x+5
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 94) :
                x = x-5
        if pyxel.btn(pyxel.KEY_UP):
           if (y>0):
                y=y-5
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y<240 ):
                y=y+5
        
    return x, y
    
def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""
    # btnr pour eviter les tirs multiples
    if etat==2:
        if len(tirs_liste)<5:
            if pyxel.btnr(pyxel.KEY_SPACE):
                tirs_liste.append([x+4, y-4])
    if etat==3:
        if len(tirs_liste)<3:
            if pyxel.btnr(pyxel.KEY_SPACE):
                tirs_liste.append([x+4, y-4])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""
    
    for tir in tirs_liste:
        if etat==2:
            tir[1] -= 3
        if etat==3:
            tir[1] -= 5
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""
    ennemi_choix=random.randint(0,2)
    # augmentation du nombre d'ennemi en fonction des points
    if etat==2:
        if point>=200:
            if (pyxel.frame_count % 10 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point>=160:
            if (pyxel.frame_count % 20 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point>=120:
            if (pyxel.frame_count % 30 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point>=80:
            if (pyxel.frame_count % 40 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point>=40:
            if (pyxel.frame_count % 50 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point>=20:
            if (pyxel.frame_count % 60 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
        elif point<20:
            if (pyxel.frame_count % 70 == 0):
                ennemis_liste.append([random.randint(78, 155),0,ennemi_choix])
    if etat==3:
        if (pyxel.frame_count % 15 == 0):
                ennemis_liste.append([random.randint(94, 146),0,ennemi_choix])
    return ennemis_liste
    

def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        if etat==2:
            ennemi[1] += 3
        if etat==3:
            ennemi[1] += 5
        if  ennemi[1]>256:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def voiture_suppression(vies):
    """disparition d'un ennemi si contact et perte d'une vie pour le mode de jeu facile"""
    
    for ennemi in ennemis_liste:
        if etat==2:
            if ennemi[0] <= voiture[0]+8 and ennemi[1] <= voiture[1]+8 and ennemi[0]+8 >= voiture[0] and ennemi[1]+8 >= voiture[1]:
                ennemis_liste.remove(ennemi)
                vies -= 1
            # on ajoute l'explosion
                explosions_creation(voiture[0], voiture[1])
    return vies

def voiture_suppression2(vies_2):
    """2eme fontion voiture_suppression pour le mode de jeu difficile"""

    for ennemi in ennemis_liste:
        if etat==3:
            if ennemi[0] <= voiture[0]+8 and ennemi[1] <= voiture[1]+8 and ennemi[0]+8 >= voiture[0] and ennemi[1]+8 >= voiture[1]:
                ennemis_liste.remove(ennemi)
                vies_2 -= 1
            # on ajoute l'explosion
                explosions_creation(voiture[0], voiture[1])
    return vies_2

                
def ennemis_suppression(point):
    """disparition d'un ennemi et d'un tir si contact plus gain de point"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)
                # on ajoute l'explosion et les points
                explosions_creation(ennemi[0], ennemi[1])
                point +=10
    return point


def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 0])


def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)                
    

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global voiture, tirs_liste, ennemis_liste, vies, explosions_liste, point, tirs, etat, vies_2

    # mise à jour de la position de la voiture
    voiture= voiture_deplacement(voiture[0], voiture[1])

    # creation des tirs en fonction de la position de la voiutre
    tirs_liste = tirs_creation(voiture[0], voiture[1], tirs_liste) 
    
    # mise à jour des menus
    menu_etat()

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_liste = ennemis_deplacement(ennemis_liste)

    # suppression des ennemis et tirs si contact
    point = ennemis_suppression(point)

    # suppression de la voiture et ennemi si contact
    vies = voiture_suppression(vies)
    vies_2 = voiture_suppression2(vies_2)


    # evolution de l'animation des explosions
    explosions_animation()    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global etat 
    
    # menu d'accueil
    if etat == 0:
        pyxel.bltm(0, 0, 2, 512, 256, 256, 256)
    
    
    # quand enter est pressé, on affiche le menu de règles
    elif etat == 1:
        pyxel.bltm(0, 0, 3, 512, 256, 256, 256)
        pyxel.text(105,40, 'regles du jeu', 0)
        pyxel.text(30,80, 'appuyez sur ESPACE pour tirer', 0)
        pyxel.text(30,100, 'vous ne pouvez pas tirer en continu', 0)
        pyxel.text(30,120, 'utilisez les fleches de direction pour vous deplacer', 0)
        pyxel.text(30,140, 'vous perdez une vie quand vous touchez un obstacle', 0)
        pyxel.text(30,160, 'pour jouer au niveau facile, appuyez sur F', 0)
        pyxel.text(30,180, 'pour jouer au niveau difficile, appuyez sur D', 0)
        pyxel.text(30,200, 'appuyez sur P pour arreter le jeu', 0)
    # le jeu commence si F est pressé
    elif etat==2 : 
    
    # vide la fenetre    
        pyxel.cls(0)

        # si le joueur possede des vies le jeu continue
        if vies > 0:
            #affichage du menu de jeu
            pyxel.bltm(0, 0, 0, 512, 256, 256, 256)
        
            # affichage des vies et des points           
            pyxel.text(5,5, 'VIES:'+ str(vies), 7)
            pyxel.text(5,15, 'POINTS:'+ str(point), 7)
        
            # affichage du decors
            pyxel.blt(maison[0], maison[1], 0, 16, 96, 32, 56,0)
            pyxel.blt(maison2[0], maison2[1], 0, 16, 96, 32, 56,0)
            pyxel.blt(coeur4[0], coeur4[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur1[0], coeur1[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur2[0], coeur2[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur3[0], coeur3[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(voiture[0], voiture[1], 0, 48, 16, 16, 16,0)
            pyxel.blt(arbre[0], arbre[1], 0, 48, 0, 16, 16,0)
            pyxel.blt(arbre2[0], arbre2[1], 0, 48, 0, 16, 16,0)
            pyxel.blt(arbre3[0], arbre3[1], 0, 48, 0, 16, 16,0)
            pyxel.blt(grand_arbre[0], grand_arbre[1], 0, 0, 64, 32, 32,0)
            pyxel.blt(grand_arbre2[0], grand_arbre2[1], 0, 0, 64, 32, 32,0)
            pyxel.blt(grand_arbre3[0], grand_arbre3[1], 0, 0, 64, 32, 32,0)
        
            # tirs
            for tir in tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 8, 8, 8,0)
        
            # ennemis
            i=0
            for ennemi in ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0,  ennemi[2]*16, 16, 16, 16,8)
                i+=1
        
            # explosions (cercles de plus en plus grands)
            for explosion in explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3) 
            # un coeur s'enlève quand le joueur perds une vie
            if vies == 3 : 
                pyxel.blt(coeur1[0], coeur1[1], 0, 40, 56, 8, 8,0)
                
            if vies == 2 : 
                pyxel.blt(coeur1[0], coeur1[1], 0, 40, 56, 8, 8,0)
                pyxel.blt(coeur2[0], coeur2[1], 0, 40, 56, 8, 8,0)
                
            if vies == 1 : 
                pyxel.blt(coeur1[0], coeur1[1], 0, 40, 56, 8, 8,0)
                pyxel.blt(coeur2[0], coeur2[1], 0, 40, 56, 8, 8,0)
                pyxel.blt(coeur3[0], coeur3[1], 0, 40, 56, 8, 8,0)
                
    elif etat==3 :
         # vide la fenetre    
        pyxel.cls(0)

        # si le joueur possede des vies le jeu continue
        if vies_2 > 0:
            pyxel.bltm(0, 0, 4, 512, 256, 256, 256)
            # affichage des vies et des points           
            pyxel.text(5,5, 'VIES:'+ str(vies_2), 7)
            pyxel.text(5,15, 'POINTS:'+ str(point), 7)
            #affichage des decors
            pyxel.blt(cactus[0], cactus[1], 0, 48, 48, 16, 16,0)
            pyxel.blt(cactus2[0], cactus2[1], 0, 48, 48, 16, 16,0)
            pyxel.blt(cactus3[0], cactus3[1], 0, 48, 48, 16, 16,0)
            pyxel.blt(cactusL[0], cactusL[1], 0, 0, 48, 16, 16,0)
            pyxel.blt(cactusL2[0], cactusL2[1], 0, 0, 48, 16, 16,0)
            pyxel.blt(cactusL3[0], cactusL3[1], 0, 0, 48, 16, 16,0)
            pyxel.blt(grand_cactus[0], grand_cactus[1], 0, 40, 80, 32, 32,0)
            pyxel.blt(grand_cactus2[0], grand_cactus2[1], 0, 40, 80, 32, 32,0)
            pyxel.blt(coeur4[0], coeur4[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(voiture[0], voiture[1], 0, 48, 16, 16, 16,0)
            for tir in tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 8, 8, 8,0)
            i=0
            for ennemi in ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0,  ennemi[2]*16, 16, 16, 16,8)
                i+=1
            # explosions (cercles de plus en plus grands)
            for explosion in explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)
                
        
            
            
                
    # affichage du menu de fin, game over
    elif etat == 4:
        pyxel.bltm(0, 0, 5, 512, 256, 256, 256)
        pyxel.text(100,70, 'VOTRE SCORE: '+str(point), 0)
        pyxel.text(100,90, 'pour rejouer appuyer sur R', 0)
        pyxel.text(100,120, 'pour arreter le jeu appuyer sur P ', 0)

    elif etat == 5 :
        pyxel.bltm(0, 0, 1, 512, 256, 256, 256)
        pyxel.text(160,90, 'GAME OVER', 0)
        pyxel.stop()

      


pyxel.run(update, draw)