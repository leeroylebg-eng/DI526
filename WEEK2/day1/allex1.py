# Exercise 1 - Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create three cat objects
cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 7)
cat3 = Cat("Mittens", 1)

# Step 2: Write a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest

# Step 3: Print the result
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")





# Exercise 2 - Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Step 3: Print details and call methods
print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger!")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger!")
else:
    print("They are the same size!")




    # Exercise 3 - Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # store lyrics as attribute

    def sing_me_a_song(self):
        for line in self.lyrics:  # print each line
            print(line)

# Create a song and call sing_me_a_song()
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

stairway.sing_me_a_song()




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