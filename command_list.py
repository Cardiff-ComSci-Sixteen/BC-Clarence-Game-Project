from feedback_lists import *
# This import will be needed when the 'debug' import is removed
from room_states import rooms_states
from map import rooms
# from parser import *
import string
import random
# from debug import *

# List of directions for the functions to check against.
# Directions such as UP and DOWN could be used later.
dire = ["east", "west", "north", "south"]

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


# Turns all input to a simple string of ONLY lowercase letters.
def normalise_input(user_input):
    """
    >>> normalise_input("Norm4lize this!")
    'normlizethis'
    """
    text = remove_punct(user_input)
    text = text.lower()
    text = text.split()
    text = filter_words(text, skip_words)
    return text


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:

    >>> filter_words(["help", "me", "please"], ["me", "please"])
    ['help']

    >>> filter_words(["go", "south"], skip_words)
    ['go', 'south']

    >>> filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], skip_words)
    ['go', 'passage', 'south']

    """
    pass
    for word in skip_words:
        if word in words:
            words.remove(word)
    return words


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, "")

    return text


# Checks if chosen exit is valid
# (is there an exit to the west or no when you type in 'west')?
def is_valid_exit(exits, user_input):
    if user_input in exits:
        return True
    else:
        return False


def command_go(exits, direction):
    list_deny = ["Going " + direction.upper() + " is not an option.",
                 "I cannot go " + direction.upper() + ".",
                 "Walking " + direction.upper() + " is impossible!",
                 "Something is blocking my path."]
    while True:
        if is_valid_exit(exits, direction):
            return direction
        else:
            cmd = random.randint(0, 3)
            print(list_deny[cmd])
            break


def command_help():
    print("\nList of available commands:\n")
    for a in commands:
        print(str(a).upper() + " - " + commands[a])


# When used, asks for player input and changes the player's name based on that input.
# Currently max characters is set to 12 (to keep things tidy).
def command_name_change():
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
        if len(element) > 0:
            if "objects" in room:
                pass
            else:
                print("DEBUG_NOTICE: 'objects' dict Key not in " + room["name_ID"])
                break
            if element[0] in room["objects"]:
                print("\n" + element[0][0].upper() + str(element[0][1:len(element[0])] + ":"))
                print(room["objects"][element[0]][0])
                break
            elif element[0] == "room":
                print("\n\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n")
                break
            else:
                print("I'm afraid I cannot inspect that.")
                break
        elif len(element) == 0:
            print("What do you want to inspect?")
            while True:
                element = input(player_name + ": ")
                if len(element) == 0:
                    pass
                else:
                    element = normalise_input(element)
                    if "inspect" in element:
                        element.remove("inspect")
                        break
                    else:
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
# Function returns errors IF:
# 1. "description" is not present under room_states (room_states.py)
# 2. "objects" is not present in room information (map.py)
def update_room_state(room):
    current_state = get_room_state(rooms_states[room])
    # Makes the actual changes based on the current room state.
    rooms[room]["description"] = rooms_states[room]["state_" + str(current_state)]["description"]
    for item in rooms[room]["objects"]:
        rooms[room]["objects"][item][0] = rooms_states[room]["state_" + str(current_state)]["objects"][item]

# NEW
# NEW
# NEW
#
# def execute_take(item_id):
#     """This function takes an item_id as an argument and moves this item from the
#     list of items in the current room to the player's inventory. However, if
#     there is no such item in the room, this function prints
#     "You cannot take that."
#     """
#     pass
#
#
# def execute_drop(item_id):
#     """This function takes an item_id as an argument and moves this item from the
#     player's inventory to list of items in the current room. However, if there is
#     no such item in the inventory, this function prints "You cannot drop that."
#     """
#     pass


def list_of_items(items):
    # This function takes a list of items (see items.py for the definition) and
    # returns a comma-separated list of item names (as a string). For example:

    item_names = []
    alpha = ""
    for item in items:
        item_names.append(item["name"])
    for item in item_names:
        alpha = alpha + ", " + item
    alpha = alpha[2:len(alpha)]
    return alpha


def print_inventory_items(items):
    # This function takes a list of inventory items and displays it nicely, in a
    # manner similar to print_room_items(). The only difference is in formatting:

    print("You have " + list_of_items(items) + ".\n")


def print_room_items(room):
    # """This function takes a room as an input and nicely displays a list of items
    # found in this room (followed by a blank line). If there are no items in
    # the room, nothing is printed. See map.py for the definition of a room, and
    # items.py for the definition of an item. This function uses list_of_items()
    # to produce a comma-separated list of item names.

    room_items = []
    for item in room["items"]:
        room_items.append(item)
    if room_items:
        print("There is " + list_of_items(room_items) + " here.\n")


def print_room(room):
    # This function takes a room as an input and nicely displays its name
    # and description. The room argument is a dictionary with entries "name",
    # "description" etc. (see map.py for the definition). The name of the room
    # is printed in all capitals and framed by blank lines. Then follows the
    # description of the room and a blank line again. If there are any items
    # in the room, the list of items is printed next followed by a blank line
    # (use print_room_items() for this)

    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)