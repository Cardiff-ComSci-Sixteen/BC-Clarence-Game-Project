from random import randint
from lists.command_list import normalise_input
from lists.feedback_lists import *
import player
import player

# def list_of_weapons():


def list_of_weapons():
    weapon_list = []
    for item in player.inventory:
        if item["class"] == 1:
            weapon_list.append(item)
    return weapon_list


def print_list_of_weapons():
    print("List of all the weapons you can currently fight with:")
    for item in list_of_weapons():
        print(item["name"])


def valid_weapon():
    while True:
        weapon_input = input("\nWhat weapon would you like to fight with (type 'weapons' to see list): ").lower()
        weapon_input = normalise_input(weapon_input)
        # Checks if weapon_input list after being normalised has more than 1 word. If yes, combines 0 and 1 index of list into a 0-index list.
        if len(weapon_input) > 1:
            weapon_input[0] = weapon_input[0] + "_" + weapon_input[1]
            weapon_input = weapon_input[:1]
        # If list empty after normalization, puts an item in index 0 to prevent crash further down the function
        elif len(weapon_input) < 1:
            weapon_input = ["a"]
        # Tests if user input is a weapon from the list or no
        if weapon_input[0] == "weapons":
            print()
            print_list_of_weapons()
        else:
            for weapon in list_of_weapons():
                if weapon_input[0] in weapon["id"]:
                    print("You have chosen " + weapon["name"] + "!")
                    print("It has got " + str(weapon["attributes"]["damage"]) + " base damage!\n")
                    return weapon
        print("You have not entered a valid weapon name from the list!")


def damage_dealt(weapon_input, attack_input):
    while True:
        if "attack" in attack_input:
            damage = weapon_input["attributes"]["damage"] + randint(-8, 2)
            player.enemy["HP"] -= damage
            alpha = randint(0, 2)
            print()
            print(weapon_power_sword_attack[alpha])
            print()
            if player.enemy["HP"] <= 0:
                print("With the last blow you deal to " + player.enemy["Name"] +
                      "\nyou come out victorious as " + player.enemy["Name"] + " is slain!")
                return False
            else:
                print(player.enemy["Name"] + " is still alive.")
                print(str(player.enemy["HP"]) + " HP Left.")
                return True
        elif "defend" in attack_input:
            print("There is no point defending yourself, go all out attack!!")
            attack_input = input("Would you like to attack or defend?: ")
            attack_input = normalise_input(attack_input)
        else:
            attack_input = input("You need to choose either 'attack' or 'defend': ")
            attack_input = normalise_input(attack_input)


def damage_got():
    print(player.enemy["Name"] + " swings at you with his spoon with extreme aggression.")
    damage = randint(4, 20)
    player.hp += - damage
    if player.hp <= 0:
        print(player.player_name + " has been killed.")
    else:
        print(player.player_name + " is still alive.")
        print(str(player.hp) + " HP Left.")


def main_fight():
    print()
    print("You have stumbled across " + player.enemy["Name"] + " and he does not look a happy bunny.")
    print()
    print("You must fight " + player.enemy["Name"] + " to proceed with the game.")
    print()
    print_list_of_weapons()
    while player.enemy["HP"] >= 1:
        weapon_choice = valid_weapon()
        # weapons()
        attack_input = input("Would you like to attack or defend?: ")
        attack_input = normalise_input(attack_input)
        # Damage_dealt would return FALSE if enemy is dead, therefore damage_got will not be further executed.
        if damage_dealt(weapon_choice, attack_input):
            print()
            damage_got()