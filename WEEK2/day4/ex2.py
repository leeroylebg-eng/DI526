import json

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

print(data["company"]["employee"]["payable"]["salary"])

data["company"]["employee"]["birth_date"] = "1995-06-15"

with open("employee.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON saved to employee.json")