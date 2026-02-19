nombre = int(input("Entrez un nombre : "))
longueur = int(input("Entrez une longueur : "))

multiples = [nombre * i for i in range(1, longueur + 1)]
print(multiples)