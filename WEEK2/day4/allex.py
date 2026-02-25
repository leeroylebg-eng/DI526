import json
import random

# ==================== Exercise 1: Random Sentence Generator ====================

def get_words_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        words = content.split()
    return words

def get_random_sentence(length):
    words = get_words_from_file("/Users/leeroybenaich/DI526/WEEK2/day4/words.txt")
    sentence = " ".join(random.choice(words) for _ in range(length))
    return sentence.lower()

def main():
    print("This program generates a random sentence from a word list.")
    user_input = input("Enter the desired sentence length (2-20): ")
    
    try:
        length = int(user_input)
    except ValueError:
        print("Error: please enter a valid integer.")
        return
    
    if length < 2 or length > 20:
        print("Error: length must be between 2 and 20.")
        return
    
    print(get_random_sentence(length))

main()

# ==================== Exercise 2: Working With JSON ====================

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(f"Salary: {data['company']['employee']['payable']['salary']}")

data["company"]["employee"]["birth_date"] = "1990-05-15"

with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)

print("Modified data saved to employee.json")

with open("employee.json", "r") as f:
    verified = json.load(f)
    print(f"Verified - birth_date: {verified['company']['employee']['birth_date']}")