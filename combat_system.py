from random import randint
from lists.command_list import normalise_input
from lists.feedback_lists import *
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


def damage_dealt(weapon_input, attack_input, enemy):
    while True:
        if "attack" in attack_input:
            print("\n-------------------------------------------------")
            if (enemy["dodge"] - randint(1, 100)) < 0:
                damage = weapon_input["attributes"]["damage"] + randint(-8, 2)
                enemy["hp"] -= damage
                alpha = randint(0, 2)
                print()
                print(weapon_power_sword_attack[alpha])
                print()
                if enemy["hp"] <= 0:
                    print("With the last blow you deal to your opponent" +
                          "\nyou come out victorious as " + enemy["name"] + " is slain!")
                    return False
                else:
                    print(enemy["name"] + " is still alive.")
                    print(str(enemy["hp"]) + " HP Left.")
                    return True
            else:
                print("Your opponent dodges your attack.")
                return True
        elif "defend" in attack_input:
            print("There is no point defending yourself, go all out attack!!")
            attack_input = input("Would you like to attack or defend?: ")
            attack_input = normalise_input(attack_input)
        elif "quit" in attack_input:
            quit()
        else:
            attack_input = input("You need to choose either 'attack' or 'defend': ")
            attack_input = normalise_input(attack_input)


def damage_got(enemy):
    e_w_r = randint(0, len(enemy["weapon"]) - 1)
    print(enemy["name"] + " " + enemy["weapon"][e_w_r]["description"])
    if (enemy["weapon"][e_w_r]["accuracy"] - randint(1, 100)) >= 0:
        damage = enemy["weapon"][e_w_r]["damage"] - randint(0, enemy["weapon"][e_w_r]["damage"] - enemy["weapon"][e_w_r]["damage_bottom"])
        if damage > player.armor:
            player.hp -= damage
            if player.hp <= 0:
                print(player.player_name + " has been killed by " + enemy["name"])
            else:
                print(player.player_name + " is still alive.")
                print(str(player.hp) + " HP Left.")
        else:
            print("Your armor has deflected the entire opponent's damage!")
    else:
        print("Due to your opponent being rather inaccurate, their attack misses you.")


def main_fight(enemy):
    print()
    print("You have stumbled across " + enemy["name"] + " and he does not look a happy bunny.")
    print()
    print("You must fight " + enemy["name"] + " to proceed with the game.")
    print()
    print_list_of_weapons()
    while enemy["hp"] >= 1:
        weapon_choice = valid_weapon()
        attack_input = input("Would you like to attack or defend?: ")
        attack_input = normalise_input(attack_input)
        # Damage_dealt would return FALSE if enemy is dead, therefore damage_got will not be further executed.
        if damage_dealt(weapon_choice, attack_input, enemy):
            print()
            damage_got(enemy)