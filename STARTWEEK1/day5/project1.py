import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters or letter == " ":
            result += letter + " "
        else:
            result += "_ "
    print(result)

def display_hangman(errors):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ==========""",
    ]
    print(stages[errors])

def play():
    guessed_letters = []
    errors = 0
    max_errors = 6

    print("Bienvenue au Pendu ! 🎮")
    print(f"Le mot a {len(word)} lettres\n")

    while errors < max_errors:
        display_hangman(errors)
        display_word(word, guessed_letters)

        if all(letter in guessed_letters or letter == " " for letter in word):
            print(f"\n🎉 Bravo tu as gagné ! Le mot était : {word}")
            break

        print(f"\nLettres déjà devinées : {', '.join(guessed_letters) if guessed_letters else 'aucune'}")
        print(f"Erreurs restantes : {max_errors - errors}")

        guess = input("\nDevine une lettre : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Entre une seule lettre !")
            continue

        if guess in guessed_letters:
            print("Tu as déjà deviné cette lettre !")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Bonne lettre !")
        else:
            print(f"❌ Mauvaise lettre !")
            errors += 1

    else:
        display_hangman(errors)
        print(f"\n💀 Tu as perdu ! Le mot était : {word}")

play()