# --- Exercise 1 ---
my_fav_numbers = {3, 7, 12, 42, 99}
print("Start:", my_fav_numbers)

my_fav_numbers.add(15)
my_fav_numbers.add(28)
print("After adding:", my_fav_numbers)

my_fav_numbers.remove(28)
print("After removing:", my_fav_numbers)

friend_fav_numbers = {5, 7, 21, 33, 50}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Combined set:", our_fav_numbers)

# --- Exercise 2 ---
my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple + (6, 7)
print("New tuple:", my_tuple)

# --- Exercise 3 ---
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Start:", basket)

basket.remove("Banana")
print("After removing Banana:", basket)

basket.remove("Blueberries")
print("After removing Blueberries:", basket)

basket.append("Kiwi")
print("After adding Kiwi:", basket)

basket.insert(0, "Apples")
print("After adding Apples at the beginning:", basket)

apple_count = basket.count("Apples")
print("Number of Apples:", apple_count)

basket.clear()
print("Final list:", basket)

# --- Exercise 4 ---
sequence = []
for i in range(3, 11):
    sequence.append(i / 2)
print("Sequence:", sequence)

# --- Exercise 5 ---
print("All numbers from 1 to 20:")
for i in range(1, 21):
    print(i)

print("Numbers at even index:")
for i in range(1, 21, 2):
    print(i)

# --- Exercise 6 ---
while True:
    name = input("Enter your name: ")
    if name.isdigit():
        print("Error: name cannot be a number!")
    elif len(name) < 3:
        print("Error: name must be at least 3 characters!")
    else:
        print("Thank you!", name)
        break

# --- Exercise 7 ---
fruits_input = input("Enter your favorite fruits (separated by spaces): ")
favorite_fruits = fruits_input.split()
print("Your favorite fruits:", favorite_fruits)

chosen_fruit = input("Enter the name of a fruit: ")
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# --- Exercise 8 ---
toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

print("\nYour toppings:")
for t in toppings:
    print(f"- {t}")

total_price = base_price + (len(toppings) * topping_price)
print(f"\nTotal price: ${total_price}")

# --- Exercise 9 ---
ages = []
total_cost = 0

while True:
    age = input("Enter a member's age (or 'quit' to stop): ")
    if age == "quit":
        break
    try:
        ages.append(int(age))
    except ValueError:
        print("Please enter a valid number!")

for age in ages:
    if age < 3:
        total_cost += 0
        print(f"Age {age}: Free")
    elif age <= 12:
        total_cost += 10
        print(f"Age {age}: $10")
    else:
        total_cost += 15
        print(f"Age {age}: $15")

print(f"\nTotal ticket cost: ${total_cost}")
