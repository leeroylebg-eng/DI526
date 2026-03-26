import random

class Game:

    def get_user_item(self):
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            choice = input("Choisissez (rock / paper / scissors) : ").strip().lower()
            if choice in valid_choices:
                return choice
            print("Choix invalide. Veuillez entrer rock, paper ou scissors.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if winning_combinations[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"\nVous avez choisi      : {user_item}")
        print(f"L'ordinateur a choisi : {computer_item}")
        if result == "win":
            print("Vous avez GAGNE !")
        elif result == "loss":
            print("Vous avez PERDU !")
        else:
            print("EGALITE !")
        return result