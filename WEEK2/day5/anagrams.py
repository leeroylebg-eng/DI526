from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker("sowpods.txt")

    print("=" * 40)
    print("   BIENVENUE DANS L'ANAGRAM CHECKER !")
    print("=" * 40)

    while True:
        print("\nMENU :")
        print("  1 - Entrer un mot")
        print("  2 - Quitter")
        choice = input("\nVotre choix : ").strip()

        if choice == "2":
            print("\nAu revoir !")
            break

        elif choice == "1":
            user_input = input("Entrez un mot : ").strip()

            # Validation : un seul mot
            if len(user_input.split()) > 1:
                print("❌ Erreur : veuillez entrer un seul mot.")
                continue

            # Validation : uniquement des lettres
            if not user_input.isalpha():
                print("❌ Erreur : le mot ne doit contenir que des lettres (pas de chiffres ni de caractères spéciaux).")
                continue

            word = user_input.lower()

            # Vérification validité
            is_valid = checker.is_valid_word(word)

            # Recherche des anagrammes
            anagrams = checker.get_anagrams(word)

            # Affichage
            print("\n" + "-" * 40)
            print(f'VOTRE MOT : "{word.upper()}"')

            if is_valid:
                print("✅ C'est un mot anglais valide.")
            else:
                print("⚠️  Ce mot n'est pas dans la liste de mots anglais.")

            if anagrams:
                print(f"Anagrammes trouvés : {', '.join(sorted(anagrams))}.")
            else:
                print("Aucun anagramme trouvé.")
            print("-" * 40)

        else:
            print("❌ Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()
