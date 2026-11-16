from puissance4.partie import Partie


def main():
    print("=== PUISSANCE 4 ===")
    print("1. Nouvelle partie")
    print("2. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        partie = Partie()
        partie.jouer()

    elif choix == "2":
        print("Au revoir !")

    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()
