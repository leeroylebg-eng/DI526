import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    found = False

    for i in range(max_attempts):
        guess = int(input("Enter your guess between 1 and 100: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("Congratulations!")
            found = True
            break

    if not found:
        print("You lost! The number was", random_number)

number_guessing_game()

