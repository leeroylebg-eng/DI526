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