from map import rooms
from items.items import *
import player

def heal(amount):
    if player.hp + amount > 100:
        player.hp = 100
        print("You healed back at maximum health!")
    else:
        player.hp += amount
        print("You healed for " + str(amount) + " health.")

def unheal(amount):
    if player.hp - amount <= 0:
        return False
    else:
        player.hp -= amount
        print("You lost " + str(amount) + " health.")
        return True

def use_crowbar():
    user = input("Should I break the doors to 'Bridge' (yes/no)? ")
    if user == "yes":
        rooms["Bridge"]["requirement"].remove(item_crowbar)
        print("I have broken the doors! Now I can finally enter.")
    elif user.lower().strip() == "no":
        print("Ok!")
    else:
        print("I did not get that.")


def use_keyA():
    user = input("Should I swipe the keycard and unlock the doors to the Armory' (yes/no)? ")
    if user == "yes":
        rooms["Armory"]["requirement"].remove(item_keyA)
        print("I have swiped the card and the Armory is now unlocked.")
    elif user.lower().strip() == "no":
        print("Ok!")
    else:
        print("I did not get that.")


def use_keyD():
    user = input("Should I swipe the keycard and unlock the doors to the Detention Centre (yes/no)? ")
    if user == "yes":
        rooms["Detention Centre"]["requirement"].remove(item_keyD)
        print("I have swiped the card and the Detention Centre is now unlocked.")
    elif user.lower().strip() == "no":
        print("Ok!")
    else:
        print("I did not get that.")


def use_keyP():
    user = input("Should I swipe the keycard and unlock the doors to the Power Control room (yes/no)? ")
    if user == "yes":
        rooms["Power Control"]["requirement"].remove(item_keyP)
        print("I have swiped the card and the Power Control room is now unlocked.")
    elif user.lower().strip() == "no":
        print("Ok!")
    else:
        print("I did not get that.")


def use_medkit():
    player.inventory.remove(item_medkit)
    print("You opened the Med-Kit box and took some bandages to put on yourself.")
    heal(25)


def use_biscuits():
    player.inventory.remove(item_biscuits)
    print("You opened a delicious-looking pack of biscuits, but little do you know - they are poisoned.")
    if not unheal(10):
        print("You are left on 1 hp!")
        player.hp = 1