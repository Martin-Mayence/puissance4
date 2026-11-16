import random

import keyboard

from puissance4.grille import Grille
from puissance4.joueur import Joueur


class Partie:
    def __init__(self):
        self.grille = Grille()
        self.joueur1 = Joueur("Joueur 1", "rouge")
        self.joueur2 = Joueur("Joueur 2", "jaune")
        self.joueur_actuel = self.joueur1

    def changer_joueur(self):
        self.joueur_actuel = (
            self.joueur1 if self.joueur_actuel == self.joueur2 else self.joueur2
        )

    def on_key_press(self, key):
        if key.scan_code == 77:
            return "droite"
        elif key.scan_code == 75:
            return "gauche"
        elif key.scan_code == 28:
            return "entrer"
        return None

    def jouer(self):
        colonne = 3

        while True:
            self.grille.afficher(colonne, self.joueur_actuel.couleur)

            key = keyboard.read_event()

            # On ignore les relâchements
            if key.event_type != keyboard.KEY_DOWN:
                continue

            action = self.on_key_press(key)

            if action == "droite":
                colonne = (colonne + 1) % 7

            elif action == "gauche":
                colonne = (colonne - 1) % 7

            elif action == "entrer":
                if not self.grille.ajouter_pion(colonne, self.joueur_actuel.couleur):
                    print("Cette colonne est pleine !")
                    print("Appuyez sur Entrée pour continuer.")

                    keyboard.wait("enter")
                    continue

                if self.grille.verifier_victoire(self.joueur_actuel.couleur):
                    self.grille.afficher()
                    print(
                        f"Félicitations {self.joueur_actuel.nom} "
                        f"({self.joueur_actuel.couleur}) ! Vous avez gagné !"
                    )
                    input("Appuyez sur Entrée pour quitter la partie.")
                    break

                if self.grille.est_pleine():
                    self.grille.afficher()
                    print("Match nul ! La grille est pleine.")
                    break

                self.changer_joueur()
                colonne = 3

            # Attendre le relâchement de la touche
            while (
                keyboard.is_pressed("left")
                or keyboard.is_pressed("right")
                or keyboard.is_pressed("enter")
            ):
                pass

    def jouer_contre_ordinateur(self):
        colonne = 3

        while True:
            self.grille.afficher(colonne, self.joueur_actuel.couleur)

            key = keyboard.read_event()

            # On ignore les relâchements
            if key.event_type != keyboard.KEY_DOWN:
                continue

            action = self.on_key_press(key)

            if action == "droite":
                colonne = (colonne + 1) % 7

            elif action == "gauche":
                colonne = (colonne - 1) % 7

            elif action == "entrer":
                if not self.grille.ajouter_pion(colonne, self.joueur_actuel.couleur):
                    print("Cette colonne est pleine !")
                    print("Appuyez sur Entrée pour continuer.")

                    keyboard.wait("enter")
                    continue

                if self.grille.verifier_victoire(self.joueur_actuel.couleur):
                    self.grille.afficher()
                    print(
                        f"Félicitations {self.joueur_actuel.nom} "
                        f"({self.joueur_actuel.couleur}) ! Vous avez gagné !"
                    )
                    input("Appuyez sur Entrée pour quitter la partie.")
                    break

                if self.grille.est_pleine():
                    self.grille.afficher()
                    print("Match nul ! La grille est pleine.")
                    break

                self.changer_joueur()
                # Attendre le relâchement de la touche
                while (
                    keyboard.is_pressed("left")
                    or keyboard.is_pressed("right")
                    or keyboard.is_pressed("enter")
                ):
                    pass
                # Tour de l'ordinateur
                colonne_ordinateur = random.randint(0, 6)
                while not self.grille.ajouter_pion(
                    colonne_ordinateur, self.joueur_actuel.couleur
                ):
                    colonne_ordinateur = random.randint(0, 6)

                if self.grille.verifier_victoire(self.joueur_actuel.couleur):
                    self.grille.afficher()
                    print("Dommage, l'ordinateur a gagné !")
                    input("Appuyez sur Entrée pour quitter la partie.")
                    break

                if self.grille.est_pleine():
                    self.grille.afficher()
                    print("Match nul ! La grille est pleine.")
                    break

                self.changer_joueur()
