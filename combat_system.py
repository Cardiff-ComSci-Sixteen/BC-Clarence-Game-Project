from random import randint
from lists.command_list import normalise_input
from lists.command_list import enter
from lists.command_list import game_over
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
    a = 0
    weapon_list = list_of_weapons()
    for item in weapon_list:
        a += 1
        print(str(a) + ". " + item["name"])
    return weapon_list


def valid_weapon():
    print()
    print("-----========[CHOOSE WEAPON]========-----")
    print_list_of_weapons()
    print()
    weapon_input = input(player.player_name + ": ")
    weapon_input = normalise_input(weapon_input)
    while True:
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
            print()
        elif weapon_input[0] == "quit":
            quit()
        else:
            # for weapon in list_of_weapons():
            #     if weapon_input[0] in weapon["id"]:
            if weapon_input[0].isdigit():
                if 0 < int(weapon_input[0]) <= len(list_of_weapons()):
                    weapon = list_of_weapons()[int(weapon_input[0]) - 1]
                    print("You have chosen " + weapon["name"] + "!")
                    print("It has got " + str(weapon["attributes"]["damage"]) + " base damage!\n")
                    return weapon
                else:
                    a = input("You have not entered a valid weapon number from the list!\n" + player.player_name + ": ")
                    weapon_input = normalise_input(a)
            else:
                a = input("You have not entered a valid weapon number from the list!\n" + player.player_name + ": ")
                weapon_input = normalise_input(a)


def reset_enemy_hp(enemy, health):
    enemy["hp"] = health


def move_prompt():
    print()
    print("-----========[CHOOSE ACTION]========-----")
    print("1. Attack")
    print("2. Defend")
    print()
    attack_input = input(player.player_name + ": ")
    attack_input = normalise_input(attack_input)
    while True:
        if "1" in attack_input:
            return 1
        elif "2" in attack_input:
            print("There is no point defending yourself, go all out attack!!")
            attack_input = normalise_input(input(player.player_name + ": "))
        elif "quit" in attack_input:
            quit()
        else:
            attack_input = input("You need to choose an option from the list (number): ")
            attack_input = normalise_input(attack_input)


def damage_dealt(weapon_input, enemy):
    while True:
        print("\n-----========[BATTLE ROUND]========-----")
        if (enemy["dodge"] - randint(1, 100)) < 0:
            damage = weapon_input["attributes"]["damage"] + randint(-5, 3)
            player.in_battle_enemy_hp -= damage
            hp = player.in_battle_enemy_hp
            alpha = randint(0, 2)
            print()
            print(weapon_power_sword_attack[alpha])
            print()
            if hp <= 0:
                print("With the last blow you deal to your opponent" +
                      "\nyou come out victorious as " + enemy["name"] + " is slain!")
                print("\n---====[BATTLE OVER]====---")
                enter()
                return False
            else:
                print(enemy["name"] + " is still alive.")
                print(str(hp) + " HP Left.")
                return True
        else:
            print("Your opponent dodges your attack.")
            return True


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
    player.in_battle_enemy_hp = enemy["hp"]
    print()
    print("You have stumbled across " + enemy["name"] + " and he does not look a happy bunny.")
    print()
    print("You must fight " + enemy["name"] + " to proceed with the game.")
    while player.in_battle_enemy_hp >= 1:
        move = move_prompt()
        if move == 1:
            weapon_choice = valid_weapon()
            # Damage_dealt would return FALSE if enemy is dead, therefore damage_got will not be further executed.
            if damage_dealt(weapon_choice, enemy):
                print()
                damage_got(enemy)
                if player.hp <= 0:
                    game_over()
                enter()