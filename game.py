import random
from command_list import *
# # import string
# import debug
from map import rooms
from player import inventory
from objects import *

in_room = "room_1"
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


def exit_leads_to(exits, direction):
    #
    # room = exits[direction]
    #
    # x = ["Going " + direction + " will lead to " + room + ".",
    # room + " is to the " + direction + ".",
    # "By going " + direction + " you will get to " + room + ".",
    # room + " is located to the " + direction + ".",
    # "Going " + direction + " takes you to " + room + "."]
    # y = random.randint(0, 4)

    if direction not in exits:
        return 0
    return exits[direction]


def print_menu_line(direction, leads_to):
    if leads_to == 0:
        return 0
    else:
        return "Go " + direction.upper() + " to " + leads_to


def print_menu(exits):
    print("You can:")
    exit_list = []
    for ch in dire:
        if ch not in exits:
            pass
        else:
            exit_list.append(ch)
            print(print_menu_line(ch, exit_leads_to(exits, ch)))
    return exit_list


def is_valid_command(user_input):
    if user_input in commands:
        return True
    else:
        return False

# Mainly replaces the command_execute function given during Exercise_2
def menu(exits):
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
                cmdn = cmd[0]
                if is_valid_command(cmd[0]) or cmdn in dire or (user_input.find("inspect") >= 0):
                    # Checks if you type "go <dir>", "go" + "<dir>" or just <dir> (dir = direction)
                    if cmdn == "go" or cmd[0] in dire:
                        while True:
                            if len(cmd):
                                if (cmd[0] == "go" and len(cmd) == 1) or (cmd[0] == "go" and cmd[1] in dire) or cmd[0] in dire:
                                    if len(cmd) > 1:
                                        direction = command_go(exits, cmd[1])
                                        if direction in dire:
                                            return direction
                                        break
                                    elif cmd[0] in dire:
                                        direction = command_go(exits, cmd[0])
                                        if direction in dire:
                                            return direction
                                        break
                                    else:
                                        cmd = input("Go where?")
                                        cmd = normalise_input(cmd)
                                elif len(cmd):
                                    print("I did not quite get that.\n")
                                    user_input = ""
                                    break
                            else:
                                break
                    if cmdn == "playername":
                        player_name = command_name_change()
                    if cmdn == "exits":
                        print_menu(exits)
                    if cmdn == "help":
                        command_help()
                    if cmdn == "quit":
                        quit()
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


def main():
    # Start game at the room_1
    current_room = rooms["room_1"]
    print("Type 'help' to see a list of available commands.")
    global in_room
    # Main game loop
    while True:
        # if current_room["name_ID"] == "room_1":
        update_room_state(current_room["name_ID"])

        display_room(current_room)

        exits = current_room["exits"]

        command_input = menu(exits)

        if command_input == "south" and get_room_state(rooms_states["room_1"]) == 1:
            rooms_states[current_room["name_ID"]]["state"] = 3

        current_room = move(exits, command_input)
        in_room = current_room["name_ID"]

# NEW
# NEW
# NEW

# def exit_leads_to(exits, direction):
#     """This function takes a dictionary of exits and a direction (a particular
#     exit taken from this dictionary). It returns the name of the room into which
#     this exit leads. For example:
#
#     >>> exit_leads_to(rooms["Reception"]["exits"], "south")
#     "MJ and Simon's room"
#     >>> exit_leads_to(rooms["Reception"]["exits"], "east")
#     "your personal tutor's office"
#     >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
#     'Reception'
#     """
#     return rooms[exits[direction]]["name"]
#
#
# def print_exit(direction, leads_to):
#     """This function prints a line of a menu of exits. It takes a direction (the
#     name of an exit) and the name of the room into which it leads (leads_to),
#     and should print a menu line in the following format:
#
#     GO <EXIT NAME UPPERCASE> to <where it leads>.
#
#     For example:
#     >>> print_exit("east", "you personal tutor's office")
#     GO EAST to you personal tutor's office.
#     >>> print_exit("south", "MJ and Simon's room")
#     GO SOUTH to MJ and Simon's room.
#     """
#     print("GO " + direction.upper() + " to " + leads_to + ".")
#
#
# def print_menu(exits, room_items, inv_items):
#     """This function displays the menu of available actions to the player. The
#     argument exits is a dictionary of exits as exemplified in map.py. The
#     arguments room_items and inv_items are the items lying around in the room
#     and carried by the player respectively. The menu should, for each exit,
#     call the function print_exit() to print the information about each exit in
#     the appropriate format. The room into which an exit leads is obtained
#     using the function exit_leads_to(). Then, it should print a list of commands
#     related to items: for each item in the room print
#
#     "TAKE <ITEM ID> to take <item name>."
#
#     and for each item in the inventory print
#
#     "DROP <ITEM ID> to drop <item name>."
#
#     For example, the menu of actions available at the Reception may look like this:
#
#     You can:
#     GO EAST to your personal tutor's office.
#     GO WEST to the parking lot.
#     GO SOUTH to MJ and Simon's room.
#     TAKE BISCUITS to take a pack of biscuits.
#     TAKE HANDBOOK to take a student handbook.
#     DROP ID to drop your id card.
#     DROP LAPTOP to drop your laptop.
#     DROP MONEY to drop your money.
#     What do you want to do?
#
#     """
#     print("You can:")
#     # Iterate over available exits
#     for direction in exits:
#         # Print the exit name and where it leads to
#         print_exit(direction, exit_leads_to(exits, direction))
#
#     #
#     # COMPLETE ME!
#     #
#
#     print("What do you want to do?")
#
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
#
#
# def move(exits, direction):
#     """This function returns the room into which the player will move if, from a
#     dictionary "exits" of avaiable exits, they choose to move towards the exit
#     with the name given by "direction". For example:
#
#     >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
#     True
#     >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
#     True
#     >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
#     False
#     """
#
#     # Next room to go to
#     return rooms[exits[direction]]
#
#
# # This is the entry point of our program
# def main():
#
#     # Main game loop
#     while True:
#         # Display game status (room description, inventory etc.)
#         print_room(current_room)
#         print_inventory_items(inventory)
#
#         # Show the menu with possible actions and ask the player
#         command = menu(current_room["exits"], current_room["items"], inventory)
#
#         # Execute the player's command
#         # execute_command(command)

main()
