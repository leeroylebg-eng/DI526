# Exercise 1
print("Hello world\n" * 4)

# Exercise 2
print((99**3)*8)

# Exercise 3
print(5 < 3)    # False
print(3 == 3)   # True
print(3 == "3") # False
print("Hello" == "hello") # False
# "3" > 3 → Error (can't compare str and int)

# Exercise 4
computer_brand = "Apple"
print("I have a " + computer_brand + " computer.")

# Exercise 5
name = "Leeroy"
age = 20
shoe_size = 42
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

# Exercise 6
a = 10
b = 5
if a > b:
    print("Hello World")

# Exercise 7
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8
user_name = input("What is your name? ")
if user_name == name:
    print("No way, we have the same name!")
else:
    print("Nice to meet you " + user_name + "!")

# Exercise 9
height = int(input("Enter your height in cm: "))
if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride!")