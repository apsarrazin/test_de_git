# coding utf-8
""" Modif faite pour tester git """
import random

random_attack = True
random_damage = 0
nom = blaba
titan1_name = ''
titan2_name = ''

titan1_hp = 250
titan2_hp = 250

print ("\nPREPAREZ VOUS LE COMBAT VAT COMMENCER\n")





titan1_name = input("Comment te nommes tu, premier combattant ? ")
titan2_name = input("Et toi quel est ton nom ? ")

print("les regles arrivent ")




input()
print(f"C'est a toi de commencer, {titan1_name} \n")
# 1ère attaque
random_attack = bool(random_attack)

if      random_attack == True:
        random_damage = random.randint(0,100)
        print(f"{titan1_name} as infligé {random_damage} a {titan2_name} " )
else:
    print("Tu n as fait aucun degat")

titan2_hp -= random_damage
print(f"{titan2_name} il te reste {titan2_hp } point de vie. ")
#2 émé attaque

input()
print(f"A ton tour de jouer {titan2_name}")

input()
random_attack = bool(random_attack)

if      random_attack == True:
        random_damage = random.randint(0,100)
        print(f"{titan2_name} as infligé {random_damage} a {titan1_name} " )
else:
    print("Tu n as fait aucun degat")

titan1_hp -= random_damage
print(f"{titan1_name} il te reste {titan1_hp } point de vie. ")

#3éme attaque

input()
print(f"A ton tour de jouer {titan1_name}")
input()

random_attack = bool(random_attack)

if      random_attack == True:
        random_damage = random.randint(0,100)
        print(f"{titan1_name} as infligé {random_damage} a {titan2_name} " )
else:
    print("Tu n as fait aucun degat")

titan2_hp -= random_damage
print(f"{titan2_name} il te reste {titan2_hp } point de vie. ")


#4éme attaque

input()
print(f"A ton tour de jouer {titan2_name}")

input()
random_attack = bool(random_attack)

if      random_attack == True:
        random_damage = random.randint(0,100)
        print(f"{titan2_name} as infligé {random_damage} a {titan1_name} " )
else:
    print("Tu n as fait aucun degat")

titan1_hp -= random_damage
print(f"{titan1_name} il te reste {titan1_hp } point de vie. ")



# FIN DU COMBAT
input()
print("\n LE COMBAT SE TERMINE MAINTENANT \n")

print(f"\n{titan1_name} il te reste {titan1_hp}")

print(f"\n{titan2_name} il te reste {titan2_hp}\n")

if titan1_hp > titan2_hp :
    print(f"{titan1_name} tu es le vainqeur de se combat.")

elif titan1_hp < titan2_hp :
    print(f"{titan2_name} tu es le vainqeur de ce combat" )

else:
    print("Vous etes à égalitée")
input()
