# # Exercices :
# # Réalisez les exercices suivants (vous n’avez pas le droit d’utiliser 
# les objets ou toute autre possibilité algorithmique de python hormis 
# les variables, conditions et les boucles et les méthodes qui si rattache).

# # Vous devez créer une fonction “myPutStr” cette fonction doit 
# permettre de retourner un String. Si c’est un nombre retournez 
# “et pourquoi pas 42 ?”.
print('1 Ent : ', end = '')
A = input()

def myPutStr(A):
    try:
        val = int(A)
        print('et pourquoi pas 42 ?')
    except ValueError:
        print(A)


# # Créer une fonction “computeSurfaceM2” qui calcule une surface 
# en m² carré.

def computeSurfaceM2(A, B):
    A = float(A)
    B = float(B)
    C = A * B
    return C

print('Entrez la première dimension (X) : ', end='')
A = input()

print('Entrez la deuxième dimension (Y) : ', end='')
B = input()

surface = computeSurfaceM2(A, B)
print(f'La surface fait : {surface} m²')
# # Type de résultat attendu :  “Votre surface et de 200 m2”



# # Créer une fonction “detectMyAgeByNight” capable d’implémenter 
# votre précédent script de la boîte de nuit et de faire entrer 
# dans une boîte de nuit une personne ayant plus de 18 ans et refusant 
# celles qui ont entre 0 et 17. 
# # Vous devez faire en sorte que “Vous ne pouvez pas entrez vous 
# n’êtes pas majeur vous avez {age}” ou “Vous pouvez entrer vous 
# êtes majeur vous avez {age}” s’affiche.
# # Cette fonction devra utiliser “Input” pour être déclenchée.

def detectMyAgeByNight(age):
    age = int(age)
    
    if age >= 42:
        print(f"Vous pouvez entrer et vous êtes le patron de la boite car vous avez {age} ans !")
    elif age >= 18:
        print(f"Vous pouvez entrer, vous êtes majeur, vous avez {age} ans.")
    elif 0 <= age < 18:
        print(f"Vous ne pouvez pas entrer, vous n'êtes pas majeur, vous avez {age} ans.")
    else:
        print("Âge invalide.")

age = input("Veuillez entrer votre âge : ")
detectMyAgeByNight(age)


# # Faite en sorte de créer une fonction “tableGenerator” capable de 
# générer un tableau matriciel avec des “|” et des ”-”  d’après une
# liste python à plusieurs dimensions. 
# # Se tableau devra obligatoirement comprendre des titres pour chaque
#  colonnes même vide et des valeurs même si vide. 
# # Appuyez-vous sur la structure de votre liste pour reproduire votre
#  tableau à l’identique dans votre console.
# # Resultat attendu : 
def tableGenerator(tab1, tab2, tab3):
    header = ["Col1", "Col2", "Col3"]
    data = [header, tab1, tab2, tab3]

    col_width = [max(len(str(item)) for item in column) for column in zip(*data)]

    separator = '+' + '+'.join('-' * (w + 2) for w in col_width) + '+'
    row_pattern = '|' + '|'.join(f' {{:<{w}}} ' for w in col_width) + '|'
    
    print(separator)
    print(row_pattern.format(*header))
    print(separator)
    for row in zip(*data[1:]):
        print(row_pattern.format(*row))
        print(separator)

test1 = [1, 3, 6]
test2 = [2, 4, 6]
test3 = [3, 2, 1]
tableGenerator(test1, test2, test3)




# 1# Vous devez réaliser une horloge numérique en affichant l’heure 
# actuelle en temps réel. Cette horloge devra être actualisée toutes
# les secondes.
# # 	Resultat attendu : 
# # 	23:00   1 seconde après -> 23:01  etc …
import time
import os

def afficher_horloge():
    try:
        while True:
            heure_actuelle = time.strftime('%H:%M:%S')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(heure_actuelle)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Horloge arrêtée.")

afficher_horloge()


# 2# Faite en sorte de créer une fonction “is_palindrome” qui vérifie 
# si une chaîne de caractère est un palindrome elle devra renvoyer
# “True” ou “False”
def is_palindrome(chaine):
    return chaine == chaine[::-1]

print(is_palindrome("radar"))  
print(is_palindrome("bonjour")) 


# 3# Faite en sorte de créer une fonction “validMyInternationalPhone”
#  qui contrôle un numéro de téléphone passé en argument et l’indicatif
# du pays concerné dans un second argument. Vous devrez vérifier et 
# faire en sorte que les numéros Français et des Etats-Unis renvoient
# “True” si le numéro est compatible avec le pays du second argument
# et “False” dans le cas contraire.
import re

def validMyInternationalPhone(numero, indicatif_pays):
    if indicatif_pays == 'FR':
        pattern = r'^(\+33|0)[1-9](\d{2}){4}$'
    elif indicatif_pays == 'US':
        pattern = r'^\+1\d{10}$'
    else:
        return False
    
    return bool(re.match(pattern, numero))

# Exemple d'utilisation
print(validMyInternationalPhone("+33612345678", "FR"))  # True
print(validMyInternationalPhone("0612345678", "FR"))    # True
print(validMyInternationalPhone("+11234567890", "US"))  # True
print(validMyInternationalPhone("1234567890", "US"))    # False


#4 # Vous devez réaliser une fonction capable de calculer la suite 
# de fibonacci à partir d’une taille limite fix en argument pour limiter 
# la taille de la suite. Vous deverez réaliser obligatoirement 
# une recursive.
# # Par exemple si je donne 5 en argument  la resultat sera le suivant : 
# # [1, 1, 2, 3, 5]       
def fibonacci(n, a=1, b=1, result=None):
    if result is None:
        result = [a, b]
    if len(result) >= n:
        return result[:n]
    result.append(result[-1] + result[-2])
    return fibonacci(n, result[-2], result[-1], result)

print(fibonacci(5))  # [1, 1, 2, 3, 5]
