import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

# Création ou ouverture de la base de données
conn = sqlite3.connect("inventaire.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS especes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    lieu TEXT
)
""")

conn.commit()


class Interface(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Champ nom espèce
        self.nom = TextInput(
            hint_text="Nom de l'espèce",
            size_hint=(1, 0.1)
        )

        # Champ lieu
        self.lieu = TextInput(
            hint_text="Lieu d'observation",
            size_hint=(1, 0.1)
        )

        # Bouton enregistrer
        self.bouton = Button(
            text="Enregistrer l'observation",
            size_hint=(1, 0.1)
        )
        self.bouton.bind(on_press=self.enregistrer)

        # Bouton afficher
        self.bouton_afficher = Button(
            text="Afficher les espèces enregistrées",
            size_hint=(1, 0.1)
        )
        self.bouton_afficher.bind(on_press=self.afficher)

        # Résultat
        self.resultat = Label(
            text="",
            size_hint=(1, 0.1)
        )

        # Zone affichage liste
        self.scroll = ScrollView(size_hint=(1, 0.5))
        self.liste = Label(
            text="",
            size_hint_y=None,
            valign="top"
        )
        self.liste.bind(texture_size=self.liste.setter('size'))

        self.scroll.add_widget(self.liste)

        # Ajout widgets
        self.add_widget(self.nom)
        self.add_widget(self.lieu)
        self.add_widget(self.bouton)
        self.add_widget(self.bouton_afficher)
        self.add_widget(self.resultat)
        self.add_widget(self.scroll)

    def enregistrer(self, instance):

        nom = self.nom.text
        lieu = self.lieu.text

        if nom == "" or lieu == "":
            self.resultat.text = "Veuillez remplir tous les champs"
            return

        cursor.execute(
            "INSERT INTO especes (nom, lieu) VALUES (?, ?)",
            (nom, lieu)
        )

        conn.commit()

        self.resultat.text = "Observation enregistrée"

        self.nom.text = ""
        self.lieu.text = ""

    def afficher(self, instance):

        cursor.execute("SELECT nom, lieu FROM especes")

        donnees = cursor.fetchall()

        texte = ""

        for espece in donnees:
            texte += f"Espèce: {espece[0]}  |  Lieu: {espece[1]}\n"

        if texte == "":
            texte = "Aucune observation enregistrée"

        self.liste.text = texte


class BiodiversiteApp(App):

    def build(self):
        return Interface()


BiodiversiteApp().run()
