from menu import menuScore
from classe import joueur

def triBulle(li:list[joueur]):
    """
    entrée: une liste de joueur

    cette  fonction fait un tri a bulle sur la liste donnée dans un ordre décroissant
    """

    p:int
    i:int
    temp:joueur
    echange:bool

    echange=True
    p=len(li)
    while echange and p>0:
        echange=False
        for i in range(p-1):
            if li[i].score<li[i+1].score:
                temp=li[i]
                li[i]=li[i+1]
                li[i+1]=temp
                echange=True
        p-=1


def affichageScore(li:list[joueur]):
    """
    entrée : une liste de joueur

    la procedure afficge un classement des joueur dans la liste
    """
    triBulle(li)
    for i in range(len(li)):
        print(i+1,"-","pseudo :",li[i].nom,"score :",li[i].score)

def score(li1:list[joueur],li2:list[joueur],li3:list[joueur]):
    """
    entrée : 3 liste joueur

    la procedure sert à choisir un jeux pour afficher son classement 
    """
    choix:int

    while True:
        menuScore()
        choix=int(input("faites un choix : "))
        
        if choix==1:
            if len(li1)!=0:
                affichageScore(li1)
            else:
                print("vous n'avez pas encore joué a ce jeu")
        if choix==2:
            if len(li2)!=0:
                affichageScore(li2)
            else:
                print("vous n'avez pas encore joué a ce jeu")

        if choix==3:
            if len(li3)!=0:
                affichageScore(li3)
            else:
                print("vous n'avez pas encore joué a ce jeu")
        
        if choix==5:
            break
        
            

