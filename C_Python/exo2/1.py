# Créer un script capable de faire entrer dans une boîte de nuit une personne ayant plus   
# de 18 ans et refusant celles qui ont entre 0 et 17 ans. Utilisez “print();” pour afficher votre message. 
# Vous devez faire une concaténation avec la phrase “Vous ne pouvez pas entrer 
# vous n’êtes pas majeur vous avez {age}” ou “Vous pouvez entrer vous êtes majeur vous avez {age}”. 
# Attention si l’âge est compris entre 42 et plus vous devenez le patron de la boite !

import random

Random = random.randint(1, 100)
match Random:
        case _ if Random >= 42:
            print(f"Vous pouvez entrer et vous êtes le patron de la boite car vous avez {Random} ans !")
        case _ if Random >= 18:
            print(f"Vous pouvez entrer, vous êtes majeur, vous avez {Random} ans.")
        case _ if 0 <= Random < 18:
            print(f"Vous ne pouvez pas entrer, vous n'êtes pas majeur, vous avez {Random} ans.")
        case _:
            print("Âge invalide.")

# Créer un algorithme qui retourne : “Cool” quand la valeur est comprise entre 0 et 10. 
# “Tepid” quand la valeur est comprise entre 11 et 20. “Warm” quand la valeur est comprise entre 21 et 30.
# Cette condition devra utiliser une variable “rand” avec un nombre aléatoire compris entre 0 et 30.

Random = random.randint(1, 30)
match Random:
        case _ if 21 <=Random <= 30:
            print(f"Warm {Random}")
        case _ if 11 <=Random <= 20:
            print(f"Tepid {Random}")
        case _ if 0 <= Random <= 10:
            print(f"Cool {Random}")
        case _:
            print(f"invalide {Random}")

# Utilisez le “match” pour déterminer le jour de la semaine avec “datetime”. Si nous sommes lundi vous devrez 
# reconnaître que nous sommes lundi et afficher “nous sommes {jour}”. Faites cela pour tous les autres jours de la semaine.

import datetime

jour = datetime.datetime.now().weekday()
match jour:
     case 0:
         print("Lundi")
     case 1:
         print("Mardi")
     case 2:
         print("Mercredi")
     case 3:
         print("Jeudi")
     case 4:
         print("Vendredi")
     case 5:
         print("Samedi")
     case 6:
         print("Dimanche")
     case _:
         print("Pas un jour de la semaine")


# Afin d’utiliser les conditions imbriquées, créer une histoire avec 3 niveaux minimum avec au minimum 3 fins différentes 
# vous devez faire des “if” imbriqués. Vous devez utiliser la fonction “input()”. Aucune autre fonction n’est autorisée. 
# Bien entendu une des fins doit obligatoirement finir par “La grande réponse sur la vie, l’univers et le reste !”.  Utilisez “print()”. 

print("Bienvenue dans l'aventure!")
path_ = input("Vous êtes au départ, merci de choisir une route: A, B, C ")

if path_ == 'A':
    path_1 = input("Merci de choisir une route: A, B, C ")
    if path_1 == 'A':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à à 42")
            
    elif path_1 == 'B':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

    elif path_1 == 'C':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

elif path_ == 'B':
    path_1 = input("Merci de choisir une route: A, B, C ")
    if path_1 == 'A':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")
            
    elif path_1 == 'B':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

    elif path_1 == 'C':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

elif path_ == 'C':
    path_1 = input("Merci de choisir une route: A, B, C ")
    if path_1 == 'A':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

    elif path_1 == 'B':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")

    elif path_1 == 'C':
        path_11 = input("Merci de choisir une route: A, B, C ")
        if path_11 == 'A':
            print("Fin du chemin C1A - Vous découvrez un trésor!")
        elif path_11 == 'B':
            print("Fin du chemin C1B - Un piège se déclenche, fin de l'aventure!")
        elif path_11 == 'C':
            print("Fin du chemin C1C - Vous trouvez une carte menant à une île mystérieuse.")
else:
    print("Choix invalide, veuillez redémarrer le jeu.")


