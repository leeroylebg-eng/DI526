# Ensemble de mes nombres favoris
my_fav_numbers = {3, 7, 12, 42, 99}
print("Départ :", my_fav_numbers)

# Ajouter deux nombres
my_fav_numbers.add(15)
my_fav_numbers.add(28)
print("Après ajout :", my_fav_numbers)

# Supprimer le dernier ajouté
my_fav_numbers.remove(28)
print("Après suppression :", my_fav_numbers)

# Ensemble de l'ami
friend_fav_numbers = {5, 7, 21, 33, 50}

# Union des deux ensembles
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Ensemble commun :", our_fav_numbers)