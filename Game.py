#import des fichiers

import pandas as pd

df = pd.read_csv('ligue_1_clean.csv')
df.head()

#  Application
# Sélectionnez un joueur au hasard
joueur = df.sample().iloc[0]

# Affiche les informations sélectionnées
print("Nationalité:", joueur['Nation'])
print("Âge:", joueur['Age'])
print("Poste:", joueur['Pos'])
print("Qui est ce joueur ?\n")

nom = input()

compteur_essais = 1

while nom.lower() not in joueur['Player'].lower():
    if compteur_essais == 3:
        print("Désolé, vous avez épuisé vos essais. La réponse est", joueur['Player'])
        break

    nom = input("Essaie encore : ")
    compteur_essais += 1

if nom.lower() in joueur['Player'].lower():
    print("Bravo, c'est gagné !")