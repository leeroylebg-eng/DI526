# Accept a number from the user and print its multiplication table

user_number = int(input("Enter a number: "))
for val in range(11):
    print(f"{user_number} times {val} is {val * user_number}")