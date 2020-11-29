class Membre():
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

class Chef(Membre):

    def __init__(self, prenom, nom, dateNaissance, mail, telephone, adresse, dateDebut):
        Membre.__init__(self, prenom, nom, dateNaissance, mail, telephone, adresse)
        self.dateDebut = dateDebut

    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)

class Anime(Membre):
    def __init__(self, prenom, nom, dateNaissance, mail, telephone, adresse, badges):
        Membre.__init__(self, prenom, nom, dateNaissance, mail, telephone, adresse)
        self.badges = badges

    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)

class ChefUnite(Membre):
    def __init__(self, prenom, nom, dateNaissance, mail, telephone, adresse, dateElection):
        Membre.__init__(self, prenom, nom, dateNaissance, mail, telephone, adresse)
        self.dateElection = dateElection

    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)

class Unite():
    def __init__(self, nom, sigle, chefsUnite):
        self.nom = nom
        self.sigle = sigle
        self.chefsUnite = chefsUnite

    def __repr__(self):
        return self.nom

class Section():
    def __init__(self, nom, chefs, animes):
        self.nom = nom
        self.chefs = chefs
        self.animes = animes

    def __repr__(self):
        return self.nom