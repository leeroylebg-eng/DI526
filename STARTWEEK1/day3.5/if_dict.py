user_string = input("enter a word: ")

letters_dict = {}
for index, letter in enumerate(user_string):
    if letter in letters_dict:
        letters_dict[letter].append(index)
    else:
        letters_dict[letter] = [index]

print(letters_dict)