# Demander les fruits favoris
fruits_input = input("Entrez vos fruits favoris (séparés par des espaces) : ")

# Stocker dans une liste
fruits_favoris = fruits_input.split()
print("Vos fruits favoris :", fruits_favoris)

# Demander un fruit
fruit_choisi = input("Entrez le nom d'un fruit : ")

# Vérifier si le fruit est dans la liste
if fruit_choisi in fruits_favoris:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
