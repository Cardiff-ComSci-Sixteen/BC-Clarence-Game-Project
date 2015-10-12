from feedback_lists import *

# This import will be needed when the 'debug' import is removed
from room_states import rooms_states

from map import rooms
import string
# from debug import *

# List of directions for the functions to check against.
# Directions such as UP and DOWN could be used later.
dire = ["east", "west", "north", "south"]


# Turns all input to a simple string of ONLY lowercase letters.
def normalise_input(text):
    """
    >>> normalise_input("Norm4lize this!")
    'normlizethis'
    """
    text = text.lower()
    for punct in string.punctuation:
            text = text.replace(punct, "")
    for digit in string.digits:
            text = text.replace(digit, "")
    text = text.replace(" ", "")
    return text


# Checks if chosen exit is valid
# (is there an exit to the west or no when you type in 'west')?
def is_valid_exit(exits, user_input):
    if user_input in exits:
        return True
    else:
        return False


# Function checks if the user input is a command for direction.
# Returns 1 if exit is valid, 2 if direction is not an exit, 3 all else
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


# Prints a list of possible commands to the player
def help_menu():
    print("\nList of available commands:\n")
    for a in commands:
        print(str(a).upper() + " - " + commands[a])


# When used, asks for player input and changes the player's name based on that input.
# Currently max characters is set to 12 (to keep things tidy).
def player_name_change():
    user_input = input("Type your new name: ")
    while True:
        if len(user_input) > 12:
            print("Your name should be 12 characters or less!")
            user_input = input("Type a player name: ")
        else:
            break
    return user_input


# The main logic through which objects (elements) are inspected.
# If an unknown element is requested to be inspected, the function will return a deny message.
def inspect_element(room, element, player_name):
    while True:
        element = normalise_input(element)
        if "objects" in room:
            pass
        else:
            print("DEBUG_NOTICE: 'objects' dict Key not in " + room["name_ID"])
            break
        if element in room["objects"]:
            print("\n" + element[0].upper() + element[1:len(element)] + ":")
            print(room["objects"][element][0])
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


# Function gets the current state of the room.
def get_room_state(room):
    n = room["state"]
    return n


# Function changes the room state depending on input
def change_room_state(room, index):
    rooms_states[room]["state"] = index
    a = rooms_states[room]["state"]
    return a


# Checks the current state of the room and initializes its contents depending on that
# every time the main() function is ran. Objects will also be initialized.
def update_room_state(room):
    current_state = get_room_state(rooms_states[room])
    # Makes the actual changes based on the current room state.
    rooms[room]["description"] = rooms_states[room]["state_" + str(current_state)]["description"]
    for item in rooms[room]["objects"]:
        rooms[room]["objects"][item][0] = rooms_states[room]["state_" + str(current_state)]["objects"][item]