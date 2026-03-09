from game import Game

def get_user_menu_choice():
    print("\n==========================")
    print("  ROCK - PAPER - SCISSORS")
    print("==========================")
    print("1 - Jouer une partie")
    print("2 - Voir les scores")
    print("3 - Quitter")
    while True:
        choice = input("Votre choix : ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        print("Choix invalide. Entrez 1, 2 ou 3.")

def print_results(results):
    print("\n==========================")
    print("       SCORES")
    print("==========================")
    print(f"Victoires : {results['win']}")
    print(f"Defaites  : {results['loss']}")
    print(f"Egalites  : {results['draw']}")
    print("Merci d'avoir joue !")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        elif choice == "3":
            print_results(results)
            break

if __name__ == "__main__":
    main()