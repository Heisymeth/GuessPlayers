#import des fichiers

import pandas as pd

df = pd.read_csv("\\Users\\grego\\OneDrive\\Documents\\Python\\GuessPlayer\\data\\Ligue1_Clean.csv")
df2 = pd.read_csv("\\Users\\grego\\OneDrive\\Documents\\Python\\GuessPlayer\\data\\Liste.csv")
# df_clubs = pd.read_csv("club")

#  Application
# Sélectionnez un joueur au hasard
rejouer = True
score = 0

while rejouer:
    joueur = df.sample().iloc[0]
    club = joueur == df2
    # filtre du df_clubs avec le nom du joueur

    # df_clubs filtré avc seulement les clubs du joeuur

    # au début selctione le premier club

    # Affiche les informations sélectionnées
    print("Nationalité:", joueur['Nation'])
    print("Âge:", joueur['Age'])
    print("Poste:", joueur['Pos'])
    print("Premier Club:", df)
    print("Qui est ce joueur ?\n")
    # affichage du 1er club

    nom = input()

    compteur_essais = 1
    essais_max = 3

    while nom.lower() not in joueur['Player'].lower():
        if compteur_essais == essais_max:
            print("Désolé, c'est perdu. La réponse est", joueur['Player'])
            score -= 1  # Décrémente le score en cas d'échec après 3 essais
            break
        
        
        nom = input("Essaie encore : ")

        # afficher un nouveau club
        compteur_essais += 1

    if nom.lower() == joueur['Player'].lower():
        print("Bravo, c'est gagné !")
        score += 1  # Incrémente le score en cas de bonne réponse
    elif nom.strip() == '':
        print("Le joueur était", joueur['Player'])
        score -= 1  # Décrémente le score en cas de réponse vide

    print("Score actuel:", score)

    choix_rejouer = input("Voulez-vous rejouer ? (Oui/Non) ")

    if choix_rejouer.lower() != "oui":
        print("Merci à bientôt !")
        rejouer = False
