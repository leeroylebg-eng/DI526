def say_hello(*args):
    print("The greetins are: ", args)

say_hello("ahoy", "hello", "hi", "cheese")

def say_hello(**kwargs):
    print("The greetings are: ", kwargs)

say_hello(greeting1="ahoy", greeting2="hello", greeting3="hi", greeting4="cheese")

def make_sandwich(type, *args, **kwargs):
    print(f"making a {type} sandwich")
    if args:
        for arg in args:
            print(f"adding {arg}")
    if kwargs:
        print("additional parameters are: ", kwargs)

sandwich_type = input("what type of sandwich? ")

make_sandwich(sandwich_type, "lettuce", "tomato", breadtype="brown pita")

# ingredients_list = []

# sandwich_type = "cheese"

# while True:
#     ing = input("What to add to sandwich? ")
#     if ing == "q":
#         break
#     else:
#         ingredients_list.append(ing)

# def create_sandwich(type, ingredients):
#     print(f"making a {type} sandwich")
#     for ingredient in ingredients:
#         print(f"adding {ingredient}")

# create_sandwich(sandwich_type, ingredients_list)

