from classe import *

def morpion(li:list[joueur]):
    """
    Entrée : liste de score
    Procédure qui simule le jeu du morpion, le premier joueur choisi son signe 'X' ou 'O',
    ensuite chaque joueur a tour de role choisi ou placer son signe sur une grille de 3X3.
    Le premier joueur qui aligne ses 3 signe sur un ligne, colonne ou diagonales gagne. Si aucun n’y parvient il y a égalité.
    """
    joueur1 : str
    joueur2 : str
    signe1 : str
    signe2 : str
    case : str
    l1 : list[str]
    l2 : list[str]
    l3 : list[str]
    l4 : list[str]
    l5 : list[str]
    l6 : list[str]
    l7 : list[str]
    A1 : str
    A2 : str
    A3 : str
    B1 : str
    B2 : str
    B3 : str
    C1 : str
    C2 : str
    C3 : str
    testlig1 : bool
    testlig2 : bool
    testlig3 : bool
    testcol1 : bool
    testcol2 : bool
    testcol3 : bool
    testdiag1 : bool
    testdiag2 : bool
    testlig1t : bool
    testlig2t : bool
    testlig3t : bool
    testcol1t : bool
    testcol2t : bool
    testcol3t : bool
    testdiag1t : bool
    testdiag2t : bool
    rempli : int
    
    compteur : int
    signe : str
    test : bool
    testt : bool
    dico_case : dict[str,int]
    gagnant:joueur
    trouve:bool
   
    
    A1 =''
    A2 =''
    A3 =''
    B1 =''
    B2 =''
    B3 =''
    C1 =''
    C2 =''
    C3 =''
    rempli = 0
    testlig1 = False
    testlig2 = False
    testlig3 = False
    testcol1 = False
    testcol2 = False
    testcol3 = False
    testdiag1 = False
    testdiag2 = False
    testlig1t = False
    testlig2t = False
    testlig3t = False
    testcol1t = False
    testcol2t = False
    testcol3t = False
    testdiag1t = False
    testdiag2t = False
    compteur = 0
    test = False 
    testt = False
    dico_case = {'A1':len(A1),'A2':len(A2),'A3':len(A1),'B1':len(A1),'B2':len(A1),'B3':len(A1),'C1':len(A1),'C2':len(A1),'C3':len(A1)}
    joueur1 = str(input("Quel est le prénom du joueur 1 : "))
    joueur2 = str(input("Quel est le prénom du joueur 2 : "))
    
    print(joueur1,end=" ")
    signe1 = str(input("choisissez votre symbole, X ou O : " ))
    while signe1 != "X" and signe1 != "O":
        signe1 = str(input("Vous ne pouvez choisir que X ou O : " ))
        
    if signe1 == "X":
        signe2 = "O"
        compteur = compteur + 1
    elif signe1 == "O":
        signe2 = "X"   
        
    print("Voici la grille de jeu :") 
    l1=["    1    2    3 "]
    l2=["A  "," ","  |  "," ","  |  "," ","  "]
    l3=["  ____|_____|____"]
    l4=["B  "," ","  |  "," ","  |  "," ","  "]
    l5=["  ____|_____|____"]
    l6=["C     |     |    "]
    l7=["   "," ","  |  "," ","  |  "," ","  "]
    ligne=[l1,l2,l3,l4,l5,l6,l7]
    
    for x in ligne:
        print()
        for i in x:
            print(i,end="")
    print()
     
           
    
    while rempli < 9 and test != True and testt != True :
            
        compteur = compteur + 1
        
        case = input("saisissez en quelle case vous souhaitez placer votre symbole (ex : 'B3'):")
        
        while case not in dico_case:
            case = input("Cette case est incorrecte, veuillez saisir une autre case : ")
            
        while dico_case[case]>0:
            case = input("Cette case est deja prise, veuillez saisir une autre case : ")
            
                
        if compteur % 2 == 0 :
            signe = signe1
            print("C'est a ",joueur1," de jouer.")
        else:
            signe = signe2
            print("C'est a ",joueur2," de jouer.")
        
        if case[0] == "A":
            if case[1] == "1" and len(A1) == 0 :
                l2[1]=signe
                A1 = signe
            elif case[1] == "2" and len(A2) == 0 :
                l2[3]=signe
                A2 = signe
            elif case[1] == "3" and len(A3) == 0 :
                l2[5]=signe
                A3 = signe
        if case[0] == "B":
            if case[1] == "1" and len(B1) == 0 :
                l4[1]=signe
                B1 = signe
            elif case[1] == "2" and len(B2) == 0 :
                l4[3]=signe
                B2 = signe
            elif case[1] == "3" and len(B3) == 0 :
                l4[5]=signe
                B3 = signe
        if case[0] == "C":
            if case[1] == "1" and len(C1) == 0 :
                l7[1]=signe
                C1 = signe
            elif case[1] == "2" and len(C2) == 0 :
                l7[3]=signe
                C2 = signe
            elif case[1] == "3" and len(C3) == 0 :
                l7[5]=signe
                C3 = signe

        for x in ligne:
            print()
            for i in x:
                print(i,end="")
        print()
   
        testlig1 = A1==signe1 and A2==signe1 and A3==signe1
        testlig2 = B1==signe1 and B2==signe1 and B3==signe1
        testlig3 = C1==signe1 and C2==signe1 and C3==signe1
        testcol1 = A1==signe1 and B1==signe1 and C1==signe1
        testcol2 = A2==signe1 and B2==signe1 and C2==signe1
        testcol3 = A3==signe1 and B3==signe1 and C3==signe1
        testdiag1 = A1==signe1 and B2==signe1 and C3==signe1
        testdiag2 = A3==signe1 and B2==signe1 and C1==signe1
        
        testlig1t = A1==signe2 and A2==signe2 and A3==signe2
        testlig2t = B1==signe2 and B2==signe2 and B3==signe2
        testlig3t = C1==signe2 and C2==signe2 and C3==signe2
        testcol1t = A1==signe2 and B1==signe2 and C1==signe2
        testcol2t = A2==signe2 and B2==signe2 and C2==signe2
        testcol3t = A3==signe2 and B3==signe2 and C3==signe2
        testdiag1t = A1==signe2 and B2==signe2 and C3==signe2
        testdiag2t = A3==signe2 and B2==signe2 and C1==signe2
        
        rempli = len(A1) + len(A2) + len(A3) + len(B1) + len(B2) + len(B3) + len(C1) + len(C2) + len(C3)
        test = testlig1==True or testlig2==True or testlig3==True or testcol1==True or testcol2==True or testcol3==True or testdiag1==True or testdiag2==True
        testt = testlig1t==True or testlig2t==True or testlig3t==True or testcol1t==True or testcol2t==True or testcol3t==True or testdiag1t==True or testdiag2t==True
        
        dico_case = {'A1':len(A1),'A2':len(A2),'A3':len(A3),'B1':len(B1),'B2':len(B2),'B3':len(B3),'C1':len(C1),'C2':len(C2),'C3':len(C3)}
        
        print()
        print()
        print()
    
    gagnant=joueur()
    trouve=False
    if test == True :
        print ("Le joueur 1 a gagner.")
        for i in range(len(li)):
            if joueur1==li[i].nom:
                li[i].score+=1
                trouve=True
    
        if not trouve:
            gagnant.nom=joueur1
            gagnant.score=1
            li.append(gagnant)

    elif testt == True :
        print (f"Le joueur2 a gagner.")
        for i in range(len(li)):
            if joueur2==li[i].nom:
                li[i].score+=1
                trouve=True
    
        if not trouve:
            gagnant.nom=joueur2
            gagnant.score=1
            li.append(gagnant)
    elif rempli == 9 :
        print ("Egalité.")
    
