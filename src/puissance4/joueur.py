class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        if couleur not in ["rouge", "jaune"]:
            raise ValueError("La couleur doit être 'rouge' ou 'jaune'.")
        if couleur == "rouge":
            self.couleur = "🔴"
        else:
            self.couleur = "🟡"
