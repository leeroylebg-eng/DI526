words = input("Entre des mots séparés par des virgules : ")

words_list = words.split(",")
words_list.sort()
result = ",".join(words_list)

print(result)
