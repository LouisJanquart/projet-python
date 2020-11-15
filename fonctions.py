import os
import pickle

class Personne():
    def __init__(self, prenom, nom, dateNaissance = "--/--/----", mail = "mail@mail.com", telephone = "0000 00 00 00", adresse = "---"):
        self._prenom = prenom
        self._nom = nom
        self._dateNaissance = dateNaissance
        self._mail = mail
        self._telephone = telephone
        self.adresse = adresse

    def __repr__(self):
        return "{} | {} | {} | {} | {} | {}".format(self._prenom, self._nom, self._dateNaissance, self._mail, self._telephone, self._adresse)

    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, prenom):
        self._prenom = prenom

    prenom = property(_get_prenom, _set_prenom)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        self._nom = nom

    nom = property(_get_nom, _set_nom)

    def _get_dateNaissance(self):
        return self._dateNaissance

    def _set_dateNaissance(self, dateNaissance):
        self._dateNaissance = dateNaissance

    dateNaissance = property(_get_dateNaissance, _set_dateNaissance)

    def _get_mail(self):
        return self._mail

    def _set_mail(self, mail):
        self._mail = mail

    mail = property(_get_mail, _set_mail)

    def _get_telephone(self):
        return self._telephone

    def _set_telephone(self, telephone):
        self._telephone = telephone

    telephone = property(_get_telephone, _set_telephone)

    def _get_adresse(self):
        return self._adresse

    def _set_adresse(self, adresse):
        self._adresse = adresse

    adresse = property(_get_adresse, _set_adresse)

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