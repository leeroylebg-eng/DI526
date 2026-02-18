while True:
    name = input("Entrez votre nom : ")
    
    # Vérifier si le nom est valide
    if name.isdigit():
        print("Erreur : le nom ne peut pas être un nombre !")
    elif len(name) < 3:
        print("Erreur : le nom doit contenir au moins 3 lettres !")
    else:
        print("Merci !", name)
        break
