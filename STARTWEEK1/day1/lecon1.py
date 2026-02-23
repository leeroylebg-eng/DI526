# print('Hello to Python')
# basis Math
# print(2 + 2) # =4
# print(10 - 3) # =7
# print(20 / 4) 
# print(10 // 3) # Floor division
# print(10 % 3) 
# print( 2 ** 8)

# Order of operation
# print (5 + 3 * 2) # 11
# print((5 + 3) * 2) # 16

greeting = "Hello class"
#  type()
# print(type(greeting))
# print(type('hi'))
# print(type(123))
# print(type("123"))

# String method
# print(greeting.upper())
# print(greeting.lower())
# print(greeting.capitalize())
# print(len(greeting))

# string concatenation - joining string together
# first = "John"
# last ="Due"
# full_name = first + " " + last
# print(full_name)

# print('Ha' * 3)
# print(dir("42"))

text = "Hello, world"
# text = text.replace('world', 'Python')
# print(text)
# print(text.count('w'))

multiline = """
line 1
line 2
"""

# print(multiline)
# print(text[0])
# print(text[-1])

# 
# Numbers
# 
# integers
age = 25
temp = 25
year = 2026
# print(type(year))

# float
price = 19.99
pi = 3.14159
# print(type(pi))

# Booleans - True/False
is_sunny = True
is_raining = False

# print(type(is_sunny))

# print(5 > 3) # True
# print(10 < 5) # Flase
# print( 7 == 7) # True
# print(5 != 3) # True

# Comparison Operators
# == 
# !=
# >
# <
# >=
# <=

# Logical Operators - and / or / not
# print( True and True) # True
# print( True and  False) # False

# print( True or False) # True
# print( False or True) # True
# print( False or False) # False

# print (not True) # False
# print (not False) # True

# 
# x = 42
# y = "42"
# print(x + 1)
# print(y + 1)

# type casting

# str_num = "100"
# print(int(str_num) + 1)

# num = 42
# print(str(num) + ' is the answer')

# print(bool(1)) # True
# print(bool(0)) # False
# print(bool(-1)) # True
# print(bool("hi")) 

name = 'Alice'
age = 25
height = 186.5
is_student = True
max_attemps = 5


# a = 1
# b = 2
# c = 3
a,b,c = 1,2,3
# print(a,b,c)

a, b = b ,a
# print(a,b,c)

# incrementing
counter = 0
counter = counter + 1
counter *= 5

# print("counter=>", counter)

#  String Formating
first = 'John'
last = "Due"

# text1 = "Hello," + " " + first + " " + last
# print(text1)

# text3 = "Hello, {} {}".format(last, first)
# print(text3)

# text4 = f"Hello, {first} {last}"
# print(text4)

# price = 19.99
# quantity = 3
# total = f"Total: ${price * quantity}"
# print(total)

# pi = 3.14159
# print(f"{pi:.3f}")

# name = input("Waht is your name?")
# print(f"Hello, {name}")
# age = int(input("Waht is your age?"))
# print(age + 1)

# THE if STATMENT

age = 15

# if age >= 18:
#     print("you can vote!")
#     print("Finish!")

score = 95

if score >= 90 or score == 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

# print(grade)


# has_license = True

# if not has_license:
#     print('No')
# else:
#     print('Yes')

# hobbies = "coding, gaming, running"

# if "coding" in hobbies: 
#     print('you are in the bootcamp')

# if "a" in "apple":
#     print('yes')

#  nested condition
my_age = 18
has_license = True

# if my_age >= 18:
#     if has_license:
#         print('you can drive')
#     else:
#         print('get a license')
# else:
#     print('too young')

# TERNARY OPERATOR
status = "adult" if my_age >= 18 else "minor"
print(status)