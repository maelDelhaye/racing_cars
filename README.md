# racing_cars

*Lisa Pacca, Ansel Gabillot, Maxen Kaiser, Mael Delhaye*

idée de jeu:
  un peu du genre subway surfer, le joueur deplace une voiture et doit eviter des obstacles sur la route. 
  plusieurs course differentes, avec des obstacles et des themes differents.
  on essaiera de faire des niveux differents avec des difficultés differentes. 
  
nom du jeu: Racing Cars 

**cahiers des charges:**

  -exemples: Subway Surfer (principe du jeu)  https://www.youtube.com/watch?v=dvjy6V4vLlI
  
  -nombres de joueurs: 1
  
  -graphisme: 2D vue du haut
  
  -niveaux: le jeu continue jusqu'a ce que le joueur perde. la difficulté augmente a chaque palier de x min
  
  -systeme de vie: a chque obstacle touché le joueur perd une vie. 3 vies en tout. 
  
  -pas de PNJ
  
  -pas de projectile 
  
  -musique:
   
   - acceuil --> https://www.youtube.com/watch?v=s5VCm-YxrK
   
   - course --> a trouver
  
  -menu d'acceuil
  
  -obstacles: caisse en bois, voitures renversées, travaux, police, trous, arbres
  
  -mouvements: la voiture ne se déplace que latéralement.(fleches droite/gauche)
  
  -fond:  la route ne bouge pas, c'est les obstacles qui se décalent de haut en bas de l'ecran. 
  
  -possible choix du theme (nuit/jour - desert/ville...)
  
  -images:
  
   - fond  https://www.freepik.com/premium-vector/top-view-road_32826224.htm
   
   - route/circuit
   
   - voiture
   
   - obstacles
   
  -controles avec les fleches du clavier

**planning**


1ere semaine (2/12/22) : decision du type de jeu

2e semaine (9/12/22) : on a fait le cahier des charges en définissant des modalités plus précises

3e semaine (16/12/22) : faire le planning sur 15 semaines 

4e semaine (6/01/23) : mettre le fond (image d'un circuit vide) qui ne bouge pas 
--> *tous ensemble*

5e semaine (13/01/23) : rajouter la voiture qui sera statique et rajouter les obstacles qui défileront à une vitesse donnée (objet comme des voiture renversées, des travaux, des arbres) 
--> *un qui s'occupe de la voiture, les 3 autres s'occupent d'obstacles différents*

6e semaine (20/01/23) : rajouter les controles de la voiture avec les fleches du clavier latérales et rajouter le système de vie (3 vies) 
--> *2 qui s'occupent de déplacer la voiture, 2 qui s'accupent d'afficher les 3 vies sur le jeu*

7e semaine (27/01/23) : faire en sorte que quand le joueur touche un obstacle il perde une vie et faire en sorte que quand le joueur n'a plus de vie, le jeu s'arrête et affiche un message de fin 
--> *1 qui s'occupe de l'impact voiture/obstacle, 1 qui s'occupent d'enlever une des 3 vies quand il y impact, 1 qui s'occupent d'arreter le jeu quand le joueur n'a plus de vie, 1 qui s'occupe d'afficher le message "game over"*

8e semaine (3/02/23) : établir le système de niveau, quand le joueur joue plus de 30s, on passe au niveau supérieur et la rapidité du jeu augmente (les obstacles défilent plus vite) 
--> *2 qui s'occupe de lancer un compteur de temps et d'intégrer les variables de 30s, (donc les pallier : niveau 1, niveau 2...), 2 qui s'occupent de changer la rapidité des obstacles*

9e semaine (10/02/23) : faire afficher le temps de partie à la fin du jeu et le niveau atteint, pour que le joueur puisse battre son record 
--> *2 qui s'occupent de faire affcher le temps, 2 qui s'occupent d'afficher le niveau atteint*

10e semaine (17/02/23) : commencer le menu d'accueil (trouver le fond, ecrire les titres, ajouter la touche "start"
--> *tous ensemble*

11e semaine (24/02/23) : rajouter les musiques (une pour l'accueil, une pour le jeu)
--> *2 pour l'accueil, 2 pour le jeu*

12e semaine (3/03/23) :  vérification du jeu, suppression des bugs 
--> *tous ensemble*

13e semaine (10/03/23) : si tout est fait dans les temps de ce planning, rajouter différentes voitures que le joueur peut choisir dans le menu d'accuei
--> *tous ensemble*

14e semaine (17/03/23) : finalisation du projet, et/ou rattraper le retard si le planning n'est pas respecté
--> *tous ensemble*

15e semaine (24/03/23) : préparation de l'oral
--> *tous ensemble*


pyxel : https://www.pyxelstudio.net/studio/aptn5z6q 

code avec limite de tirs : https://www.pyxelstudio.net/studio/aptn5z6q
code avec musique : https://www.pyxelstudio.net/studio/aptn5z6q

# on rajoute random
import pyxel, random

# taille de la fenetre 128x128 pixels   
# ne pas modifier
pyxel.init(256, 256, title="Racing cars")

pyxel.load("res.pyxres")
pyxel.playm(0,loop=True)
# position initiale de la voiture
# (origine des positions de chaque élément)
voiture_x = 100
voiture_y = 200

arbre_x = 200
arbre_y = 120

arbre2_x = 20
arbre2_y = 80

arbre3_x = 30
arbre3_y = 140

grand_arbre_x = 220
grand_arbre_y = 170

grand_arbre2_x = 210
grand_arbre2_y = 20

grand_arbre3_x = 20
grand_arbre3_y = 30

coeur1_x = 210
coeur1_y = 5

coeur2_x = 220
coeur2_y = 5

coeur3_x = 230
coeur3_y = 5

coeur4_x = 240
coeur4_y = 5

maison_x = 10
maison_y = 180

maison2_x = 200
maison2_y = 50

# vies, points et tirs
vies = 4
point = 0
tirs = 70
menu_debut = 0
menu_end = 0

# initialisation des tirs
tirs_liste = []

# initialisation des ennemis
ennemis_liste = []

# initialisation des explosions
explosions_liste = []

# chargement des images
pyxel.load("res.pyxres")

def menu_accueil(menu_debut):
    if pyxel.btnr(pyxel.KEY_RETURN):
        menu_debut = 1
    return menu_debut
    
def menu_fin(menu_end):
    if pyxel.btnr(pyxel.KEY_ESCAPE):
        menu_end = 1
    return menu_end

def voiture_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 163) :
            x = x+3
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 69) :
            x = x-2
    return x, y
    
