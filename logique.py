"""
Logique du jeu « Clique la cible »
Exemple de démonstration pour le projet de session, 420-LAP-OS, Saïd Hamdane.
Ce code sert à montrer la structure attendue. Il ne peut pas être remis comme projet.
"""
import json
import random

FICHIER_SAUVEGARDE = "sauvegarde.json"
LARGEUR, HAUTEUR = 500, 400


class Cible:
    """Un cercle qui apparaît à un endroit au hasard et donne des points quand on clique dessus."""

    def __init__(self):
        self.rayon = 25
        self.points = 1
        self.couleur = "steelblue"
        self.x = random.randint(self.rayon, LARGEUR - self.rayon)
        self.y = random.randint(self.rayon, HAUTEUR - self.rayon)

    def contient(self, px, py):
        """Retourne True si le point (px, py) est dans la cible."""
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.rayon ** 2


class CibleRapide(Cible):
    """Une cible plus petite qui vaut plus de points. Hérite de Cible."""

    def __init__(self):
        super().__init__()
        self.rayon = 14
        self.points = 3
        self.couleur = "tomato"

class CibleBonus(Cible):
    """Une cible dorée rare qui vaut 5 points. Hérite de Cible."""

    def __init__(self):
        super().__init__()
        self.points = 5
        self.couleur = "gold"

class Partie:
    """Une partie : un score, un temps et la liste des cibles à l'écran (composition)."""

    DUREE = 20  # secondes

    def __init__(self):
        self.score = 0
        self.temps_restant = Partie.DUREE
        self.cibles = []  # une Partie possède ses Cibles
        self.meilleur = self.charger_meilleur()

    def nouvelle_cible(self):
        tirage = random.random()
        if tirage < 0.1:
            cible = CibleBonus()
        elif tirage < 0.4:
            cible = CibleRapide()
        else:
            cible = Cible()
        self.cibles.append(cible)
        return cible

    def clic(self, px, py):
        """Retourne la cible touchée, ou None. Enlève la cible et ajoute les points."""
        for cible in self.cibles:
            if cible.contient(px, py):
                self.cibles.remove(cible)
                self.score += cible.points
                return cible
        return None

    def tic(self):
        """Une seconde passe. Retourne True si la partie est finie."""
        self.temps_restant -= 1
        return self.temps_restant <= 0

    def terminer(self):
        if self.score > self.meilleur:
            self.meilleur = self.score
            self.sauvegarder_meilleur()

    # --- sauvegarde JSON avec gestion des erreurs ---
    def charger_meilleur(self):
        try:
            with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
                return int(json.load(f)["meilleur"])
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
            return 0  # pas de sauvegarde, ou fichier abîmé : on repart à zéro

    def sauvegarder_meilleur(self):
        try:
            with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
                json.dump({"meilleur": self.meilleur}, f)
        except OSError as e:
            print("Impossible de sauvegarder :", e)
