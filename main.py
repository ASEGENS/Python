#1 My Python Code Forever

#2 My 
# Python 
# Code 
# every 
# day

#3 Data types
int = 5, 
str = "aze", 
float = 5.2, 
list = ["aze","aze"], 
dict = {"name" : "John", "age" : 36}
bool = True

#4 my42count
my42count = "quarante-deux"

#5
try:
    check42 = isThere42
except NameError:
    check42 = 42


#6
myArray42 = ["q", "u", "a", "r", "a", "n", "t", "e", "-", "d", "e", "u", "x"]

#7
myArray42Len = len(myArray42)

#8
string42 = "".join(myArray42)
print(f'La grande réponse sur la vie, l’univers et le reste ! {string42}')

#9 rand
import random

rand = random.randint(1, 42)
if rand == 42 :
    rand = True
print(rand)

#10
my42Type = type

#11
compute42 = 21*2
print(compute42)
#float(compute42)

#12 42424242
intToString = "42424242"
intToString = intToString.replace("42", "quarante-deux ")

print(intToString)

#13 Créer 2 variables telles que a = 24 et  b = 42. Vous devez à présent transférer “a” vers “b” et “b” vers “a”.
a = 24 
b = 42

c = a
a = b
b = c

print(a)
print(b)
