# GuessPlayers
Petite application où il faut deviner le nom du joueur de ligue 1 sur la base des critère suivants:
  - Age
  - Nationalité
  - Poste

Les fichiers sont répertoriés de la manière suivante:
  - PSG = liste des joueurs du PSG qui a été nettoyée
  - PSG_Clean = export du PSG nettoyé
  - Ligue1 = liste des joueurs de ligue 1 qui a été nettoyée
  - Ligue1_Clean = export de Ligue1 nettoyé
  - Game = version du jeu actuelle en python, le fichier Ligue1_Clean.csv devra se trouver dans le même dossier, le module 'pandas' devra être installé. 
  - Scraping = BS et Selenium pour récupérer les clubs de chaques joueurs

Pour run le jeu:
  - ouvrir le terminal
  - taper "python game.py" (s'assurer que le module pandas soit installé)

Travail en cours: Trouver le le nom des clubs pour chaque joueur. Les faire apparaitre du plus ancien au plus récent.
Pour la suite: s'intéresser à toutes les ligues de football, puis d'autres sports.
