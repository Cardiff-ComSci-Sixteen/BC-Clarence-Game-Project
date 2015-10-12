from room_states import get_room_state
import random
from command_list import *
import string

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
    print("\n\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n\n")


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


def menu(exits):
    print_menu(exits)
    global player_name
    user_input = "a"
    while True:
        if user_input == "":
            user_input = input(player_name + ": ")
        else:
            user_input = input("\n" + player_name + ": ")
        user_input = normalise_input(user_input)
        user_input = user_input.replace("go", "")
        list_deny = ["Going " + user_input.upper() + " is not an option.",
                     "I cannot go " + user_input.upper() + ".",
                     "Walking " + user_input.upper() + " is impossible!",
                     "Something is blocking my path."]

        if is_valid_command(user_input) or "inspect" in user_input:
            a = user_input

            if command_direction(exits, a) == 1:
                return a
            elif command_direction(exits, a) == 2:
                a = random.randint(0, 3)
                print(list_deny[a])
            if a == "playername":
                player_name = player_name_change()
            if a == "exits":
                print_menu(exits)
            if a == "help":
                help_menu()
            if a == "quit":
                quit()
            if str(a).find("inspect") >= 0:
                inspect_element(rooms[in_room], a.replace("inspect", ""), player_name)

        elif user_input == "":
            pass
        else:
            i = random.randint(0, len(command_unknown) - 1)
            print(command_unknown[i])


def move(exits, direction):
    return rooms[exits[direction]]


def main():
    # Start game at the room_1
    current_room = rooms["needs_name1"]
    print("Type 'help' to see list of available commands.")
    global in_room
    # Main game loop
    while True:
        display_room(current_room)

        exits = current_room["exits"]

        command_input = menu(exits)
        if command_input == "south" and get_room_state(rooms_states["room_1"]) == 1:
            change_room_desc(current_room, 3)

        current_room = move(exits, command_input)
        in_room = current_room["name_ID"]


main()
