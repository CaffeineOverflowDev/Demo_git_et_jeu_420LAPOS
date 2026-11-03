"""
Fenêtre tkinter du jeu « Clique la cible »
Exemple de démonstration, 420-LAP-OS, Saïd Hamdane. Ne peut pas être remis comme projet.
"""
import tkinter as tk
from logique import Partie, LARGEUR, HAUTEUR


class Fenetre(tk.Tk):
    """La fenêtre : elle affiche la Partie et réagit aux clics. Toute la logique est dans logique.py."""

    def __init__(self):
        super().__init__()
        self.title("Clique la cible (démo 420-LAP-OS)")
        self.resizable(False, False)
        self.partie = None

        self.etiquette = tk.Label(self, text="Clique sur Jouer", font=("Arial", 14))
        self.etiquette.pack(pady=6)
        self.canvas = tk.Canvas(self, width=LARGEUR, height=HAUTEUR, bg="white")
        self.canvas.pack()
        self.bouton = tk.Button(self, text="Jouer", command=self.demarrer)
        self.bouton.pack(pady=6)
        self.canvas.bind("<Button-1>", self.clic)

    def demarrer(self):
        self.partie = Partie()
        self.canvas.delete("all")
        self.bouton.config(state="disabled")
        self.afficher_info()
        self.ajouter_cible()
        self.after(1000, self.tic)

    def ajouter_cible(self):
        if self.partie is None or self.partie.temps_restant <= 0:
            return
        c = self.partie.nouvelle_cible()
        self.canvas.create_oval(c.x - c.rayon, c.y - c.rayon, c.x + c.rayon, c.y + c.rayon,
                                fill=c.couleur, outline="", tags=str(id(c)))
        self.after(900, self.ajouter_cible)

    def clic(self, evenement):
        if self.partie is None or self.partie.temps_restant <= 0:
            return
        touchee = self.partie.clic(evenement.x, evenement.y)
        if touchee is not None:
            self.canvas.delete(str(id(touchee)))
            self.afficher_info()

    def tic(self):
        fini = self.partie.tic()
        self.afficher_info()
        if fini:
            self.partie.terminer()
            self.canvas.delete("all")
            self.canvas.create_text(LARGEUR // 2, HAUTEUR // 2, font=("Arial", 20),
                                    text=f"Fini! Score : {self.partie.score}\nMeilleur : {self.partie.meilleur}")
            self.bouton.config(state="normal")
        else:
            self.after(1000, self.tic)

    def afficher_info(self):
        p = self.partie
        self.etiquette.config(text=f"Score : {p.score}    Temps : {p.temps_restant} s    Meilleur : {p.meilleur}")
