from command_list import *


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
    text = input("Do you want to help the vessel?")
    text = normalise_input(text)
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


def enter():
    input("\nPress to continue.\n")


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
          "\nYou approach very close at about 2 space miles from BC Clarence as all of a sudden"
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
            intro_input = input_hang(intro_input, "Yes or No?")


def post_intro_prompt():
    print()
    print("You prepare for a crash landing as there is no other option for you."
          "\nYou go to the emergency bay of your ship and decide to take some"
          "\nstuff with you just in case things go wrong afterwards.")
    print()
    print("Pick a weapon: ")
    print("1. " + item_powersword["name"])
    print("2. " + item_laspistol["name"])
    print("3. " + item_swordgun["name"])
    weapon_choice = input("")
    while True:
        if weapon_choice == "1":
            inventory.append(item_powersword)
            break
        if weapon_choice == "2":
            inventory.append(item_laspistol)
            break
        if weapon_choice == "3":
            inventory.append(item_swordgun)
            break
        else:
            weapon_choice = input("Type 1, 2 or 3 to select weapon. ")
    print("\nPick armor: ")
    print("1. Basic Spacesuit")
    print("2. Basic Armor")
    print("3. No Clothing")
    armor_choice = input()
    while True:
        if armor_choice == "1":
            inventory.append(item_basic_spacesuit)
            break
        if armor_choice == "2":
            inventory.append(item_basic_armor)
            break
        if armor_choice == "3":
            player.is_nakedked = 1
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