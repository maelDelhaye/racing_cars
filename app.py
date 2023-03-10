# on rajoute random
import pyxel, random

# taille de la fenetre 256x256 pixels   
# ne pas modifier
pyxel.init(256, 256, title="Racing cars")

pyxel.load("res.pyxres")
pyxel.playm(0,loop=True)
# position initiale de la voiture
# (origine des positions de chaque élément)

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

# vies, points,tirs et initialisation des menu
vies = 4
vies_2 = 1
point = 0
menu_debut = 0
menu_end = 0
menu_3 = 0
menu_rapide = 0

# initialisation des tirs
tirs_liste = []

# initialisation des ennemis
ennemis_liste = []

# initialisation des explosions
explosions_liste = []

# chargement des images
pyxel.load("res.pyxres")

#création de variables menu pour pouvoir changer d'espace de jeu quand le joueur appuie sur une touche spécifique
def menu_accueil(menu_debut):
    if pyxel.btnr(pyxel.KEY_RETURN):
        menu_debut = 1
    return menu_debut
    
def menu_fin(menu_end):
    if pyxel.btnr(pyxel.KEY_P):
        menu_end = 1
    return menu_end
    
def menu_regles(menu_3):
    if pyxel.btnr(pyxel.KEY_D):
        menu_3 = 1
    return menu_3
    
def menu_vite(menu_rapide):
    if pyxel.btnr(pyxel.KEY_V):
        menu_rapide = 1
    return menu_rapide

#fonctions de déplacement, de jeu, de suppression et création
def voiture_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if menu_3==1:
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
    elif menu_rapide==1:
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 140) :
                x = x+5
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 100) :
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
    if menu_3==1:
        if len(tirs_liste)<5:
            if pyxel.btnr(pyxel.KEY_SPACE):
                tirs_liste.append([x+4, y-4])
    if menu_rapide==1:
        if len(tirs_liste)<3:
            if pyxel.btnr(pyxel.KEY_SPACE):
                tirs_liste.append([x+4, y-4])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""
    
    for tir in tirs_liste:
        if menu_3==1:
            tir[1] -= 3
        if menu_rapide==1:
            tir[1] -= 5
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""
    ennemi_choix=random.randint(0,1)
    # augmentation du nombre d'ennemi en fonction des points
    if menu_3==1:
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
    if menu_rapide==1:
        if (pyxel.frame_count % 20 == 0):
                ennemis_liste.append([random.randint(100, 140),0,ennemi_choix])
    return ennemis_liste
    

def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        if menu_3==1:
            ennemi[1] += 3
        if menu_rapide==1:
            ennemi[1] += 5
        if  ennemi[1]>256:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def voiture_suppression(vies,vies_2):
    """disparition de la voiture et d'un ennemi si contact"""

    for ennemi in ennemis_liste:
        if ennemi[0] <= voiture[0]+8 and ennemi[1] <= voiture[1]+8 and ennemi[0]+8 >= voiture[0] and ennemi[1]+8 >= voiture[1]:
            ennemis_liste.remove(ennemi)
            vies -= 1
            vies_2 -= 1
            # on ajoute l'explosion
            explosions_creation(voiture[0], voiture[1])
    #return vies,vies_2

                
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

    global voiture, tirs_liste, ennemis_liste, vies, explosions_liste, point, tirs, menu_debut,menu_end, menu_3, menu_rapide, vies_2

    # mise à jour de la position de la voiture
    voiture= voiture_deplacement(voiture[0], voiture[1])

    # creation des tirs en fonction de la position de la voiutre
    tirs_liste = tirs_creation(voiture[0], voiture[1], tirs_liste) 
    
    # mise à jour des menus
    menu_debut = menu_accueil(menu_debut)
    menu_end = menu_fin(menu_end)
    menu_3 = menu_regles(menu_3)
    menu_rapide = menu_vite(menu_rapide)

    if menu_3==1 or menu_rapide==1:
        # mise a jour des positions des tirs
        tirs_liste = tirs_deplacement(tirs_liste)

        # creation des ennemis
        ennemis_liste = ennemis_creation(ennemis_liste)

        # mise a jour des positions des ennemis
        ennemis_liste = ennemis_deplacement(ennemis_liste)

        # suppression des ennemis et tirs si contact
        point = ennemis_suppression(point)

        # suppression de la voiture et ennemi si contact
        voiture_suppression(vies,vies_2)
        voiture_suppression(vies,vies_2)


        # evolution de l'animation des explosions
        explosions_animation()    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    pyxel.bltm(0, 0, 2, 512, 256, 256, 256)
    # menu d'accueil
    
    # quand enter est pressé, on affiche le menu de règles
    if menu_debut == 1:
        pyxel.bltm(0, 0, 3, 512, 256, 256, 256)
        pyxel.text(105,70, 'regles du jeu', 0)
        pyxel.text(30,120, 'la difficulte du jeu augmente en fonction des points', 0)
        pyxel.text(30,140, 'appuyer sur P pour arreter le jeu', 0)
        pyxel.text(30,160, 'vous perdez une vie quand vous touchez un obstacle', 0)
        pyxel.text(30,180, 'pour jouer au niveau 1, appuyez sur D', 0)
        pyxel.text(30,200, 'pour jouer au niveau 2, appuyez sur V', 0)
        
    #quand D ou V est pressé, le jeu commence
    if menu_3 == 1: 
    
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
            pyxel.blt(voiture[0], voiture[1], 0, 32, 16, 16, 16,0)
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
                pyxel.blt(ennemi[0], ennemi[1], 0,  ennemi[2]*16, 16, 16, 16,0)
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
                
    if menu_rapide==1:
         # vide la fenetre    
        pyxel.cls(0)

        # si le joueur possede des vies le jeu continue
        if vies_2 > 0:
            pyxel.bltm(0, 0, 4, 512, 256, 256, 256)
            # affichage des vies et des points           
            pyxel.text(5,5, 'VIES:'+ str(vies_2), 7)
            pyxel.text(5,15, 'POINTS:'+ str(point), 7)
            #affichage des decors
            pyxel.blt(coeur1[0], coeur1[1], 0, 40, 48, 8, 8,0)
            pyxel.blt(voiture[0], voiture[1], 0, 32, 16, 16, 16,0)
            for tir in tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 8, 8, 8,0)
            i=0
            for ennemi in ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0,  ennemi[2]*16, 16, 16, 16,0)
                i+=1
            # explosions (cercles de plus en plus grands)
            for explosion in explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)
                
        
            
            
                
        # affichage du menu de fin, game over
        if menu_end == 1 or vies == 0 or vies_2 == 0:
                pyxel.bltm(0, 0, 1, 512, 256, 256, 256)
                pyxel.text(160,90, 'GAME OVER', 0)
                pyxel.text(154,110, 'VOTRE SCORE: '+str(point), 0)
                pyxel.stop()

      


pyxel.run(update, draw)