from puissance4.partie import Partie


def main():
    print("=== PUISSANCE 4 ===")
    print("1. Nouvelle partie")
    print("2. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Nouvelle partie !")
        print("1. Partie contre un autre joueur")
        print("2. Partie contre l'ordinateur ")
        sous_choix = input("Votre choix : ")
        if sous_choix == "1":
            partie = Partie()
            partie.jouer()
        else:
            partie = Partie()
            partie.jouer_contre_ordinateur()

    elif choix == "2":
        print("Au revoir !")

    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()
