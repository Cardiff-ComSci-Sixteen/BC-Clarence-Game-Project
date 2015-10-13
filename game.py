import random
from command_list import *
# # import string
# import debug
from map import rooms
from player import inventory
from objects import *

in_room = "Player Ship"
player_name = input("Type a player name (12 characters max): ")
while True:
    if len(player_name) > 12:
        print("Your name should be 12 characters or less!")
        player_name = input("Type a player name: ")
    else:
        break


def remove_punct(text):
    txt = text
    for punct in string.punctuation:
        txt = txt.replace(punct, "")
    return txt


def remove_spaces(text):
    text = text.strip()
    print(text)


def display_room(room):
    print("\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n")
    print_room_items(room)


def exit_leads_to(exits, direction):
    if direction not in exits:
        return 0
    return exits[direction]


def print_menu_line(leads_to):
    if leads_to == 0:
        return 0
    else:
        return "Go to " + leads_to


def print_menu(exits):
    print("You can:")
    exit_list = []
    for ch in rooms[in_room]["exits"]:
        if ch not in exits:
            pass
        else:
            exit_list.append(ch)
            print(print_menu_line(rooms[exit_leads_to(exits, ch)]["name"]))
    return exit_list


def is_valid_command(user_input):
    if user_input in commands:
        return True
    else:
        return False


# Mainly replaces the command_execute function given during Exercise_2
def command_execute(exits):
    print_menu(exits)
    global player_name
    user_input = "a"
    while True:
        if user_input.strip() == "":
            user_input = input(player_name + ": ")
        else:
            user_input = input("\n" + player_name + ": ")
        if user_input.strip() == "":
            pass
        else:
            user_input = user_input.lower()
            cmd = user_input
            cmd = normalise_input(cmd)
            if len(cmd) >= 1:
                # Checks if user input (command) is less or more than 3 words in length. If less, does nothing, if more, makes the second word
                # the same as the second and third word combined, so if we have ["go", "hangar", "1"] it will give ["go", "hangar_1"]
                if len(cmd) < 3:
                    pass
                elif len(cmd) >= 3:
                    cmd_combined = cmd[1] + "_" + cmd[2]
                    del cmd[1:len(cmd) - 1]
                    cmd[1] = cmd_combined
                cmdn = cmd[0]

                if is_valid_command(cmdn) or cmdn in dire or (user_input.find("inspect") >= 0):
                    # Checks if you type "go <dir>", "go" + "<dir>" or just <dir> (dir = direction)
                    if cmdn == "go":
                        valid = command_go_superior(exits, in_room, cmd)
                        if valid:
                            return valid
                    if cmdn == "playername":
                        player_name = command_name_change()
                    if cmdn == "exits":
                        print_menu(exits)
                    if cmdn == "help":
                        command_help()
                    if cmdn == "quit":
                        quit()
                    if cmdn == "inventory":
                        command_inventory(inventory)
                    if user_input.find("inspect") >= 0:
                        user_input = user_input.replace("inspect", "")
                        cmd = normalise_input(user_input)
                        inspect_element(rooms[in_room], cmd, player_name)
                        user_input = str(cmd)
                else:
                    i = random.randint(0, len(command_unknown) - 1)
                    print(command_unknown[i])


def move(exits, direction):
    return rooms[exits[direction]]


def menu(current_room):
    display_room(current_room)
    exits = current_room["exits"]
    command_input = command_execute(exits)

    print("DEBUG NOTICE: COMMAND_INPUT " + command_input)
    if command_input == "hangar_1" and get_room_state(rooms_states["Hangar 1"]) == 1:
        rooms_states[current_room["name_ID"]]["state"] = 3

    current_room = move(exits, command_input)
    in_room = current_room["name_ID"]
    return move(exits, command_input)


def main():
    # Start game at the room_1
    current_room = rooms["Player Ship"]
    print("Type 'help' to see a list of available commands.")
    global in_room
    # Main game loop
    while True:
        update_room_state(current_room["name_ID"])
        current_room = menu(current_room)
        in_room = current_room["name_ID"]

# NEW
# NEW
# NEW
# def menu(exits, room_items, inv_items):
#     """This function, given a dictionary of possible exits from a room, and a list
#     of items found in the room and carried by the player, prints the menu of
#     actions using print_menu() function. It then prompts the player to type an
#     action. The players's input is normalised using the normalise_input()
#     function before being returned.
#
#     """
#
#     # Display menu
#     print_menu(exits, room_items, inv_items)
#
#     # Read player's input
#     user_input = input("> ")
#
#     # Normalise the input
#     normalised_user_input = normalise_input(user_input)
#
#     return normalised_user_input
main()
