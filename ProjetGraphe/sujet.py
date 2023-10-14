#en utilisant tkinter, affiche l'image plan_piste.png dans un canvas de 500x500

import tkinter
from PIL import ImageTk, Image

#on importe le graphe des pistes
from build_graphe import build_graphe

#on definit les variables globales comme la taille de la fenetre et l'erreur de click de souris
TAILLE = (1300, 1000)
ERREUR = (TAILLE[0]//100, TAILLE[1]//100)

#poids des remontees mecaniques
TELEPHERIQUE = 5
TELECABINE = 6
TELESIEGE = 7
TELESKI = 8

#dictionnaire de tout les sommets lie au coordonnees des lieux sur l'image
LISTE_LIEU = {
    "haut_roc_merlet": (138, 195),
    "haut_pyramide": (70, 254),
    "creux": (344, 305),
    "signal": (65, 375),
    "haut_combe": (166, 390),
    "bas_combe": (231, 458),
    "bas_chapelets": (122, 555),
    "courchevel_1650": (428, 661),
    "haut_belvedere": (298, 585),
    "bas_stade": (247, 593),
    "haut_st_aggate": (359, 613),
    "bosses": (270, 516),
    "haut ariondaz": (191, 463),
    "prameruel": (333, 449),
    "haut_gravelle": (420, 357),
    "haut_aigulle_du_fruit": (486, 256),
    "vizelle": (580, 185),
    "bas_suisse": (464, 376),
    "creux_noirs": (534, 95),
    "bas_creux_noirs": (404, 239),
    "saulire": (644, 164),
    "haut biollay": (550, 351),
    "verdons": (634, 387),
    "pralong": (518, 508),
    "lac": (637, 531),
    "haut_bellecote": (573, 481),
    "haut_rocher_ombre": (667, 333),
    "courchevel_1850": (672, 588),
    "chenus": (795, 406),
    "loze": (810, 447),
    "courchevel_1550": (615, 708),
    "bas_plantrey": (759, 630),
    "haut_epicea": (823, 547),
    "courchevel_1300": (966, 737),
    "st_bon": (773, 815),
    "haut_foret": (869, 503),
    "col_loze": (925, 381),
    "praz_juget": (948, 518),
    "la tania": (1184, 684)
}

#variable globale contenant le sommet de depart et arrivee, et le niverau de difficulte
DEPART = None
ARRIVEE = None
#par defaut le niveau est debutant
NIVEAU = "debutant"
    
#en considerant un multigraphe oriente avec poids sous la forme d'un dictionnaire
#les cles sont les sommets et les valeurs sont des dictionnaires avec les sommets voisins comme cles et comme valeurs les poids des arcs (sous forme de dictonnaire)
#avec dans le dictionnaire du poid des arcs, les cles sont les noms des pistes et les valeurs sont les poids des arcs
#exemple: {"sommet1": {"sommet2": {"piste1": 1, "piste2": 2}, "sommet3": {"piste3": 3}}}
#si le sommet de depart n'est pas dans le multigraphe, retourner None
#si le sommet d'arrivee n'est pas dans le multigraphe, retourner None
#si le sommet de depart est le meme que le sommet d'arrivee, retourner []
#la fonction renvoie une liste de tuples (sommet, piste, poids piste) qui represente le chemin
#ainsi que le poids du chemin
#exemple: ([("sommet1", "piste1", 1), ("sommet2", "piste2", 2)], 3)

def dijkstra(multigraphe, depart, arrivee):
    """retourne le plus court chemin entre deux sommets
    la fonction renvoie une liste de tuples (sommet, piste, poids piste) qui represente le chemin
    et le poids du chemin
    """
    if depart not in multigraphe:
        return None
    if arrivee not in multigraphe:
        return None
    if depart == arrivee:
        return [], 0
    #initialisation
    sommets = list(multigraphe.keys())
    poids = {sommet: float("inf") for sommet in sommets}
    poids[depart] = 0
    pere = {sommet: None for sommet in sommets}
    pere[depart] = depart
    #recherche du plus court chemin
    while sommets:
        sommet = min(sommets, key=lambda sommet: poids[sommet])
        sommets.remove(sommet)
        for voisin in multigraphe[sommet]:
            for piste in multigraphe[sommet][voisin]:
                if poids[voisin] > poids[sommet] + multigraphe[sommet][voisin][piste]:
                    poids[voisin] = poids[sommet] + multigraphe[sommet][voisin][piste]
                    pere[voisin] = sommet, piste, multigraphe[sommet][voisin][piste]
    #reconstruction du chemin
    chemin = []
    sommet = arrivee
    while sommet != depart:
        chemin.append(pere[sommet])
        sommet = pere[sommet][0]
    chemin.reverse()
    return chemin, poids[arrivee]

def recherche_chemin():
    """a l'aide de la fonction dijkstra, recherche le chemin le plus court entre deux sommets
    on traite ensuite chaque cas pour afficher le chemin comme demande dans l'enonce"""
    if NIVEAU == "debutant":
        VERTE = 1
        BLEUE = 4
        ROUGE = 9
        NOIRE = 16  
    elif NIVEAU == "expert":
        VERTE = 1
        BLEUE = 2
        ROUGE = 3
        NOIRE = 4
    graphe = build_graphe(VERTE, BLEUE, ROUGE, NOIRE) #on construit le graphe en fonction du niveau de difficulte
    chemin, poids = dijkstra(graphe, DEPART, ARRIVEE) #on recherche le chemin le plus court
    print("Vous vous trouvez a", DEPART)
    for path in chemin: #on parcourt chaque etape du chemin pour l'afficher proprement
        if path[2] == TELEPHERIQUE:
            print("-Prenez le telepherique", path[1])
        elif path[2] == TELECABINE:
            print("-Prenez la telecabine", path[1])
        elif path[2] == TELESIEGE:
            print("-Prenez le telesiege", path[1])
        elif path[2] == TELESKI:
            print("-Prenez le teleski", path[1])
        else:
            print("-Prenez la piste", path[1])
    print("-Vous etes arrive a", ARRIVEE)
    print(f"-Le trajet devrait vous prendre environ {poids} minutes")
    
def display_image(taille):
    """affiche l'image plan_piste.png dans un canvas de taille TAILLE"""
    fenetre = tkinter.Tk()
    canvas = tkinter.Canvas(fenetre, width=taille[0]+100, height=taille[1]) #on initialise le canvas
    canvas.pack()
    image = Image.open("plan_piste.png") #on ouvre l'image avec PIL pour la redimensionner
    image_resized = ImageTk.PhotoImage(image.resize(taille)) #on redimensionne l'image
    canvas.create_image(0, 0, anchor=tkinter.NW, image=image_resized) #on affiche l'image dans le canvas
    print("clique sur le sommet de depart")
    #detecte les clicks sur le canvas
    def detecte_lieu(event):
        """detecte les clicks sur le canvas et affiche le nom du sommet clique
        met a jour les variables DEPART et ARRIVEE et lance la fonction recherche_chemin()"""
        global DEPART, ARRIVEE
        for key, value in LISTE_LIEU.items():
            #on teste si le click est dans la zone d'erreur du sommet
            if event.x in range(value[0]-ERREUR[0], value[0]+ERREUR[0]) and event.y in range(value[1]-ERREUR[1], value[1]+ERREUR[1]):
                if DEPART is None:
                    DEPART = key
                    print(f"point de depart: {DEPART}\n")
                    print("clique sur le sommet d'arrivee")
                elif ARRIVEE is None:
                    ARRIVEE = key
                    print(f"point d'arrivee: {ARRIVEE}\n")
                    recherche_chemin()
                break
    canvas.bind("<Button-1>", detecte_lieu) #on lie la fonction detecte_lieu() au click gauche sur le canvas

    def niveau_debutant():
        """met a jour la variable NIVEAU et affiche le niveau de difficulte"""
        global NIVEAU
        NIVEAU = "debutant"
        print("niveau: debutant")
    def niveau_expert():
        """met a jour la variable NIVEAU et affiche le niveau de difficulte"""
        global NIVEAU
        NIVEAU = "expert"
        print("niveau: expert")
    #on cree les boutons pour choisir le niveau de difficulte
    button_debutant = tkinter.Button(fenetre, text="debutant", command=niveau_debutant)
    button_expert = tkinter.Button(fenetre, text="expert", command=niveau_expert)
    #on place les boutons
    button_debutant.place(x=taille[0]+10, y=taille[1]//2-20)
    button_expert.place(x=taille[0]+10, y=taille[1]//2+20)
    
    fenetre.mainloop() #on lance la boucle principale

display_image(TAILLE) #on lance le programme
