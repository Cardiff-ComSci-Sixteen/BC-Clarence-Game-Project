from player_combatsystem import *
from items_combatsystem import *
from random import randint


# def list_of_weapons():



def list_of_weapons():
    print("This is a list of all the weapons you have to fight with: ")
    print(sword["Name"])
    print(gun["Name"])
    print(lightsaber["Name"])
    print(blaster["Name"])
    print()


def valid_weapon():
    while True:
        global weapon_input
        weapon_input = input("What weapon would you like to fight with?: ").lower()
        if weapon_input == "sword":
            break
        elif weapon_input == "sword of azrath":
            break
        elif weapon_input == "gun":
            break
        elif weapon_input == "the holy gun":
            break
        elif weapon_input == "the stick of life":
            break
        elif weapon_input == "lightsaber":
            break
        elif weapon_input == "light saber":
            break
        elif weapon_input == "the blaster rifle":
            break
        elif weapon_input == "blaster":
            break
        elif weapon_input == "rifle":
            break
        else:
            print("You have not entered a valid weapon name!")
            continue


def damage_dealt(weapon_input, attack_input):
    if weapon_input == "sword of azrath" or weapon_input == "sword":
        if attack_input == "attack":
            damage = sword["Damage"]
            enemy["HP"] += - damage
            if enemy["HP"] <= 0:
                print(enemy["Name"] + " has been killed.")
                print(str(enemy["HP"]) + " HP Left.")
            else:
                print(enemy["Name"] + " is still alive.")
                print(str(enemy["HP"]) + " HP Left.")
            damage_got()
            return enemy["HP"]
        if attack_input == "defend":
            print("There is no point defending yourself, go all out attack!!")

    if weapon_input == "the holy gun" or weapon_input == "gun":
        if attack_input == "attack":
            damage = 75
            enemy["HP"] += - damage
            if enemy["HP"] <= 0:
                print(enemy["Name"] + " has been killed.")
                print(str(enemy["HP"]) + " HP Left.")
            else:
                print(enemy["Name"] + " is still alive.")
                print(str(enemy["HP"]) + " HP Left.")
            damage_got()
            return enemy["HP"]
        if attack_input == "defend":
            print("There is no point defending yourself, go all out attack!!")

    if weapon_input == "glow stick of life" or weapon_input == "lightsaber" or weapon_input == "light saber":
        if attack_input == "attack":
            damage = 80
            enemy["HP"] += - damage
            if enemy["HP"] <= 0:
                print(enemy["Name"] + " has been killed.")
                print(str(enemy["HP"]) + " HP Left.")
            else:
                print(enemy["Name"] + " is still alive.")
                print(str(enemy["HP"]) + " HP Left.")
            damage_got()
            return enemy["HP"]
        if attack_input == "defend":
            print("There is no point defending yourself, go all out attack!!")

    if weapon_input == "the blaster rifle" or weapon_input == "blaser rifle" or weapon_input == "rifle":
        if attack_input == "attack":
            damage = 60
            enemy["HP"] += - damage
            if enemy["HP"] <= 0:
                print(enemy["Name"] + " has been killed.")
                print(str(enemy["HP"]) + " HP Left.")
            else:
                print(enemy["Name"] + " is still alive.")
                print(str(enemy["HP"]) + " HP Left.")
            damage_got()
            return enemy["HP"]
        if attack_input == "defend":
            print("There is no point defending yourself, go all out attack!!")


def damage_got():
    print(enemy["Name"] + " swings at you with his spoon with extreme aggression.")

    damage = randint(4, 20)
    elliott["HP"] += - damage
    if elliott["HP"] <= 0:
        print(elliott["Name"] + " has been killed.")
        print(str(elliott["HP"]) + " HP Left.")
    else:
        print(elliott["Name"] + " is still alive.")
        print(str(elliott["HP"]) + " HP Left.")
    return elliott["HP"]


def main_fight():
    print()
    print("You have stumbled across " + enemy["Name"] + " and he does not look a happy bunny.")
    print()
    print("You must fight " + enemy["Name"] + " to proceed with the game.")
    print()
    list_of_weapons()
    while enemy["HP"] >= 1:
        valid_weapon()
        weapons(weapon_input)
        attack_input = input("Would you like to attack or defend?: ")
        damage_dealt(weapon_input, attack_input)