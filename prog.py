# Importe des bibliothèques ou des programmes (nom de la library)
import re
import csv

# Initialise une chaine avec 1 espace
ssh33= " "
# Expression régulière d'une adresse IP (\d -> chiffre {1,3} comprenant entre 
# 1 et 3 chiffres; \. suivit du caaractère '.' etc)
IP_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# Ouvre le fichier mentionné en lecture seul ("r")
with open("C:/Users/cmcol/Desktop/IUT_RT/SAE 15/DumpFile.txt", "r") as f:
    
    # Initialise des variables de type compteur
    compteur_http = 0
    compteur_https = 0
    compteur_http_final = 0
    compteur_domaine = 0
    compteur_ssh = 0  
    compteur_icmp = 0
    compteur_icmp_req = 0
    compteur_icmp_rep = 0
    compteur_flags_connexion = 0
    compteur_flags_SynAcK = 0
    compteur_flags_deco = 0
    compteur_flags_push = 0
    compteur_flags_nokonnexion = 0
    compteur = 0
    # Initialise un tableau de 60 nombres initialisés à 0 (tableau des secondes dans une minutes)
    tab = [0]*60
     
    # Pour chaque ligne dans le fichier f
    for line in f:
        # Cherche une heure au format HH:mm:ss
        match = re.search(r"\d{2}:\d{2}:\d{2}", line)
        # La ligne contient une heure
        if match:
            # Si HH:mm:45 -> inc le comnpteur de 1 de tab[45]
            tab[int(line[6]+line[7])]+=1
            # Compte le nombre d'occurences de http 
            if 'http' in line:
                # Compteur de http + https
                compteur_http = compteur_http +1
                # Compteur uniquement des https
                compteur_http_final  = compteur_http - compteur_https

            # Compte le nombre d'occurences de domain 
            if '.domain' in line:
                compteur_domaine = compteur_domaine + 1
            # Compte le nombre d'occurences de ssh    
            if 'ssh' in line:
                compteur_ssh = compteur_ssh +1
            # Compte le nombre d'occurences de https    
            if 'https' in line:
                compteur_https = compteur_https + 1
            # Compte le nombre d'occurences de ICMP
            if 'ICMP' in line:
                compteur_icmp = compteur_icmp + 1
            # Compte le nombre d'occurences de ICMP request               
            if 'ICMP echo request' in line:
                compteur_icmp_req = compteur_icmp_req + 1
            # Compte le nombre d'occurences de ICMP reply                               
            if 'ICMP echo reply' in line:
                compteur_icmp_rep = compteur_icmp_rep + 1
            # Compte le nombre d'occurences de chaque flag                               
            if 'Flags [S]' in line:
                compteur_flags_connexion = compteur_flags_connexion +1
            if 'Flags [S.]' in line:
                compteur_flags_SynAcK = compteur_flags_SynAcK +1
            if 'Flags [F.]' in line:
                compteur_flags_deco = compteur_flags_deco +1
            if 'Flags [P.]' in line:
                compteur_flags_push = compteur_flags_push +1
            if 'Flags [.]' in line:
                compteur_flags_nokonnexion = compteur_flags_nokonnexion +1
            # Compte le nombre d'occurences d'adresse IP                                               
            for ip in IP_pattern.findall(line):
                compteur += 1
    print("nombre",compteur,"d'ip")
    
    # On a fini de parcourir tout le fichier f        
    # Ouvre le fichier mentionné en écriture et ajout
    with open('aAAAa.csv','a') as file:
        # Ecrit les données au format csv ';'
        # Nom des colonnes  (header)
        fieldnames = ["secondes","nb de trame"]
        # Création d'un objet CSVWriter pour écrire du csv dans le fichier
        # Separateur = ; et le nom des champs/colonnes secondes et nb de trame
        writer =csv.DictWriter(file, delimiter = ";", fieldnames=fieldnames)
        # Ecrit le nom des colonnes dans le fichier
        writer.writeheader()
        # de 0 à 59 (Tab a une taille de 60)
        for i in range(len(tab)):
            # Si le nb de trame est > 150 à la seconde i
            if tab[i] > 150:
                writer.writerow({"secondes" : i, "nb de trame": tab[i]})
        # ferme le fichier et écrit le contenu dans le fichier
        file.close()
                    
    
    # Affiche les résultats
    print("Protocol et le nombre de trames associées:")
    print('ssh:',compteur_ssh)
    print("http:",compteur_http_final)
    print("https:",compteur_https)
    print("dns:",compteur_domaine)
    print("icmp total:",compteur_icmp)
    print("icmp_req:",compteur_icmp_req)
    print("icmp_rep:",compteur_icmp_rep)
    print("il y a",compteur_flags_connexion,"de connexion demandé")
    print("il y a",compteur_flags_SynAcK,"packet SynAcK")
    print("il y a",compteur_flags_deco,"demande deconexion demandé")
    print("il y a",compteur_flags_push,"flags pushs")
    print("il y a",compteur_flags_nokonnexion,"No Flag Set")
    if compteur_icmp_rep != compteur_icmp_req:
        print("possible attack")