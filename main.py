from allumette import *
from devinette import *
from morpion import *
from classe import *
from menu import *
from score import *
import pickle
from typing import BinaryIO


if __name__=="__main__":
    
    choix:int
    gagnant:str
    scoredevinette:list[joueur]
    scoreallumette:list[joueur]
    scoremorpion:list[joueur]
    f:BinaryIO
    

    choix=0
    scoreallumette=[]
    scoredevinette=[]
    scoremorpion=[]
    try: #lit les score dans un fichier binaire
        f=open("score.dat","rb")
        scoredevinette=pickle.load(f)
        scoreallumette=pickle.load(f)
        scoremorpion=pickle.load(f)
        f.close()
    except FileNotFoundError: #créer le fichier si il n'exise pas
        f=open("score.dat","wb")
        pickle.dump(scoredevinette,f)
        pickle.dump(scoreallumette,f)
        pickle.dump(scoremorpion,f)
        f.close()
    
    while choix!=5:
        menu()
        choix=int(input("faites un choix : "))
        if choix==1:
            print("règle :\n\nles joueurs choisisse une limite > 0, un des joueur choisis le nombre secret a trouver entre 0 et la limite, l’autre joueur saisis des nombres afin de trouver le nombre secret le programme affiche \"trop grand\" ou \"trop petit\" en fonction du nombre saisis par rapport au nombre secret. Si le joueur trouve le nombre en moins de 10 tours il gagne, sinon il perd.")
            devinette(scoredevinette)
        elif choix==2:
            print("règle :\n\nil y a au départ 20 alumettes a chaque joueur joue chacun son tour, il peut retirer 1,2 ou 3 alumettes, le joueur qui arrive a 0 perd la partie.")
            allumette(scoreallumette)
        elif choix==3:
            print("règle :\n\n le premier joueur choisi son signe 'X' ou 'O', ensuite chaque joueur a tour de role choisi ou placer son signe sur une grille de 3X3. Le premier joueur qui aligne ses 3 signe sur un ligne, colonne ou diagonales gagne. Si aucun n’y parvient il y a égalité.")
            morpion(scoremorpion)
        elif choix==4:
            score(scoredevinette,scoreallumette,scoremorpion)
        elif choix==5:
            print("Au revoir")
            f=open("score.dat","wb") #enregistre les score dans un fichier binaire
            pickle.dump(scoredevinette,f)
            pickle.dump(scoreallumette,f)
            pickle.dump(scoremorpion,f)
            f.close()
        else:
            print("erreur de saisi")
