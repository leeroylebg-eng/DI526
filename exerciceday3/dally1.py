word = input("Enter a word: ")
letter_index = {}
for index, char in enumerate(word):
    if char in letter_index:
        letter_index[char].append(index)
    else:
        letter_index[char] = [index]
print(letter_index)




items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

wallet = int(wallet.replace("$", "").replace(",", ""))
basket = []

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))
    if price <= wallet:
        basket.append(item)
        wallet -= price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))


