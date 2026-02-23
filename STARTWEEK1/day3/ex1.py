# Access the value of key `history`

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics": 70,
            "history": 80
         }
      }
   }
}

history = sample_dict["class"]["student"]["marks"]["history"]

print(history)

sample_dict["class"]["student"]["marks"]["history"] = 100

print(sample_dict["class"]["student"]["marks"]["history"])

sample_dict["class"]["student"]["marks"]["music"] = 93

del sample_dict["class"]["student"]["marks"]["physics"]

print(sample_dict)