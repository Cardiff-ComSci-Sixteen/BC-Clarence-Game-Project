from lists.command_list import *
import combat_system
from items.monsters import *
from items.objects import *
from lists.use import *


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
    if player.current_room["name_ID"] == "Hangar 2" and player.hangar_2_power == 0 and "power_up_hangar" not in player.objectives:
        player.objectives["power_up_hangar"] = "I need to power up Hangar #2 somehow."
        player.objectives_changed = 1
    if player.current_room["name_ID"] == "Hangar 2" and player.hangar_2_power == 1:
        screen_flush()
        print("As you enter Hangar 2 you see the room completely lit. The hangar"
              "\ndoor is closed and there is a big fighter plane inside the room with an open"
              "\ncockpit. You hear noise from the left where a whole stash of Vodka is laying"
              "\nand as you look there you see someone walking out. Someone rather familiar..."
              )
        enter()
        print("As the unknown man approaches you, not wearing any top clothing,"
              "\nholding a bottle of Vodka, you pull back against the wall.")
        enter()
        print("Do you remember me, " + player.player_name + "?"
              "\n10 years ago you imprisoned me on this ship, apparently because I was"
              "\nsome kind of a scary man! Well, the time has come to settle this."
              "\n"
              "\nI brought you here, using my super amazing computer skills and"
              "\nnow it is YOUR turn to die for 10 years... Or more!"
              "\nXaxaxaxa! That will be fun~")
        print("...")
        print("I better get ready to fight!")
        enter()
        combat_system.main_fight(enemy_kirill)
        player.encounters.append(player.current_room["name_ID"])
        print()
        print("As Kirill has been slain after an exhausting battle,"
              "\nblood stains covering your arms, you get up and look at the fighter."
              "\nYou open the hangar doors from the console on the right and get inside"
              "\nthe fighter's cockpit."
              "\n\nAs You are a Computer Scientist, with your brain big, you"
              "\nmanage to hack into the console of the ship and take off, freely escaping"
              "\nBC Clarence alive and full of stories to tell!")
        raise Victory

    if player.current_room["name_ID"] == "Vehicle Storage" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Power Generator" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Main Engineering" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Officer Deck" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Crew Quarters" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(monster_kirill_minion)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Bridge" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(enemy_matt)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Detention Centre" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(enemy_potter)
        player.encounters.append(player.current_room["name_ID"])

    if player.current_room["name_ID"] == "Armory" and player.current_room["name_ID"] not in player.encounters:
        combat_system.main_fight(enemy_volderwart)
        player.encounters.append(player.current_room["name_ID"])


# Events checked each time you give input
def input_event_update(user_input, exits, inventory):
    if (user_input == ["charge", "scanner"] or user_input == ["recharge", "scanner"]) and player.current_room["name"] == "Wrecked Ship":
        print("You have successfully recharged your scanner!")
        item_scanner["attributes"]["power"] = 50
        return True
    if (user_input == ["start", "generator"] or
        user_input == ["press", "button"] or
        user_input == ["press", "start"] or
       user_input == ["start", "power_generator"]) and player.current_room["name"] == "Power Control":
            if player.hangar_2_power == 0:
                print("\nYou turn on the power generator for Hangar #2. After a few seconds the button"
                      "\nunder the 'Hangar #2' label turns green, meaning there is power in the Hangar.")
                object_powerconsole["description"] = "All the buttons are green now! There should be power in Hangar #2."
                rooms["Power Control"]["description"] = ("Power is distributed using this. Every room has a 'START' and 'STOP' button"
                                                         "\nto control its power. All 'START' buttons are green besides where"
                                                         "\nthe generator for Hangar #2 is. Starting the generator may be my"
                                                         "\nonly chance out of here!")
                player.hangar_2_power = 1
                if "power_up_hangar" in player.objectives:
                    del player.objectives["power_up_hangar"]
                player.objectives["escape_from_hangar"] = "I need to get to Hangar #2 and escape!"
                print("\nOBJECTIVES UPDATED")
            else:
                print("\nThe generator is already on!")
            return True
    return False