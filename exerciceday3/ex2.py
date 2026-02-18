# --- Exercise 2 ---
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        print(f"{name}: Free")
    elif age <= 12:
        total_cost += 10
        print(f"{name}: $10")
    else:
        total_cost += 15
        print(f"{name}: $15")

print(f"\nTotal cost: ${total_cost}")

# --- Bonus ---
family_bonus = {}
while True:
    name = input("Enter a family member's name (or 'quit' to stop): ")
    if name == "quit":
        break
    age = int(input(f"Enter {name}'s age: "))
    family_bonus[name] = age

total_bonus = 0
for name, age in family_bonus.items():
    if age < 3:
        print(f"{name}: Free")
    elif age <= 12:
        total_bonus += 10
        print(f"{name}: $10")
    else:
        total_bonus += 15
        print(f"{name}: $15")

print(f"\nTotal cost: ${total_bonus}")
