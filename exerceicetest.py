# Exercice 1
list1 = [("name", "Elie"), ("job", "Instructor")]
dict1 = {key: value for key, value in list1}
print("Exercice 1:", dict1)

# Exercice 2
states_abbr = ["CA", "NJ", "RI"]
states_full = ["California", "New Jersey", "Rhode Island"]
dict2 = {abbr: full for abbr, full in zip(states_abbr, states_full)}
print("Exercice 2:", dict2)

# Exercice 3
vowels = ['a', 'e', 'i', 'o', 'u']
dict3 = {vowel: 0 for vowel in vowels}
print("Exercice 3:", dict3)

# Exercice 4
dict4 = {i: chr(64 + i) for i in range(1, 27)}
print("Exercice 4:", dict4)

# Exercice 5 - Super Bonus
text = "awesome sauce"
vowels = ['a', 'e', 'i', 'o', 'u']
dict5 = {vowel: text.count(vowel) for vowel in vowels}
print("Exercice 5:", dict5)
