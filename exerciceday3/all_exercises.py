# --- Exercise 1 ---
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))
print(dictionary)

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

# --- Exercise 3 ---
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara sells clothes for: {', '.join(brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]
print(f"Last competitor: {brand['international_competitors'][-1]}")
print(f"Major colors in the US: {brand['major_color']['US']}")
print(f"Number of keys: {len(brand)}")
print(f"All keys: {list(brand.keys())}")

more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print(f"\nMerged dictionary: {brand}")

# --- Exercise 4 ---
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

char_to_index = {user: i for i, user in enumerate(users)}
print(char_to_index)

index_to_char = {i: user for i, user in enumerate(users)}
print(index_to_char)

sorted_chars = {user: i for i, user in enumerate(sorted(users))}
print(sorted_chars)
