#import de 2 bibliothèque
import os
import pickle

#import de toutes les données du fichier Personne
from personne import *

#affichage du menu
def menu(liste):
    print("1. Afficher le listing")
    print("2. Inscrire un nouveau membre")
    print("3. Quitter")
    choix = 0
    while choix < 1 or choix > 3:
        choix = int(input())
    if choix == 1:
        afficher_listing(liste)
        input()
        menu(liste)
    elif choix == 2:
        inscription(liste)
        menu(liste)
    elif choix == 3:
        return 0

#choix numéro 1 on affiche la liste des membres
def afficher_listing(liste):
    for membre in liste:
        print(membre)

#Choix numéro 2 on demande d'introduire les données du nouvel arrivant 
def inscription(liste):
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    dateNaissance = input("Date de naissance : ")
    mail = input("Adresse e-mail : ")
    telephone = input("Numéro de téléphone : ")
    adresse = input("Adresse : ")
    liste.append(Personne(prenom, nom, dateNaissance, mail, telephone, adresse))
    enregistrer_listing(liste)

#Fonction permettant de récuperer la liste contenant les infos sur chaque personnes
def recup_listing():
    if os.path.exists("listing"):
        fichier_listing = open("listing", "rb")
        mon_depickler = pickle.Unpickler(fichier_listing)
        listing = mon_depickler.load()
        fichier_listing.close()
    else:
        listing = []
    return listing

#fonction permmettant d'enregistrer les données introduite par l'utilisateur dans le fichier reprenant toutes les informations
def enregistrer_listing(liste):
    with open('listing', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(liste)