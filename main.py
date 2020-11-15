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

listing = []

def ajout_listing(listing, membre):
    listing.append(membre)

def afficher_listing(listing):
    print("PRENOM          | NOM             | DATE       | MAIL                           | TELEPHONE     | ADRESSE ")
    for membre in listing:
        prenom = format(membre.prenom, 15)
        nom = format(membre.nom, 15)
        dateNaissance = format(membre.dateNaissance, 10)
        mail = format(membre.mail, 30)
        telephone = format(membre.telephone, 13)
        adresse = membre.adresse
        print("{} | {} | {} | {} | {} | {}".format(prenom, nom, dateNaissance, mail, telephone, adresse))
    input()
    menu()
            
def format(mot, n):
    while len(mot) < n:
        mot = mot + " "
    return mot

def inscription():
   
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    dateNaissance = input("Date de naissance : ")
    mail = input("Adresse e-mail : ")
    telephone = input("Numéro de téléphone : ")
    adresse = input("Adresse : ")

    #insertion information dans tableau depuis inputs
    fichier = open("Tableau.txt", "a") 
    fichier.write(str( Personne(prenom, nom, dateNaissance, mail, telephone, adresse)))
    fichier.write("\n")
    fichier.close()
    

    menu()

def menu():
    print("1. Afficher le listing")
    print("2. Inscrire un nouveau membre")
    print("3. Quitter")

    choix = 0

    while int(choix) < 1 or int(choix) > 3:
        choix = int(input())

    if choix == 1:
        fichier = open("Tableau.txt", "r")
        print (fichier.read())
        fichier.close()
        input()
        menu()
    elif choix == 2:
        inscription()

    elif choix == 3:
        fichier = open("Tableau.txt", "a")

        for membre in listing :
          fichier.write(str (membre))
          fichier.write("\n")
        fichier.close()
        return 0

menu()