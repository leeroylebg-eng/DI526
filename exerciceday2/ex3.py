# La liste de départ
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Départ :", basket)

# Supprimer "Banana"
basket.remove("Banana")
print("Après suppression de Banana :", basket)

# Supprimer "Blueberries"
basket.remove("Blueberries")
print("Après suppression de Blueberries :", basket)

# Ajouter "Kiwi" à la fin
basket.append("Kiwi")
print("Après ajout de Kiwi :", basket)

# Ajouter "Apples" au début
basket.insert(0, "Apples")
print("Après ajout de Apples au début :", basket)

# Compter combien de fois "Apples" apparaît
nombre_apples = basket.count("Apples")
print("Nombre de Apples :", nombre_apples)

# Vider la liste
basket.clear()
print("Liste finale :", basket)