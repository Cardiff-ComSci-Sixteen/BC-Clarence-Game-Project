from feedback_lists import *
from map import rooms
from room_states import change_room_state
from room_states import change_description
from room_states import rooms_states

# List of direction to check against.
dire = ["east", "west", "north", "south"]


# This function, when addressed, will change the room descriptions based on the room's current state (see room_states for more info)
def change_room_desc(current_room, index):
    change_room_state(current_room["name_ID"], index)

    # Gets the new description as a string.
    a = rooms_states["Reception"]["state_" + str(change_description("Reception"))]["description"]
    b = rooms_states["Reception"]["state_" + str(change_description("Reception"))]["objects"]

    # Changes the current description of the room to the new one.
    current_room["description"] = a
    current_room["objects"] = b

# Turns all input to a simple string of ONLY lowercase letters.
def normalise_input(text):
    text = text.lower()
    text_new = ""
    for ch in text:
        if ch in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}:
            text_new = text_new + ch
    return text_new

# Checks if chosen exit is valid (is there an exit to the west or no when you type in 'exit')?
def is_valid_exit(exits, user_input):
    if user_input in exits:
        return True
    else:
        return False

# Function checks if the user input is a command for direction. Returns 1 if exit is valid, 2 if direction is not an exit, 3 all else
def command_direction(exits, user_input):
    while True:
        if is_valid_exit(exits, user_input):
            return 1
            break
        else:
            if user_input in dire:
                return 2
            else:
                return 3

# Prints a list of possible commands
def help_menu():
    print("\nList of available commands:\n")
    for a in commands:
        print(str(a).upper() + " - " + commands[a])

# Changes and returns new player name
def player_name_change():
    user_input = input("Type your new name: ")
    return user_input

# The way elements are inspected and outputs if element is not present (has debug for new rooms)
def inspect_element(room, element, player_name):
    while True:
        element = normalise_input(element)
        if "objects" in room:
            pass
        else:
            print("DEBUG_NOTICE: 'objects' not in " + room["name_ID"])
            break
        if element in room["objects"]:
            print("\n" + element[0].upper() + element[1:len(element)] + ":")
            print(room["objects"][element])
            break
        elif element == "":
            element = input("What do you want to inspect?\n" + player_name + ": ")
            element = element.replace("inspect", "")
        elif element == "room":
            print("\n\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n\n")
            break
        else:
            print("I'm afraid I cannot inspect that.")
            break