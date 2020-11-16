import os
import pickle
from personne import *

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

def afficher_listing(liste):
    for membre in liste:
        print(membre)

def inscription(liste):
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    dateNaissance = input("Date de naissance : ")
    mail = input("Adresse e-mail : ")
    telephone = input("Numéro de téléphone : ")
    adresse = input("Adresse : ")
    liste.append(Personne(prenom, nom, dateNaissance, mail, telephone, adresse))
    enregistrer_listing(liste)

def recup_listing():
    if os.path.exists("listing"):
        fichier_listing = open("listing", "rb")
        mon_depickler = pickle.Unpickler(fichier_listing)
        listing = mon_depickler.load()
        fichier_listing.close()
    else:
        listing = []
    return listing

def enregistrer_listing(liste):
    with open('listing', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(liste)