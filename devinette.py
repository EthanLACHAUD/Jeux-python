from classe import *

def devinette(li:list[joueur]): 
    """
    Entrée : liste de joueur
    Procédure qui simule le jeu du juste prix, les joueurs choisisse une limite > 0, 
    un des joueur choisis le nombre secret a trouver entre 0 et la limite, 
    l’autre joueur saisis des nombres afin de trouver le nombre secret le programme affiche "trop grand" ou "trop petit" 
    en fonction du nombre saisis par rapport au nombre secret. Si le joueur trouve le nombre en moins de 10 tours il gagne, 
    sinon il perd.
    """
    limite : int 
    choix_nb : int
    nb : int
    joueur1 : str
    joueur2 : str
    nb_tour : int
    victoire : bool
    gagnant : joueur
    trouve : bool
    
    gagnant=joueur()
    joueur1 = str(input("Quel est le prénom du joueur 1 : "))
    joueur2 = str(input("Quel est le prénom du joueur 2 : "))
    
    
    limite = int(input("Saisissez la limite : "))
    while limite <= 1:
        limite = int(input("Resaisissez la limite, la limite doit etre superieur a 1 : "))
        
    choix_nb = int(input("Saisissez le nombre secret : "))
    
    while choix_nb <= 1 or choix_nb > limite:
        choix_nb = int(input("Votre nombre doit être superieur a 1 et inferieur a la limite, resaisissez le nombre : "))
      
    print("Proposez un nombre entre 1 et ", limite," : ",end="")  
    nb = int(input())
    
    while nb < 1 or nb > limite :
        print("Votre nombre doit etre plus grand 1 et inferieur a ", limite," : ",end="")  
        nb = int(input())
    
    nb_tour=1
    victoire=False
    while not victoire and nb_tour<10 :
        if nb < choix_nb :
            print("trop petit")
        elif nb > choix_nb :
            print("trop grand")
        elif nb == choix_nb :
            victoire=True
        
        if not victoire :
            print("Reproposez un nombre entre 1 et ", limite,":",end=" ")
            nb = int(input())
            while nb < 1 or nb > limite :
                print("Votre nombre doit etre plus grand 1 et inferieur a ", limite," : ",end=" ")  
                nb = int(input())
        
        nb_tour+=1
    trouve=False
    if victoire :
        print(joueur2,"a gagné")
        for i in range(len(li)):
            if joueur2==li[i].nom:
                li[i].score+=1
                trouve=True
    
        if not trouve:
            gagnant.nom=joueur2
            gagnant.score=1
            li.append(gagnant)
    else :
        print(joueur1,"a gagné")
        for i in range(len(li)):
            if joueur1==li[i].nom:
                li[i].score+=1
                trouve=True
    
        if not trouve:
            gagnant.nom=joueur1
            gagnant.score=1
            li.append(gagnant)
    
            
    
