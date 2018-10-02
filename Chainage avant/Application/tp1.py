# -*- coding: utf-8 -*-



import sys
import os.path
class Regle:
    premisse = []
    conclusion = []
    etat = "True"
    idn = 0
    def __init__(self,premisse,conclusion,etat,idn):
		self.premisse = premisse
		self.conclusion = conclusion
		self.etat = etat
		self.idn = idn


class Fait:
    fait = []
    numRegle = 0

    def __init__(self,fait,numRegle):
                self.fait = fait
                self.numRegle = numRegle



class definition:

 
    def listeRegles(self):
        print("Donner le nom du fichier des regles")
        x = raw_input()
        if os.path.exists(x):
            f = open(x,"r")
        else :
            print("file not found")
            sys.exit()
      
        listeR = []
        for line in f:
            
            pre = []
            nouv=line.split(" ")
            k = nouv.index("alors")
            n = nouv[0]
            num = n[1:-3]
            
            i = 1
            while i < k:
                pre.append(nouv[i])
                i = i + 2
            
            concl = nouv[k+1]
            c=concl[0:-1]

            r = Regle(pre,c,"True",num)
            #print(r.conclusion)
            
            listeR.append(r)
            
       
        f.close()
        return(listeR)

#******************************************************************
    def listeFaits(self):
        print("Donner le nom du fichier des faits")
        x = raw_input()
        if os.path.exists(x):
            f = open(x,"r")
        else :
            print("file not found")
            sys.exit()
            
        listeF = []
        line = f.read()
        
        faits=line.split(",")
        
        for i in faits:
            ft = Fait(i,-1)
            listeF.append(ft)
            
   
        f.close()
        return(listeF)
    
#****************************************************************** 
    def regleDecl(self,regle,f,chemin,x):
        decl = []
        faits = []
        
        for i in f:
            
            faits.append(i.fait)

        
        for r in regle:
            if set(r.premisse)<set(faits):
                decl.append(r)
        if decl :
            return(decl)
        else :
            if (x == 1):
                print ("but non atteint")
            print(chemin)
            print("Voulez-vous sauvegarder la trace ? o/n ")
            rep = raw_input()
        
            if rep == "o":
                fich = open('trace.txt','w')
                fich.write(str(chemin))
                fich.close()
            else:
                fich = open('trace.txt','w')
                fich.write("")
                fich.close()

            
        
            sys.exit()
        
        
       

#******************************************************************    
    def choixRegle(self,liste,choix):
        tmp = []
        if choix == "1" :
            return(liste[0])
        elif choix == "2":
            for i in liste:
                tmp.append(len(i.premisse))

            
            indice = tmp.index(max(tmp))
            return(liste[indice])
        else:
            print("mauvais choix")
            sys.exit()
#******************************************************************  
    def change (self,regle,indice):
        regle[indice].etat = "False"
        return(regle)
#******************************************************************            
    def saturation(self,regles,faits,choice):
        chemin = []
        x = 1
        a = definition()
        reglDec = a.regleDecl(regles,faits,chemin,x)
        choix=a.choixRegle(reglDec,choice)
        chemin.append(choix.idn)

        ff = []
        
        for i in faits:
            
            ff.append(i.fait)
     
        while choix :

            ft = Fait(choix.conclusion,choix.idn)
            
            if (choix.conclusion[4:-1] in ff) or ("non("+choix.conclusion+")" in ff):
                print("contraduction dans la base des faits")
                sys.exit()
                
            faits.append(ft)
            # r = a.change(regles,choix.idn)
            regles.remove(choix)
            reglDec = a.regleDecl(regles,faits,chemin,x)
            choix = a.choixRegle(reglDec,choice)
            chemin.append(choix.idn)
      
#******************************************************************            
    def butAtteint(self,regles,faits,but,choice):
        chemin = []
        a = definition()
        x = 1
        reglDec = a.regleDecl(regles,faits,chemin,x)
        choix=a.choixRegle(reglDec,choice)
        chemin.append(choix.idn)
        ff = []
        
        for i in faits:
            
            ff.append(i.fait)
        if (choix.conclusion[4:-1] in ff) or ("non("+choix.conclusion+")" in ff):
                print("contraduction dans la base des faits")
                sys.exit()
        while (choix.conclusion != but) :
            ft = Fait(choix.conclusion,choix.idn)

            if (choix.conclusion[4:-1] in ff) or ("non("+choix.conclusion+")" in ff):
                print("contraduction dans la base des faits")
                sys.exit()
                
            faits.append(ft)
            # r = a.change(regles,choix.idn)
            regles.remove(choix)
            reglDec = a.regleDecl(regles,faits,chemin,x)
            choix = a.choixRegle(reglDec,choice)
            chemin.append(choix.idn)
            
        print("but atteint")
        print(chemin)

        print("Voulez-vous sauvegarder la trace ? o/n ")
        rep = raw_input()
        
        if rep == "o":
            fich = open('trace.txt','w')
            fich.write(str(chemin))
            fich.close()
        else:
            fich = open('trace.txt','w')
            fich.write("")
            fich.close()
            
       
        sys.exit()
        

#******************************************************************
                
    def choixSortie(self):
        print("Entrer votre choix :")
        print("1 : but trouve")
        print("2 : saturation de la base des faits") 
        choix = raw_input()
        if (choix != "2") and (choix != "1"):
            print("mauvais choix")
            sys.exit()
        a=definition()
        regles = a.listeRegles()
        faits = a.listeFaits()
       
        print("Entrer votre choix de la regle à declencher:")
        print("1 : premiere regle")
        print("2 : regle ayant le plus de premisses")
        choice = raw_input()
        if (choice != "2") and (choice != "1"):
            print("mauvais choix")
            sys.exit()

        if choix == "1":
            
            print("Entrer le but recherche")
            but = raw_input()
            a.butAtteint(regles,faits,but,choice)
        elif choix == "2":
            a.saturation(regles,faits,choice)
        else:
            print("mauvais choix mlthode")
            sys.exit()




a = definition()
b = a.choixSortie()





            
            

        

        
      

   
        
        
        
        
    


    
    
    



