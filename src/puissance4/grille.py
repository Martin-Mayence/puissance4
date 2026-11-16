import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


class Grille:
    def __init__(self):
        self.grille = [["  " for _ in range(7)] for _ in range(6)]

    def afficher(self, colonne=None, couleur=None):
        clear_console()

        # Affichage du pion en déplacement
        if colonne is not None and couleur is not None:
            affichage = ["  " for _ in range(7)]
            affichage[colonne] = couleur
            print("|" + "|".join(affichage) + "|")
        else:
            print(" 1  2  3  4  5  6  7")

        for ligne in self.grille:
            print("|" + "|".join(ligne) + "|")

        print("-------------------------------")

    def ajouter_pion(self, colonne, couleur):
        for ligne in reversed(self.grille):
            if ligne[colonne] not in ("🔴", "🟡"):
                ligne[colonne] = couleur
                return True
        return False

    def est_pleine(self):
        return all(
            cellule == "🔴" or cellule == "🟡"
            for ligne in self.grille
            for cellule in ligne
        )

    def verifier_victoire(self, couleur):
        # Vérification des lignes
        for ligne in self.grille:
            if self._verifier_sequence(ligne, couleur):
                return True

        # Vérification des colonnes
        for col in range(7):
            colonne = [self.grille[ligne][col] for ligne in range(6)]
            if self._verifier_sequence(colonne, couleur):
                return True

        # Vérification des diagonales
        for ligne in range(6):
            for col in range(7):
                if self._verifier_diagonale(ligne, col, couleur):
                    return True

        return False

    def _verifier_sequence(self, sequence, couleur):
        count = 0
        for cellule in sequence:
            if cellule == couleur:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def _verifier_diagonale(self, ligne, col, couleur):
        # Vérification diagonale descendante
        if (
            ligne <= 2
            and col <= 3
            and all(self.grille[ligne + i][col + i] == couleur for i in range(4))
        ):
            return True

        # Vérification diagonale montante
        return (
            ligne >= 3
            and col <= 3
            and all(self.grille[ligne - i][col + i] == couleur for i in range(4))
        )