def tirs_limite(tirs):
    """limite de tir"""
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs = tirs - 1
    if tirs<=0:
        tirs=0
    return tirs

def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""
    # btnr pour eviter les tirs multiples
    if tirs > 0:
        if pyxel.btnr(pyxel.KEY_SPACE):
            tirs_liste.append([x+4, y-4])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 3
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # augmentation du nombre d'ennemi en fonction des points
    
    if point>=200:
        if (pyxel.frame_count % 10 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point>=160:
        if (pyxel.frame_count % 20 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point>=120:
        if (pyxel.frame_count % 30 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point>=80:
        if (pyxel.frame_count % 40 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point>=40:
        if (pyxel.frame_count % 50 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point>=20:
        if (pyxel.frame_count % 60 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    elif point<20:
        if (pyxel.frame_count % 70 == 0):
            ennemis_liste.append([random.randint(78, 155), 0])
    return ennemis_liste


def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        ennemi[1] += 3
        if  ennemi[1]>256:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def voiture_suppression(vies):
    """disparition de la voiture et d'un ennemi si contact"""

    for ennemi in ennemis_liste:
        if ennemi[0] <= voiture_x+8 and ennemi[1] <= voiture_y+8 and ennemi[0]+8 >= voiture_x and ennemi[1]+8 >= voiture_y:
            ennemis_liste.remove(ennemi)
            vies -= 1
            # on ajoute l'explosion
            explosions_creation(voiture_x, voiture_y)
    return vies

                
def ennemis_suppression(point):
    """disparition d'un ennemi et d'un tir si contact"""

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

    global voiture_x, voiture_y, tirs_liste, ennemis_liste, vies, explosions_liste, point, tirs, menu_debut,menu_end 

    # mise à jour de la position du vaisseau
    voiture_x, voiture_y = voiture_deplacement(voiture_x, voiture_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(voiture_x, voiture_y, tirs_liste)
    
    tirs = tirs_limite(tirs)

    menu_debut = menu_accueil(menu_debut)
    menu_end = menu_fin(menu_end)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_liste = ennemis_deplacement(ennemis_liste)

    # suppression des ennemis et tirs si contact
    point = ennemis_suppression(point)

    # suppression du vaisseau et ennemi si contact
    vies = voiture_suppression(vies)


    # evolution de l'animation des explosions
    explosions_animation()    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    pyxel.bltm(0, 0, 2, 512, 256, 256, 256)
    pyxel.text(100,200, 'APPUYEZ SUR ENTRER POUR JOUER', 0)
    
    if menu_debut == 1:
    # vide la fenetre
        
        pyxel.cls(0)

        # si le vaisseau possede des vies le jeu continue
        if vies > 0:
        
            pyxel.bltm(0, 0, 0, 512, 256, 256, 256)
        
            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(vies), 7)
            pyxel.text(5,15, 'POINTS:'+ str(point), 7)
            pyxel.text(5,25, 'TIRS:'+ str(tirs), 7)
        
            # vaisseau (carre 8x8)
            pyxel.blt(maison_x, maison_y, 0, 16, 96, 32, 56,0)
            pyxel.blt(maison2_x, maison2_y, 0, 16, 96, 32, 56,0)
            pyxel.blt(coeur4_x, coeur4_y, 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur1_x, coeur1_y, 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur2_x, coeur2_y, 0, 40, 48, 8, 8,0)
            pyxel.blt(coeur3_x, coeur3_y, 0, 40, 48, 8, 8,0)
            pyxel.blt(voiture_x, voiture_y, 0, 32, 16, 16, 16,0)
            pyxel.blt(arbre_x, arbre_y, 0, 48, 0, 16, 16,0)
            pyxel.blt(arbre2_x, arbre2_y, 0, 48, 0, 16, 16,0)
            pyxel.blt(arbre3_x, arbre3_y, 0, 48, 0, 16, 16,0)
            pyxel.blt(grand_arbre_x, grand_arbre_y, 0, 0, 64, 32, 32,0)
            pyxel.blt(grand_arbre2_x, grand_arbre2_y, 0, 0, 64, 32, 32,0)
            pyxel.blt(grand_arbre3_x, grand_arbre3_y, 0, 0, 64, 32, 32,0)
        
            # tirs
            for tir in tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 8, 8, 8,0)
        
            # ennemis
            i=0
            for ennemi in ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0, (i%2)*16, 16, 16, 16,0)
                i+=1
        
            # explosions (cercles de plus en plus grands)
            for explosion in explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)   
                
        
        if vies == 0:
                pyxel.bltm(0, 0, 1, 512, 256, 256, 256)
                pyxel.text(160,90, 'GAME OVER', 0)
                pyxel.text(154,110, 'VOTRE SCORE: '+str(point), 0)
        
        if menu_end == 1:
            pyxel.quit()

pyxel.run(update, draw)
       
