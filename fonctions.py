import os
import pickle
from Personne import *

def menu(listing):
    print("1. Afficher le listing")
    print("2. Inscrire un nouveau membre")
    print("3. Quitter")
    choix = 0
    while choix < 1 or choix > 3:
        choix = int(input())
    if choix == 1:
        afficher_listing(listing)
        input()
        menu(listing)
    elif choix == 2:
        inscription(listing)
        menu(listing)
    elif choix == 3:
        return 0

def afficher_listing(listing):
    for membre in listing:
        print(membre)

def inscription(listing):
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    dateNaissance = input("Date de naissance : ")
    mail = input("Adresse e-mail : ")
    telephone = input("Numéro de téléphone : ")
    adresse = input("Adresse : ")
    listing.append(Personne(prenom, nom, dateNaissance, mail, telephone, adresse))
    enregistrer_listing(listing)

def recup_listing():
    if os.path.exists("listing"):
        fichier_listing = open("listing", "rb")
        mon_depickler = pickle.Unpickler(fichier_listing)
        listing = mon_depickler.load()
        fichier_listing.close()
    else:
        listing = []
    return listing

def enregistrer_listing(listing):
    with open('listing', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(listing)