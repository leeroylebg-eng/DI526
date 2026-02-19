# Exercise 7
import random

def get_random_temp():
    return random.uniform(-10, 40)  # Bonus floating point

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