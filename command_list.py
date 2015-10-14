from feedback_lists import *
from room_states import rooms_states
import string
from player import inventory
from map import rooms
from objects import *
import player

# List of directions for the functions to check against.
# Directions such as UP and DOWN could be used later.
dire = ["east", "west", "north", "south"]

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'and', 'another', 'any', 'around', 'at', 'are',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'there', 'this', 'those', 'through', 'till', 'to',
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
        while True:
            if word in words:
                words.remove(word)
            else:
                break
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
    # user_input = normalise_input(user_input)
    if user_input in exits:
        return True
    else:
        return False


# Actually returns the direction.
def command_go(exits, direction):
    while True:
        if is_valid_exit(exits, direction):
            return direction
        else:
            cmd = random.randint(0, 3)
            print(go_deny[cmd])
            break


# Holds the logic of input and different types of direction addressing.
def command_go_superior(exits, in_room, cmd):
    while True:
        if len(cmd):
            if cmd[0] == "go" or cmd[0] in rooms[in_room]["exits"]:
                if len(cmd) > 1:
                    direction = command_go(exits, cmd[1])
                    if direction in rooms[in_room]["exits"]:
                        return direction
                    break
                elif cmd[0] in rooms[in_room]["exits"]:
                    direction = command_go(exits, cmd[0])
                    if direction in rooms[in_room]["exits"]:
                        return direction
                    break
                else:
                    while True:
                        cmd = input("Go where? ")
                        cmd = normalise_input(cmd)
                        if len(cmd) > 1:
                            if cmd[0] == "go" and len(cmd) > 2:
                                cmd_changed = cmd[1] + "_" + cmd[2]
                                del cmd[0:len(cmd)-1]
                                cmd[0] = cmd_changed
                                break
                            else:
                                cmd_changed = cmd[0] + "_" + cmd[1]
                                del cmd[0:len(cmd)-1]
                                cmd[0] = cmd_changed
                                break
                        if len(cmd) == 1:
                            break
            elif len(cmd):
                print("I did not quite get that.")
                # return cmd
                break
        else:
            break


def command_help(user_input):
    if "help" in user_input and "detailed" not in user_input:
        print("\nList of available commands:\n")
        for a in commands:
            print(str(a).upper() + " - " + commands[a])
    elif "help" in user_input and "detail" in user_input:
        print("\nList of available commands:\n")
        for a in commands_detailed:
            print(len(a) * "=")
            print(str(a).upper() + " - " + commands_detailed[a])


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


def command_take(player_name, room, item):
    while True:
        if len(item) == 0 or (item[0] == "take" and len(item) == 1):
            print("What do you want me to take?")
            while True:
                item = input(player_name + ": ")
                if len(item) == 0:
                    pass
                else:
                    item = normalise_input(item)
                    if "take" in item:
                        item.remove("take")
                        break
                    else:
                        break
        elif len(item) > 0:
            for a in rooms[room]["items"]:
                if a["id"] in item:
                    if a["weight"] + player.weight <= 100:
                        rooms[room]["items"].remove(a)
                        inventory.append(a)
                        print("You have taken " + a["id"] + "!")
                        return
                    else:
                        print("Taking this item will make me too heavy!")
                        return
            if "bass" in item:
                inventory.append(item_bass)
                print("Well, you just put some bass in your pocket!")
                return
            i = random.randint(0, len(take_deny) - 1)
            print(take_deny[i])
            break


def command_drop(player_name, room, item):
    while True:
        if len(item) == 0 or (item[0] == "drop" and len(item) == 1):
            print("What do you want me to drop?")
            while True:
                item = input(player_name + ": ")
                if len(item) == 0:
                    pass
                else:
                    item = normalise_input(item)
                    if "drop" in item:
                        item.remove("drop")
                        break
                    else:
                        break
        elif len(item) > 0:
            if "bass" in item:
                if item_bass in inventory:
                    inventory.remove(item_bass)
                print("You just dropped the bass!")
                return
            for a in inventory:
                if a["id"] in item:
                    inventory.remove(a)
                    rooms[room]["items"].append(a)
                    b = str(a["id"] + " dropped!")
                    print(b[0].upper() + b[1:])
                    return
            if "everything" in item or "all" in item:
                while True:
                    if len(inventory) > 0:
                        for item_a in inventory:
                            inventory.remove(item_a)
                            rooms[room]["items"].append(item_a)
                            break
                    else:
                        print("I dropped everything!")
                        break
                return

            i = random.randint(0, len(drop_deny) - 1)
            print(drop_deny[i])
            break


def command_stats(room):
    print()
    print("Name: " + player.player_name)
    print("Health: " + str(player.hp))
    print("Weight: " + str(player.weight) + " space units")
    print("Items: " + str(len(inventory)))
    print("Room: " + room)


# The main logic through which objects (elements) are inspected.
# If an unknown element is requested to be inspected, the function will return a deny message.
def scan_element(room, element, player_name, inventory):
    while True:
        if len(element) > 0:
            if "objects" in room:
                pass
            else:
                print("DEBUG_NOTICE: 'objects' dict Key not in " + room["name_ID"])
                break
            if element[0] in room["objects"] and item_scanner in inventory:
                print("\n" + element[0][0].upper() + str(element[0][1:len(element[0])] + ":"))
                print(room["objects"][element[0]][0])
                break
            elif "room" in element or "rooms" in element:
                if "items" in element:
                    print_room_items(room)
                    break
                else:
                    print("\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n")
                    print_room_items(room)
                    break
            elif element[0] == "inventory":
                command_inventory(inventory)
                break
            elif item_scanner not in inventory:
                print("I need something to scan this with!")
                break
            elif ("item_" + str(element[0])) in inventory:
                print("\n" + element[0][0].upper() + str(element[0][1:len(element[0])] + ":"))
                print(["item_" + str(element[0])]["description"])
            else:
                print("I'm afraid I cannot scan that.")
                break
        elif len(element) == 0:
            print("What do you want to scan?")
            while True:
                element = input(player_name + ": ")
                if len(element) == 0:
                    pass
                else:
                    element = normalise_input(element)
                    if "scan" in element:
                        element.remove("scan")
                        break
                    else:
                        for alpha in commands_aliases:
                            if alpha in element:
                                element.remove(alpha)
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


def command_inventory(inventory):
    # This function takes a list of inventory items and displays it nicely, in a
    # manner similar to print_room_items(). The only difference is in formatting:
    print("I am carrying " + list_of_items(inventory) + ".")


def list_of_items(items):
    # This function takes a list of items (see items.py for the definition) and
    # returns a comma-separated list of item names (as a string). For example:

    item_names = []
    alpha = ""
    for item in items:
        item_names.append(item["name"])
    for item in item_names:
        if len(item_names) == 1:
            alpha = item[0:2] + item
        elif item == item_names[len(item_names) - 1]:
            alpha = alpha[:len(alpha)] + " and " + item
        else:
            alpha = alpha + ", " + item
    alpha = alpha[2:len(alpha)]
    return alpha


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
        print("There is " + list_of_items(room_items) + " here.")
    else:
        print("There is no special item in the room.")


def update_player_stats():
    player.weight = 0
    for item in inventory:
        player.weight = player.weight + item["weight"]


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