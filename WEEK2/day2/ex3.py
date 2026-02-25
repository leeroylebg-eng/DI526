import random
from exercise2 import Dog  # adapte le nom du fichier

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ", ".join([dog.name for dog in args] + [self.name])
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

if __name__ == "__main__":
    my_dog = PetDog("Fido", 2, 10)
    buddy = PetDog("Buddy", 3, 12)
    my_dog.train()
    my_dog.play(buddy)
    my_dog.do_a_trick()