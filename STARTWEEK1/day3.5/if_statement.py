user_name = input('What is your name? ')

# if user_name == 'sergei':
#     print("Privet")
# elif user_name == "revite":
#     print("Bonjour")
# elif user_name == "alex":
#     print("Hola")
# elif user_name == "avner":
#     print("Shalom")
# elif user_name == "xiao":
#     print("ni hao")
# elif user_name == "aaron":
#     print("ahoy")
# else:
#     print("hello")

greetings = {
    'sergei': "Privet",
    "revite": "Bonjour",
    'alex': 'hola',
    'avner': 'shalom',
    'xiao': 'ni hao',
    'aaron': 'ahoy',
    'other': 'hello'
}

print(greetings[user_name])