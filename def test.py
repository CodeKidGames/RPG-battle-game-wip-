import time
from random import randint as randint
# Gate system, each gate requires something to get through.
# var + level. php1 = player hp level 1.

php1 = 5000
item = randint(1, 10)
mhp1 = 2000
monster_attack1 = randint(500, 750)
magic1 = randint(500, 1500)
player_attack1 = randint(750, 1000)
defence = randint(300, 500)
exp = 0
# DEFENCE FUNCTION
# x = monster damage (with defence deduction), y = player hp.


def damage2(x, y):
    print("----------\nYou defended")
    y = y - x
    print("----------\nThe monster did", x, "damage.\n----------\n")
    print("You have", y, "HP")


# ATTACK FUNCTION
# x = players attack damage, y = Monster hp, b = Player hp, a = monsters attack
def damage1(x, y, b, a):

    print("----------\nyou did", x, "damage.\n----------")

    print("monster has", y, "HP\n----------")
    y = y - x
    time.sleep(0.5)
    
    print("The monster did", a, "damage\n----------")
    b = b - a
    print("You have", b, "HP")



# x is just the exp or item needed


def win(x):
    print("You Win!!\n")
    x = x + 1
    print("You now have", x, "exp!")


while exp < 5:
    action = input("What would you like to do. Hunt, go, search, or talk: ")

    if action == "Hunt":
        print("A monster appears! (Lvl 1)")
        while php1 and mhp1 > 0:
            if php1 < 0:
                print("fucking loser.")
            else:
                attack_action = input('what do you do? 1 = attack 2 = magic 3 = defend: ')
            if attack_action == "3":
                damage2(defence, php1)
                continue
            elif attack_action == "1":
                damage1(player_attack1, mhp1, php1, monster_attack1)

                continue
            elif attack_action == "2":
                damage1(magic1, mhp1, php1, monster_attack1)
                continue
            else:
                continue
            if mhp1 < 0:
                win(exp)
    elif action == "go":
        if exp >= 5:
            print("You advance to level 2!")
        else:
            print("You do not have enough exp!")

time.sleep(1)
print("story thing or what not idk")
magic2 = randint(800, 1750)
php2 = 5500
mhp2 = randint(2250, 2750)
monster_attack2 = randint(750, 1400)
player_attack2 = randint(1000, 1500)
defence2 = randint(560, 1050)

while exp < 10:
    action = input("What would you like to do. Hunt, go, search, or talk: ")

    if action == "Hunt":
        print("A monster appears! (Lvl 1)")
        while php2 and mhp2 > 0:
            if php2 < 0:
                print("fucking loser.")
            else:
                attack_action = input('what do you do? 1 = attack 2 = magic 3 = defend: ')
            if attack_action == "3":
                damage2(defence2, php2)
                continue
            elif attack_action == "1":
                damage1(player_attack2, mhp2, php2, monster_attack2)
                continue
            elif attack_action == "2":
                damage1(magic2, mhp2, php2, monster_attack2)
            else:
                continue
            if mhp1 < 0:
                win(exp)
    elif action == "go":
        if exp >= 10:
            print("You advance to level 3!")
        else:
            print("You do not have enough exp!")
