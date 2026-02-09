# Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# This is a comment.

# Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2.
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# Assign a variable called nope to an absence of value.
nope = None

# Use the language’s “and” boolean operator to combine True and False.
result = True and False  # Output: False

# Calculate the length of the string "What's my length?"
length = len("What's my length?")  # Output: 17

# Convert the string "i am shouting" to uppercase.
shouting = "i am shouting".upper()  # Output: "I AM SHOUTING"

# Convert the string "1000" to the number 1000.
number = int("1000")

# Combine the number 4 with the string "real" to produce "4real".
combined = str(4) + "real"  # Output: "4real"

# Record the output of the expression 3 * "cool".
cool_output = 3 * "cool"  # Output: "coolcoolcool"

# Record the output of the expression 1 / 0.
# This will raise an error:
# ZeroDivisionError: division by zero

# Determine the type of [].
list_type = type([])  # Output: <class 'list'>

# Ask the user for their name, and store it in a variable called name.
name = input("What is your name? ")

# Ask the user for a number and check if it’s negative, positive, or zero.
num = float(input("Enter a number: "))

if num < 0:
    print("That number is less than 0!")
elif num > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# Find the index of "l" in "apple".
index_l = "apple".index("l")  # Output: 3

# Check whether "y" is in "xylophone".
check_y = "y" in "xylophone"  # Output: True

# Check whether a string called my_string is all in lowercase.
my_string = "hello"
is_lowercase = my_string.islower()  # Output: True
