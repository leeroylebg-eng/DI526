# Liste des ages de la famille
ages = []
prix_total = 0

# Demander les ages
while True:
    age = input("Entrez l'age d'un membre (ou 'quit' pour arrêter) : ")
    
    if age == "quit":
        break
    else:
        ages.append(int(age))

# Calculer le prix total
for age in ages:
    if age < 3:
        prix_total += 0
        print(f"Age {age} : Gratuit")
    elif age <= 12:
        prix_total += 10
        print(f"Age {age} : $10")
    else:
        prix_total += 15
        print(f"Age {age} : $15")

print(f"\nPrix total des billets : ${prix_total}")
