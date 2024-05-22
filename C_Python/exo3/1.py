# Vous devez réaliser les tables de multiplications de “1, 2, 3, 5” et “8”.
# >> Création d’une liste par table avec l’ensemble des résultats des multiplications
mylist1 = [0,1,2,3,4,5,6,7,8,9,10]
mylist2 = [0,2,4,6,8,10,12,14,16,18,20]
mylist3 = [0,3,6,9,12,15,18,21,24,27,30]
mylist5 = [0,5,10,15,20,25,30,35,40,45,50]
mylist8 = [0,8,16,24,32,40,48,56,64,72,80]

# Vous devez créer une liste de 1 à 10 et multiplier les résultats de la table de “5” 
# (vous n'avez le droit d’utiliser que les String). Utilisez une boucle For.
# >> Création de listes de strings indiquant : 
# 5 x 1 = 5
# 5 x 2 = 10
# …
list_10 = [0,1,2,3,4,5,6,7,8,9,10]
for x in list_10:
    print(5 * x)


# Même exercice que le 2 avec une boucle “while” avec “true” comme valeur de condition.
# Faites une incrémentation dans un print() avec la table de multiplication par “5”. 
i = 0
while i < len(list_10):
  print(5 * list_10[i])
  i = i + 1

# Vous devez créer une variable avec l’objet suivant {“a”: 42, “b”: 42, “c”: 42, “d”: 42}. 
# Vous devrez parcourir chaque key et faire la multiplication de la valeur précédente par
#  la nouvelle (accumulateur) sauf pour la lettre ‘d’ ou vous devrez faire une soustraction de 42. Le calcul retournera “74046” 


# Écrivez un programme qui génère et affiche le motif suivant en utilisant des boucles imbriquées : * **  *** **** *****


# (Trie à bulle) Vous devez réaliser un algo qui vous permettra de trier un tableau “nbr” en ordre croissant 
# par exemple si j’ai “[5, 4, 3, 2, 1]” le résultat sera “[1, 2, 3, 4, 5]”. Vous n’avez pas le droit d’utiliser de fonction.


# Faire une liste partant de 1980 à nos jours en prenant en compte l’année actuelle actualisé.


# Faite en sorte d’afficher la structure visuelle suivante (cf ex5) en un script avec une boucle for :
i = 0
valeur = '1'
while  i < 10 : 
    y = 0   
    while y < i :
        print(valeur, end = '')
        y = y + 1
    print()
    i = i + 1
 
# Si vous avez réussi le précédent exercice, vous pouvez essayer d’afficher cette structure :


i = 0
max = 10
A = '['
B = ']'
while  i < max : 
    y = 0
    while y > i - max:
        print(' ', end = '')
        y = y - 1
        
    y = 0
    while y < i :
        print(A, end = '')
        y = y + 1
    print('   ', end = '')
    y = 0
    while y < i :
        print(B, end = '')
        y = y + 1

    print()
    i = i + 1

