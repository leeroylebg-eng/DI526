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