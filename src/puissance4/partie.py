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

    def jouer(self):
        while True:
            self.grille.afficher()
            try:
                colonne = (
                    int(
                        input(
                            f"{self.joueur_actuel.nom} ({self.joueur_actuel.couleur}), choisissez une colonne (1-7): "
                        )
                    )
                    - 1
                )
                if colonne < 0 or colonne > 6:
                    print(
                        "Colonne invalide. Veuillez choisir une colonne entre 1 et 7."
                    )
                    continue
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entre 1 et 7.")
                continue

            if not self.grille.ajouter_pion(colonne, self.joueur_actuel.couleur):
                print("Cette colonne est pleine. Veuillez en choisir une autre.")
                continue

            if self.grille.verifier_victoire(self.joueur_actuel.couleur):
                self.grille.afficher()
                print(
                    f"Félicitations {self.joueur_actuel.nom} ({self.joueur_actuel.couleur}) ! Vous avez gagné !"
                )
                break

            if self.grille.est_pleine():
                self.grille.afficher()
                print("Match nul ! La grille est pleine.")
                break

            self.changer_joueur()

    def jouer_contre_ordinateur(self):
        import random

        while True:
            self.grille.afficher()
            if self.joueur_actuel == self.joueur1:
                try:
                    colonne = (
                        int(
                            input(
                                f"{self.joueur_actuel.nom} ({self.joueur_actuel.couleur}), choisissez une colonne (1-7): "
                            )
                        )
                        - 1
                    )
                    if colonne < 0 or colonne > 6:
                        print(
                            "Colonne invalide. Veuillez choisir une colonne entre 1 et 7."
                        )
                        continue
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entre 1 et 7.")
                    continue
            else:
                colonne = random.randint(0, 6)
                print(f"L'ordinateur choisit la colonne {colonne + 1}.")

            if not self.grille.ajouter_pion(colonne, self.joueur_actuel.couleur):
                print("Cette colonne est pleine. Veuillez en choisir une autre.")
                continue

            if self.grille.verifier_victoire(self.joueur_actuel.couleur):
                self.grille.afficher()
                print(
                    f"Félicitations {self.joueur_actuel.nom} ({self.joueur_actuel.couleur}) ! Vous avez gagné !"
                )
                break

            if self.grille.est_pleine():
                self.grille.afficher()
                print("Match nul ! La grille est pleine.")
                break

            self.changer_joueur()
