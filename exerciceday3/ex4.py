# --- Exercise 4 ---
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Personnage -> index
char_to_index = {user: i for i, user in enumerate(users)}
print(char_to_index)

# 2. Index -> personnage
index_to_char = {i: user for i, user in enumerate(users)}
print(index_to_char)

# 3. Personnages triés alphabétiquement -> index
sorted_chars = {user: i for i, user in enumerate(sorted(users))}
print(sorted_chars)