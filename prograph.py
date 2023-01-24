import matplotlib.pyplot as plt

import numpy as np
import datetime
import csv
fh=open('C:/Users/salam/Downloads/S.txt','r')
#print(ress)
#tableau_evenements=np.array([])

info=''
heure=''
identifiant=''
seq=''
ipsource=''
ipdest=''
ack=''
win=''
flags=''
options=''
mot=''
val=''
ecr=''
length=''
titre=''
continu= True
titre="heure"+";"+"ipsource"+";"+"ipdest"+";"+"flags"+";"+"id"+";"+"seq"+";"+"ack"+";"+"win"+";"+"options"+";"+"lenght"
valeur=[]
liste_valeur_split=[]
texte=[]

while continu:
    line=fh.readline()
    
    
    if "seq" in line and "id" in line:
        
        texte=line.split(", ")
        
        identifiant=texte[1]
        seq=texte[2]
        contenu_heure=line.split("IP")
        heure=contenu_heure[0]
                        
        if "IP" in line:
            texte=line.split("IP")
            ips=texte[1].split(">")
            ipd=ips[1].split(":")
            ipsource=ips[0]
            ipdest=ipd[0]

        if "Flags" in line:
            texte=line.split(":")
            texte2=texte[3].split(",")
            flags=texte2[0]
            
        #if "length" in line:
            #texte=line.split(":")
            #texte2=texte[3].split("\n")
            #texte3=texte2[0].split(", ")
            
            #length=texte3[3]
            
        info=heure+";"+ipsource+";"+ipdest+";"+flags+";"+identifiant+";"+seq+";"+" "+";"+" "+";"+" "+";"+" "
        valeur.append(info)

    elif "ack" in line and "seq" in line:
        
        texte=line.split(", ")
        seq=texte[1]
        ack=texte[2]
        win=texte[3]

        contenu_heure=line.split("IP")
        heure=contenu_heure[0]
                        
        if "IP" in line:
            texte=line.split("IP")
            ips=texte[1].split(">")
            ipd=ips[1].split(":")
            ipsource=ips[0]
            ipdest=ipd[0]
            
        if "Flags" in line:
            texte=line.split(":")
            texte2=texte[3].split(",")
            flags=texte2[0]
            
        if "options" in line:
            texte=line.split(", ")
            options=texte[4]
        
            
        #if "length" in line:
            #texte=line.split(":")
            #texte2=texte[3].split("\n")
            #texte3=texte2[0].split("]")
            
            
        info=heure+";"+ipsource+";"+ipdest+";"+flags+";"+" "+";"+seq+";"+ack+";"+win+";"+options
        valeur.append(info)
        
    elif "seq" in line and "win" in line:
        
        texte=line.split(", ")
        seq=texte[1]
        win=texte[2]
        
        contenu_heure=line.split("IP")
        heure=contenu_heure[0]
                        
        if "IP" in line:
            texte=line.split("IP")
            ips=texte[1].split(">")
            ipd=ips[1].split(":")
            ipsource=ips[0]
            ipdest=ipd[0]
            
        if "Flags" in line:
            texte=line.split(":")
            texte2=texte[3].split(",")
            flags=texte2[0]
            
        if "length" in line:
            texte=line.split(", ")
            texte2=texte[3].split(":")
            length=texte2[0]
                    
        info=heure+";"+ipsource+";"+ipdest+";"+flags+";"+" "+";"+seq+";"+" "+";"+win+";"+" "+";"+length
        valeur.append(info)
     
        

    if "ack" in line and "Flags [.]" in line:
        
        
        contenu_heure=line.split("IP")
        heure=contenu_heure[0]
            
        if "IP" in line:
            texte=line.split("IP")
            ips=texte[1].split(">")
            ipd=ips[1].split(":")
            ipsource=ips[0]
            ipdest=ipd[0]
            
        if "Flags" in line:
            texte=line.split(":")
            texte2=texte[3].split(",")
            flags=texte2[0]
            
        if "ack" in line:
            texte=line.split(", ")
            ack=texte[1]
            
        if "win" in line:
            texte=line.split(", ")
            win=texte[2]
            
        if "options" in line:
            texte=line.split(", ")
            options=texte[3]
    
        #if "length" in line:
            #texte=line.split(":")
            #texte2=texte[3].split("\n")
            #texte3=texte2[0].split("]")
            
            #length=texte3[2]
        
        info=heure+";"+ipsource+";"+ipdest+";"+flags+";"+" "+";"+" "+";"+ack+";"+win+";"+options
        valeur.append(info)

            
       
    if line == '':  
        print("end of file")
        break          
     


for j in range (len(valeur)):
    valeur_split=valeur[j].split(",")
    liste_valeur_split.append(valeur_split)
    
    
with open('data.csv','a') as file:
    
    writer=csv.writer(file)
    writer.writerow([titre])
    
    labels = 'Flags [F.]', 'Flags [.]', 'Flags [S]', 'Flags [P.]'
    sizes = [15, 80, 45, 40]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('PieChart01.png')
    plt.show()
    
    for i in range (len(liste_valeur_split)):
        writer.writerow(liste_valeur_split[i])
        print(liste_valeur_split[i])
    file.close()            

    


fh.close()  
   
