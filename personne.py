
#initalisation de la classe Personne reprenant toutes les infos sur une personne
class Personne():
    #initalisation des informations nécéssaire
    def __init__(self, prenom, nom, dateNaissance = "--/--/----", mail = "mail@mail.com", telephone = "0000 00 00 00", adresse = "---"):
        self._prenom = prenom
        self._nom = nom
        self._dateNaissance = dateNaissance
        self._mail = mail
        self._telephone = telephone
        self.adresse = adresse
#définition du format
    def __repr__(self):
        return "{} | {} | {} | {} | {} | {}".format(self._prenom, self._nom, self._dateNaissance, self._mail, self._telephone, self._adresse)

#Getter et setter du prénom
    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, prenom):
        self._prenom = prenom

    prenom = property(_get_prenom, _set_prenom)

#Getter et setter du nom
    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        self._nom = nom

    nom = property(_get_nom, _set_nom)

#Getter et setter de la date de naissance
    def _get_dateNaissance(self):
        return self._dateNaissance

    def _set_dateNaissance(self, dateNaissance):
        self._dateNaissance = dateNaissance

    dateNaissance = property(_get_dateNaissance, _set_dateNaissance)

#Getter et setter du mail
    def _get_mail(self):
        return self._mail

    def _set_mail(self, mail):
        self._mail = mail

    mail = property(_get_mail, _set_mail)

#Getter et setter du téléphone
    def _get_telephone(self):
        return self._telephone

    def _set_telephone(self, telephone):
        self._telephone = telephone

    telephone = property(_get_telephone, _set_telephone)

#Getter et setter du l'adresse
    def _get_adresse(self):
        return self._adresse

    def _set_adresse(self, adresse):
        self._adresse = adresse

    adresse = property(_get_adresse, _set_adresse)