from random import randint
from lists.command_list import normalise_input
from lists.command_list import enter
from lists.command_list import GameOver
from lists.command_list import quit_test
from lists.command_list import screen_flush
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
        quit_test(weapon_input)
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
        else:
            # for weapon in list_of_weapons():
            #     if weapon_input[0] in weapon["id"]:
            if weapon_input[0].isdigit():
                if 0 < int(weapon_input[0]) <= len(list_of_weapons()):
                    weapon = list_of_weapons()[int(weapon_input[0]) - 1]
                    print()
                    print("You have chosen " + weapon["name"] + " with " + str(weapon["attributes"]["damage"]) + " base damage!\n")
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
    print("-----========[CHOOSE STANCE]========-----")
    print("1. Attack")
    print("2. Defend")
    print()
    attack_input = input(player.player_name + ": ")
    attack_input = normalise_input(attack_input)
    while True:
        quit_test(attack_input)
        if "1" in attack_input:
            print("\nYou take on an offensive stance! You deal normal damage.")
            return 1
        elif "2" in attack_input:
            print("\nYou take on a defensive stance! You deal less damage but gain more armor!")
            return 2
        else:
            attack_input = input("You need to choose an option from the list (number): ")
            attack_input = normalise_input(attack_input)


def damage_dealt(weapon_input, enemy, move):
    if move == 1:
        a = 1
    else:
        a = 2
    while True:
        print("\n-----========[BATTLE ROUND]========-----")
        alpha = randint(0, len(weapon_input["feedback"]) - 1)
        print()
        print(weapon_input["feedback"][alpha])
        if (enemy["dodge"] - randint(1, 100)) < 0:
            damage = int((weapon_input["attributes"]["damage"] + randint(-5, 3))/a)
            player.in_battle_enemy_hp -= damage
            hp = player.in_battle_enemy_hp
            if hp <= 0:
                print("With the last blow you deal to your opponent" +
                      "\nyou come out victorious as " + enemy["name"] + " is slain!")
                print("    ______________________________________________    _______________________________")
                print("   / __ )  /   | /__  __/ /__  __/ / /     / ____/    | |     / / / __ \  / | / / / /")
                print("  / __  | / /| |   / /      / /   / /     / __/       | | /| / / / / / / /  |/ / / / ")
                print(" / /_/ / / ___ |  / /      / /   / /___  / /___       | |/ |/ / / /_/ / / /|  / /_/  ")
                print("/_____/ /_/  |_| /_/      /_/   /_____/ /_____/       |__/|__/  \____/ /_/ |_/ (_)   ")
                print()
                player.score += enemy["score"]
                print("You have earned: " + str(enemy["score"]) + " bits!")
                enter()
                return False
            else:
                print(enemy["name"] + " is still alive with " + str(hp) + " HP Left.")
                return True
        else:
            print("Your opponent dodges your attack.")
            return True


def damage_got(enemy, move):
    if move == 1:
        a = 1
    else:
        a = 1.5
    armor = int(player.armor * a)
    e_w_r = randint(0, len(enemy["weapon"]) - 1)
    print(enemy["name"] + " " + enemy["weapon"][e_w_r]["description"])
    if (enemy["weapon"][e_w_r]["accuracy"] - randint(1, 100)) >= 0:
        damage = enemy["weapon"][e_w_r]["damage"] - randint(0, enemy["weapon"][e_w_r]["damage"] - enemy["weapon"][e_w_r]["damage_bottom"])
        if damage > armor:
            player.hp = player.hp + armor - damage
            if player.hp <= 0:
                print(player.player_name + " has been killed by " + enemy["name"])
            else:
                print("You have " + str(player.hp) + " HP Left.")
        else:
            print("Your armor has deflected the entire opponent's damage!")
    else:
        print("Due to your opponent being rather inaccurate, their attack misses you.")


def print_encounter():
    print()
    print("    ___________________________________________________________________  ")
    print("   / ____/ / | / / / ___\ / __ \  / / / / / | / / /_  __/ / ____/ / __ \ ")
    print("  / __/   /  |/ / / /    / / / / / / / / /  |/ /   / /   / __/   / /_/ / ")
    print(" / /___  / /|  / / /__  / /_/ / / /_/ / / /|  /   / /   / /___  / _, _/  ")
    print("/_____/ /_/ |_/  \____/ \____/  \____/ /_/ |_/   /_/   /_____/ /_/ |_|   ")
    print()


def print_stats(enemy):
    print("=============")
    print("Your HP: " + str(player.hp))
    print("Enemy HP: " + str(player.in_battle_enemy_hp))
    print("=============")


def main_fight(enemy):
    screen_flush()
    player.in_battle_enemy_hp = enemy["hp"]
    print_encounter()
    alpha = randint(0, len(encounter_fill) - 1)
    print("You have encountered " + enemy["name"] + encounter_fill[alpha])
    print("You must fight " + enemy["name"] + " to proceed (you cannot save during battle).")
    print()
    while True:
        a = input("Heads or Tails (winner goes first)? ")
        normalise_input(a)
        while True:
            quit_test(a)
            if "tails" in a:
                a = 0
                break
            elif "heads" in a:
                a = 1
                break
            else:
                a = input("You have to choose between Heads and Tails: ")
                a = normalise_input(a)
        b = randint(0, 1)
        if b == a:
            screen_flush()
            print_encounter()
            print("You go first!")
            enter()
            while player.in_battle_enemy_hp >= 1:
                screen_flush()
                print_encounter()
                print_stats(enemy)
                weapon_choice = valid_weapon()
                move = move_prompt()
                # Damage_dealt would return FALSE if enemy is dead, therefore damage_got will not be further executed.
                if damage_dealt(weapon_choice, enemy, move):
                    print()
                    damage_got(enemy, move)
                    if player.hp <= 0:
                        raise GameOver
                    enter()
                    screen_flush()

            break
        else:
            screen_flush()
            print_encounter()
            print(enemy["name"] + " goes first!")
            enter()
            print()
            move = 1
            while player.in_battle_enemy_hp >= 1:
                screen_flush()
                print_encounter()
                print_stats(enemy)
                print()
                damage_got(enemy, move)
                if player.hp <= 0:
                    raise GameOver
                weapon_choice = valid_weapon()
                move = move_prompt()
                # Damage_dealt would return FALSE if enemy is dead, therefore damage_got will not be further executed.
                if damage_dealt(weapon_choice, enemy, move):
                    enter()
                    screen_flush()
            break