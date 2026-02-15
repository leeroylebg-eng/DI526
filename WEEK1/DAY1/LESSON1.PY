










print(2 + 2)        # Addition
print(10 - 3)       # Subtraction
print(20 / 4)       # Division
print(10 // 3)      # Floor division
print(10 % 3)       # Modulo (remainder)
print(2 ** 8)       # Power

# Order of operations

print(5 + 3 * 2) # 11
print((5 + 3) * 2) # 16

greeting = "hello class"
# type()
print(type(greeting))
print(type('hi'))
print(type(123))
print(type("123"))

#String method
print(greeting.upper())
print(greeting.lower())
print(greeting.capitalize())

#string concatenation - joining string together
#first = "john"
#last = "due"
#full name = first + " " + last
#print(full_name)

print("ha" * 3)
print(dir(42))

#text = "hello world"
#print(text.replace('world' , 'python'))
#print(text)
#print(text.count('l'))

multiline = """
line 1 
line 2 
"""

#print(multiline)
print(text[0])
# -------------------------
# Numbers
# -------------------------

# integers (nombres entiers)
age = 25
temp = 25
year = 2026

print(type(year))   # affiche le type de year

# float (nombres décimaux)
price = 19.99
pi = 3.14159

print(type(price))  # affiche le type de price

# BOOLEANS - True/False
is_sunny = True
is_raining = False

print(type(is_sunny))

print(5 > 3) #true
print(10 < 5 ) #false 
print(7==7) # true
print(5 != 5) # false


# ==
# !=
# >
# <
# >=
# <+

#logical operators - and / or / not


print(True and True)     # True
print(True and False)    # False

print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

print(not True)          # False
print(not False)         # True

#
x = 42
y = "42"
print( x + 1)
print (y + 1)


# type casting 

str_num = "100"
print (int(str_num) + 1)

num = 42
print(str(num)) + ' is tr answer'

print(bool(1)) #true 
print(bool(0)) #false 
print(bool(-1)) #true
print(bool("hi"))

name = "alice"
age  = 30
height = 186.5
is_student = True 
max_attemps = 5

# a = 1
# b = 2
# c = 3
a,b,c = 1,2,3
print (a,b,c)

a ,b = b ,a 
#print (a,b,c)

#incrementing
counter = 0
counter =counter + 1
# -------------------------
# Counter example
# -------------------------

counter = 0

print("Counter:", counter)

# Incrementing (augmenter de 1)
counter = counter + 1
print("Counter:", counter)

counter = counter + 1
print("Counter:", counter)

# string formatting 

first = "John"
last = "Due"

# 1️⃣ Méthode avec concaténation (+)
text1 = "Hello, " + first + " " + last
print(text1)

# 2️⃣ Méthode avec .format()
text3 = "Hello, {} {}".format(last, first)
print(text3)

# 3️⃣ Méthode moderne (f-string) ✅
text4 = f"Hello, {first} {last}"
print(text4)

price = 19.99
quantity = 3

total = f"Total: ${price * quantity}"
print(total)

# -------------------------
# Format decimal
# -------------------------

pi = 3.14159
print(f"{pi:.2f}")

name = imput("what is your name ?")
print(f"hello {name}")
age =int(input("what is your age?"))
print(age + 1)

#the if statment

age = 15

if age >= 18:
    print("You can vote.")
    print("Finish!")

# -------------------------
# Grade system
# -------------------------

score = 95

if score >= 90 or score == 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(grade)


has_licenses_license = True

if not has_license:
    print("no")
else:
    print("yes")


hobbies = ['reading', 'coding', 'hiking']

if 'coding' in hobbies:
    print("You are in the bootcamp!")

if "a" in "apple":
    print("yes")


# -------------------------
# Nested condition
# -------------------------

my_age = 18
has_license = True

if my_age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("Get a license.")
else:
    print("Too young.")


    #ternary opertor

    status = "adult" if age >= 18 else "minor"
    print(status)