from classe import joueur

def allumette(li:list[joueur]):
    """
    Entrée : liste de joueur
    Procédure qui simule le jeu des alumettes, il y a au départ 20 alumettes a chaque joueur joue chacun son tour,
    il peut retirer 1,2 ou 3 alumettes, le joueur qui arrive a 0 perd la partie.
    """
    numeroJoueur:int
    nbAllumette:int
    joueurs:list[str]
    retrait:int
    trouve:bool
    gagnant:joueur

    gagnant=joueur()
    joueurs=[input("entrer le nom du joueur 1 : "),input("entrer le nom du joueur 2 : ")]
    nbAllumette=20
    numeroJoueur=0
    while nbAllumette>0: #fait jouer des tours tant qu'il reste des allumettes
        print()
        for i in range(nbAllumette):
            print("| ",end="")
        if nbAllumette!=1:
            print("\n\nil reste",nbAllumette,"allumettes")
        else:
            print("\n\nil reste",nbAllumette,"allumette")
        print()
        if nbAllumette==1:
            print("defaite obligatoire partie terminée")
            nbAllumette-=1
        else:
            print(joueurs[numeroJoueur],"enlevez 1,2 ou 3 allumettes : ",end="")
            retrait=int(input())
            while retrait<1 or retrait>3:
                retrait=int(input("erreur de saisi, veuillez retirer 1,2 ou 3 allumettes : "))
            nbAllumette-=retrait
        numeroJoueur=(numeroJoueur+1)%2
    print()
    print(joueurs[(numeroJoueur+1)%2],"a perdu")
    trouve=False
    for i in range(len(li)):
        if joueurs[numeroJoueur]==li[i].nom:
            li[i].score+=1
            trouve=True
    
    if not trouve:
        gagnant.nom=joueurs[numeroJoueur]
        gagnant.score=1
        li.append(gagnant)

