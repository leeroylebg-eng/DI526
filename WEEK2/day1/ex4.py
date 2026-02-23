class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        return {letter: [a for a in self.animals if a.startswith(letter)]
                for letter in sorted(set(a[0] for a in self.animals))}

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Example usage
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Lion")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat", "Cougar", "Zebra")
brooklyn_safari.get_groups()