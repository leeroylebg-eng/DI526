# --- Exercise 3 ---
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# Changer number_stores à 2
brand["number_stores"] = 2

# Afficher les clients de Zara
print(f"Zara sells clothes for: {', '.join(brand['type_of_clothes'])}")

# Ajouter country_creation
brand["country_creation"] = "Spain"

# Vérifier si international_competitors existe et ajouter Desigual
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Supprimer creation_date
del brand["creation_date"]

# Afficher le dernier concurrent
print(f"Last competitor: {brand['international_competitors'][-1]}")

# Afficher les couleurs principales aux US
print(f"Major colors in the US: {brand['major_color']['US']}")

# Afficher le nombre de clés
print(f"Number of keys: {len(brand)}")

# Afficher toutes les clés
print(f"All keys: {list(brand.keys())}")

# --- Bonus ---
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

brand.update(more_on_zara)
print(f"\nMerged dictionary: {brand}")
