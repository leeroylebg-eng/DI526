import random

# Exercise 1
def display_message():
    print("I am learning about functions in Python.")

display_message()

# -------------------------

# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# -------------------------

# Exercise 3
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# -------------------------

# Exercise 4
def compare_numbers(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")

compare_numbers(50)

# -------------------------

# Exercise 5
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")

# -------------------------

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

make_great(magician_names)
show_magicians(magician_names)

# -------------------------

# Exercise 7
def get_random_temp():
    return random.uniform(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()




print ("hello world")
print (5 +3)
print (5 * 3)

x= 5

print (x *3)



