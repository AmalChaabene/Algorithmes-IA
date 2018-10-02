# -*- coding: cp1252 -*-
import sys
import os.path

class unification:

    def extractFonction(self,var):
        tabOuv=[]
        nb=0
        i=0
        list=[]
        while i<len(var):

            if var[i]=='(':	
                tabOuv.append(i)
                nb+=1
                i=i+1
	
            if var[i]==')':  
                nb=nb-1
                i=i+1
                if nb==0:
                    ch=var[tabOuv[0]-1:i]
                    list.append(ch)
                    tabOuv=[]

            else:
                i=i+1

        return (list)


    def extract1element(self,var):
        i=0
        
        while i<len(var):
            if var[i]==',':
                ch=var[0:i]
                if '(' in ch:
                    list=self.extractFonction(var)
                    return list[0]
                    
                else:
                    return var[0:i]
            else:
                if i==(len(var)-1):
                    return var
                else:
                    i=i+1
                
        

    def unifierAtome(self,atome1,atome2):
        l1=len(atome1)
        l2=len(atome2)
        global ch

        if l1==1 and l2==1 and atome1!=atome2:
            print ("Echec: Deux constantes différentes")
            sys.exit()

        if l1==1 and l2==1 and atome1==atome2:
            return(atome2,atome1)
            
        if l1==1 and l2==2:
            return(atome2,atome1)
            
        if l1==2 and l2==1:   
            return(atome1,atome2)
        
        if l1==2 and l2==2:  
            return(atome2,atome1)

        if l1==2 and l2>2:
            if atome2.find(atome1)!= -1:
                print ("Echec:fonction/variable: "+atome1+" existe dans "+atome2)
                if test=="true":
                    fich = open('trace.txt','w')
                    ch=ch+"\n"+"echec"
                    fich.write(str(ch))
                    fich.close()
                    ch=""
                sys.exit()

            else:
                return(atome1,atome2)  

        if l1>2 and l2==2:
            if atome1.find(atome2)!= -1:
                print ("Echec:fonction/variable: "+atome2+" existe dans "+atome1)
                if test=="true":
                    fich = open('trace.txt','w')
                    ch=ch+"\n"+"echec"
                    fich.write(str(ch))
                    fich.close()
                    ch=""
                sys.exit()

            else:
                return(atome2,atome1)
                

        else:
            print ("Echec type atomes: "+atome1+" et "+atome2)
            if test=="true":
                fich = open('trace.txt','w')
                ch=ch+"\n"+"echec"
                fich.write(str(ch))
                fich.close()
                ch=""
            sys.exit()


    def substitution(self,atome1,atome2):
        global r1
        global r2
        global ch
        

        r1=r1.replace(atome1,atome2)
        r2=r2.replace(atome1,atome2)
        
        print ("Substitution "+ atome1 +" par " +atome2)
        ch=ch+"\n"+"Substitution "+ atome1 +" par " +atome2
        
        
        
        
        
        
    
    
    def unifier(self,var1,var2):
        global r1
        global r2
        global test
        global ch
        
      

        if (len(var1)!=0 and len(var2)!=0):

            
            
            p1=self.extract1element(var1)
            p2=self.extract1element(var2)

            
            if (len(p1)!=0 and len(p2)!=0):

                if len(p1)>2 and len(p2)>2:
                    if p1[0]==p2[0]:
                        self.unifier(var1[2:(len(p1)-1)]+var1[(len(p1)):],var2[2:(len(p2)-1)]+var2[(len(p2)):])
                    else:
                        print (var1[0] + " est different de " + var2[0])

                

                else:
                    
                    r1=var1[len(p1)+1:]
                    r2=var2[len(p2)+1:]
                   

                    a1,a2=self.unifierAtome(p1,p2)
                    self.substitution(a1,a2)
                    
                    self.unifier(r1,r2)

        elif (len(var1)==0 and len(var2)!=0) or (len(var1)!=0 and len(var2)==0):
            print "Echec longueur"
            if test=="true":
                fich = open('trace.txt','w')
                ch=ch+"\n"+"echec"
                fich.write(str(ch))
                fich.close()
                ch=""
        else:
            print "succes"
            if test=="true":
                fich = open('trace.txt','w')
                ch=ch+"\n"+"succes"
                fich.write(str(ch))
                fich.close()
                ch=""
                
            
        
        
print("choisir le jeu de 1 a 4")
x = raw_input()
l1=""
l2=""
test=""
ch=""

print("Voulez-vous sauvegarder la trace ? o/n ")
rep = raw_input()
        
if rep == "o":
    test="true"

    
else:
    test="false"
    

if (x=="1") :
    f=open('jeu1.txt')
    lines=f.readlines()
    l11=lines[0]
    t=l11.split(" ")
    l1=t[0]
    l2=t[1]
    

elif (x=="2") :
    f=open('jeu2.txt')
    lines=f.readlines()
    l11=lines[0]
    t=l11.split(" ")
    l1=t[0]
    l2=t[1]
        
elif (x=="3") :
    f=open('jeu3.txt')
    lines=f.readlines()
    l11=lines[0]
    t=l11.split(" ")
    l1=t[0]
    l2=t[1]
        
elif (x=="4") :
    f=open('jeu4.txt')
    lines=f.readlines()
    l11=lines[0]
    t=l11.split(" ")
    l1=t[0]
    l2=t[1]
        


else:
    print "Choix invalide"
    sys.exit()


a=unification()
a.unifier(l1,l2)
r1=""
r2=""









