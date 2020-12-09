from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from fonctions import recup_listing

class Info(Label):
    pass

class Inscription(BoxLayout):
    pass

class Interface(BoxLayout):
    def display_listing(self):
        layout = self.ids['content']
        layout.clear_widgets()
        for membre in recup_listing():
            line = BoxLayout()
            prenom = Info(text=membre.prenom)
            nom = Info(text=membre.nom)
            dateNaissance = Info(text=membre.dateNaissance)
            mail = Info(text=membre.mail)
            telephone = Info(text=membre.telephone)
            adresse = Info(text=membre.adresse)
            line.add_widget(prenom)
            line.add_widget(nom)
            line.add_widget(dateNaissance)
            line.add_widget(mail)
            line.add_widget(telephone)
            line.add_widget(adresse)
            layout.add_widget(line)

    def display_inscription(self):
        layout = self.ids['content']
        layout.clear_widgets()
        layout.add_widget(Inscription())

class InterfaceApp(App):
    def build(self):
        return Interface()

InterfaceApp().run()