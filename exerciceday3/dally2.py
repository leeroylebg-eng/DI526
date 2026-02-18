import random

string = input("Enter a string of exactly 10 characters: ")

if len(string) < 10:
    print("String not long enough.")
elif len(string) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # 3. Premier et dernier caractère
    print(string[0])
    print(string[-1])

    # 4. Construire caractère par caractère
    for i in range(1, len(string) + 1):
        print(string[:i])

    # 5. Bonus : mélanger la string
    characters = list(string)
    random.shuffle(characters)
    jumbled = "".join(characters)
    print("Jumbled:", jumbled)
