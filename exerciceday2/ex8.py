# Liste des toppings et prix de base
toppings = []
prix_base = 10
prix_topping = 2.50

# Boucle pour ajouter les toppings
while True:
    topping = input("Entrez un topping (ou 'quit' pour arrêter) : ")
    
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

# Afficher les toppings et le prix total
print("\nVos toppings :")
for t in toppings:
    print(f"- {t}")

prix_total = prix_base + (len(toppings) * prix_topping)
print(f"\nPrix total : ${prix_total}")
