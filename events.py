import player
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
    print("You prepare for a crash landing as there is no other option for you."
          "\nYou go to the emergency bay of your ship and decide to take some"
          "\nstuff with you just in case things go wrong afterwards.")
    # input("Pick a weapon: ")
    while True:
        a = input("DEBUG Type END to stop intro loop and get to game loop.")
        if a == "end":
            break


def intro_prompt():
    player_name()
    intro_input = input("Play intro?")
    intro_input = normalise_input(intro_input)
    while True:
            if intro_input[0] == "yes":
                intro()
                break
            elif intro_input[0] == "no":
                break
            intro_input = input_hang(intro_input, "Yes or No?")