from lists.command_list import *
import combat_system
from items.monsters import *


def player_name():
    player.player_name = input("What is your name? ")
    while True:
        if player.player_name.strip() == "quit":
            quit()
        elif player.player_name.strip() == "":
            print("Your name should include something!")
            player.player_name = input("\nType a player name: ")
        elif len(player.player_name) > 12:
            print("Your name should be 12 characters or less!")
            player.player_name = input("\nType a player name: ")
        else:
            break


def intro_help_prompt():
    text = input("Do you want to help the vessel? ")
    text = normalise_input(text)
    if text:
        pass
    else:
        text = ["null"]
    while True:
        if text[0] == "yes":
            print("\nAs you decide to help the distressed ship you adjust"
                  "\nthe coordinates on your board AI and alter your"
                  "\ncourse towards the ship.")
            break
        elif text[0] == "no":
            print("\nHaving chosen not to help the ship you carry on with"
                  "\nyour current path. However, after a few minutes you"
                  "\nnotice a change in your course as you turn towards that of"
                  "\nthe distressed ship. You try to change the coordinates,"
                  "\nbut to no avail.")
            break
        text = input_hang(text, "Yes or No?")


def intro():
    print()
    print("It is 2133, the Age of Colonization. Having boarded"
          "\nyour little but robust spaceship - Sparrow the Space Lorry -"
          "\nyou have been given as a task for the day to transport"
          "\ngoods to the 42 V-Class Starbase. However, on your way"
          "\nto the station you receive a distress signal from BC Clarence"
          "\nlocated at about 1800 space miles from you, asking for help.")
    print()
    print("The signal grabs your attention as you need to make a decision.")
    intro_help_prompt()
    enter()
    print("As you fly towards the location of the distressed ship"
          "\nyou stay alert in your small ship, monitoring your AI for any"
          "\nfurther information there might be about the vessel. You try to call"
          "\nClarence several times, but you never get any response."
          "\n\nEventually, after around 40 minutes you see a big, dark-brown"
          "\nship with barely any light emitting from it, several panels seemingly"
          "\ntorn apart from the hull, probably due to an explosion."
          "\nYou approach very close to about 2 space miles from BC Clarence as all of a sudden"
          "\nyour ship is jolted forward, followed by a loud bang from the engine compartment."
          "\n\nYou panic as your board AI warns you that you are on a collision"
          "\ncourse with BC Clarence and notifies you of an emergency docking"
          "\nprocedure in effect.")
    enter()


def intro_prompt():
    player_name()
    intro_input = input("Skip Intro? ")
    intro_input = normalise_input(intro_input)
    if intro_input:
        pass
    else:
        intro_input = ["null"]
    while True:
            if intro_input[0] == "no":
                intro()
                break
            elif intro_input[0] == "yes":
                break
            intro_input = input_hang(intro_input, "Yes or No? ")


def post_intro_prompt(inventory):
    print()
    print("You prepare for a crash landing as there is no other option for you."
          "\nYou go to the emergency bay of your ship and decide to take some"
          "\nstuff with you just in case things go wrong afterwards.")
    print()
    print("Pick a weapon: ")
    print("1. Power Sword")
    print("2. Laspistol")
    print("3. Sword-Gun")
    weapon_choice = input("")
    while True:
        if weapon_choice == "1":
            inventory.append(weapon_powersword)
            break
        if weapon_choice == "2":
            inventory.append(weapon_laspistol)
            break
        if weapon_choice == "3":
            inventory.append(weapon_swordgun)
            break
        else:
            weapon_choice = input("Type 1, 2 or 3 to select weapon. ")
    print("\nPick armor: ")
    print("1. Recon Suit")
    print("2. Engineering Suit")
    print("3. No Clothing")
    armor_choice = input()
    while True:
        if armor_choice == "1":
            inventory.append(armor_lightarmour1)
            break
        if armor_choice == "2":
            inventory.append(armor_heavyarmour1)
            break
        if armor_choice == "3":
            player.is_naked = 1
            break
        else:
            armor_choice = input("Type 1, 2 or 3 to select armor. ")
    print("\nPick a consumable: ")
    print("1. Biscuits")
    print("2. Coffee")
    print("3. Med-Kit")
    consumable_choice = input()
    while True:
        if consumable_choice == "1":
            inventory.append(item_biscuits)
            break
        if consumable_choice == "2":
            inventory.append(item_coffee)
            break
        if consumable_choice == "3":
            inventory.append(item_medkit)
            break
        else:
            consumable_choice = input("Type 1, 2 or 3 to select consumable. ")


# Events checked each time you change rooms
def event_update(exits):
    if player.current_room["name_ID"] == "Hangar 1" and player.last_room == "Hangar 2":
        print("You hear a loud bang behind you. You turn around and see that the exit to Hangar 2 has collapsed.")
        del player.current_room["exits"]["hangar_2"]
    # if player.current_room["name_ID"] == "Vehicle Storage" and player.current_room["name_ID"] not in player.encounters:
    #     combat_system.main_fight(monster_kirill_minion)
    #     print_room(player.current_room)
    #     print_menu(exits)
    #     player.encounters.append(player.current_room["name_ID"])
    #     print("LIST " + str(player.encounters))
    if player.current_room["name_ID"] == "Crew Quarters" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        print_room(player.current_room)
        print_menu(exits)
        player.encounters.append(player.current_room["name_ID"])
    # if player.current_room["name_ID"] == "Bridge" and player.current_room["name_ID"] not in player.encounters:
    #     combat_system.main_fight(enemy_matt)
    #     print_room(player.current_room)
    #     print_menu(exits)
    #     player.encounters.append(player.current_room["name_ID"])
    # if player.current_room["name_ID"] == "Detention Centre" and player.current_room["name_ID"] not in player.encounters:
    #     combat_system.main_fight(enemy_potter)
    #     print_room(player.current_room)
    #     print_menu(exits)
    #     player.encounters.append(player.current_room["name_ID"])
    # if player.current_room["name_ID"] == "Armory" and player.current_room["name_ID"] not in player.encounters:
    #     combat_system.main_fight(enemy_volderwart)
    #     print_room(player.current_room)
    #     print_menu(exits)
    #     player.encounters.append(player.current_room["name_ID"])


# Events checked each time you give input
def input_event_update(user_input, exits, inventory):
    if (user_input == ['eat', 'biscuits'] or user_input == ['eat', 'pack_biscuits'] or user_input == ['eat', 'pack']) and item_biscuits in inventory:
        inventory.remove(item_biscuits)
        print("You ate the biscuits and soon start feeling ill. As a result you lose 10 hp!")
        player.hp -= 10
        return True
    if user_input == ["battle"]:
        combat_system.main_fight(monster_kirill_minion)
        print_room(player.current_room)
        print_menu(exits)
        return True
    if (user_input == ["charge", "scanner"] or user_input == ["recharge", "scanner"]) and player.current_room["name"] == "Wrecked Ship":
        print("You have successfully recharged your scanner!")
        item_scanner["attributes"]["power"] = 50
        return True
    return False