class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Version de base
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        # Bonus étape 8 : kwargs
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    # Bonus étape 6
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Bonus étape 7
    def get_short_info(self):
        animal_list = self.get_animal_types()
        animals_str = []
        for animal in animal_list:
            if self.animals[animal] > 1:
                animals_str.append(animal + "s")
            else:
                animals_str.append(animal)
        
        if len(animals_str) > 1:
            joined = ", ".join(animals_str[:-1]) + " and " + animals_str[-1]
        else:
            joined = animals_str[0]
        
        return f"{self.name}'s farm has {joined}"


# Test
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
