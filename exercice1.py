my_favorite_numbers = {7, 10, 21}
print (my_favorite_numbers)
my_favorite_numbers.add(99)
my_favorite_numbers.add(42)
print (my_favorite_numbers)
my_favorite_numbers.remove(42)
print (my_favorite_numbers)
friend_fav_numbers = {3, 7, 42}
our_fav_numbers =my_favorite_numbers | friend_fav_numbers
print(our_fav_numbers)
