# Clique la cible (démo)

Exemple de démonstration pour le projet de session, 420-LAP-OS Langage de programmation II, automne 2026. Saïd Hamdane.

Ce dépôt montre la structure attendue d'un projet : deux modules, quatre classes, un héritage, une composition, une sauvegarde JSON et des erreurs gérées. Il ne peut pas être remis comme projet, ni en partie ni en entier.

## Comment lancer le jeu

```
python main.py
```

## Règles du jeu

Des cibles apparaissent pendant 20 secondes. Clique dessus pour marquer des points. Les petites cibles rouges valent 3 points, les bleues 1 point. Le meilleur score est sauvegardé dans sauvegarde.json.

## Structure

| Fichier | Contenu |
|---|---|
| logique.py | Cible, CibleRapide (hérite de Cible), Partie (possède des Cibles) |
| fenetre.py | Fenetre (tkinter) : affichage et clics seulement |
| main.py | lance le jeu |
