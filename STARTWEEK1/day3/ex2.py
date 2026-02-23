# Delete set of keys from Python Dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]

# del sample_dict["name"]
# del sample_dict["salary"]

for item in keys_to_remove:
    del sample_dict[item]

print(sample_dict)