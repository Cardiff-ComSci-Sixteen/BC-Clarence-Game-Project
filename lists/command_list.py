from lists.feedback_lists import *
# from room_states import rooms_states
import string
from map import rooms
from items.items import *
import player
import json

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


# Asks user to press anything to continue.
def enter():
    input("\nPress ENTER to continue.\n")


# Combines the user's input keywords into one variable to be parsed to the commands themselves
def input_combine(cmd):
    if len(cmd) < 3:
        pass
    elif len(cmd) >= 5:
        cmd_combined = cmd[1] + "_" + cmd[2] + "_" + cmd[3] + "_" + cmd[4]
        del cmd[1:len(cmd) - 1]
        cmd[1] = cmd_combined
    elif len(cmd) >= 4:
        cmd_combined = cmd[1] + "_" + cmd[2] + "_" + cmd[3]
        del cmd[1:len(cmd) - 1]
        cmd[1] = cmd_combined
    elif len(cmd) >= 3:
        cmd_combined = cmd[1] + "_" + cmd[2]
        del cmd[1:len(cmd) - 1]
        cmd[1] = cmd_combined
    return cmd


def input_combine_commands(cmd):
    if len(cmd) < 2:
        pass
    elif len(cmd) >= 4:
        cmd_combined = cmd[0] + "_" + cmd[1] + "_" + cmd[2] + "_" + cmd[3]
        del cmd[0:len(cmd) - 1]
        cmd[0] = cmd_combined
    elif len(cmd) >= 3:
        cmd_combined = cmd[0] + "_" + cmd[1] + "_" + cmd[2]
        del cmd[0:len(cmd) - 1]
        cmd[0] = cmd_combined
    elif len(cmd) >= 2:
        cmd_combined = cmd[0] + "_" + cmd[1]
        del cmd[0:len(cmd) - 1]
        cmd[0] = cmd_combined
    return cmd


def input_hang(user_input, feed):
    while True:
        if str(user_input).strip() == "":
            user_input = input(player.player_name + ": ")
        else:
            user_input = input(feed + ": ")
        if str(user_input).strip() == "":
            pass
        else:
            user_input = user_input.lower()
            cmd = user_input
            cmd = normalise_input(cmd)
            if cmd:
                return cmd
            else:
                cmd = ["null"]
                return cmd


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


def exit_leads_to(exits, direction):
    if direction not in exits:
        return 0
    return exits[direction]


def print_menu_line(leads_to):
    if leads_to == 0:
        return 0
    else:
        return leads_to


def print_menu(exits):
    print("\n┌-----┐")
    print("╣EXITS│")
    print("└-----┘")
    exit_list = []
    for ch in rooms[player.in_room]["exits"]:
        if ch not in exits:
            pass
        else:
            exit_list.append(ch)
            print(print_menu_line(rooms[exit_leads_to(exits, ch)]["name"]))
    return exit_list


# Actually returns the direction.
def command_go(exits, direction):
    while True:
        if direction == "back":
            direction = normalise_input(player.last_room)
            if len(direction) > 1:
                cmd_changed = direction[0] + "_" + direction[1]
                del direction[0:len(direction)-1]
                direction[0] = cmd_changed
            return direction[0]
        else:
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
            if cmd[0] == "go" or cmd[0] == "back" or cmd[0] in rooms[in_room]["exits"]:
                if len(cmd) > 1:
                    direction = command_go(exits, cmd[1])
                    if direction in rooms[in_room]["exits"]:
                        return direction
                    elif cmd[1] == "back":
                        print("I cannot go back.")
                    break
                elif cmd[0] in rooms[in_room]["exits"] or cmd[0] == "back":
                    direction = command_go(exits, cmd[0])
                    if direction in rooms[in_room]["exits"]:
                        return direction
                    elif cmd[0] == "back":
                        print("I cannot go back.")
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
            print(str(a).upper().ljust(12, " ") + commands[a])
    elif "help" in user_input and "detail" in user_input:
        print("\nList of available commands:\n")
        for a in commands_detailed:
            # print((len(a)+1) * "-" + "|")
            print(str(a).upper().ljust(12, " ") + commands_detailed[a])


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


# Make user get prompted with a text based on their reaction (kjkafjajf - it hs to be (yes/no)

def command_take(player_name, room, item, inventory):
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
                        input_combine_commands(item)
                        break
                    else:
                        input_combine_commands(item)
                        break
        elif len(item) > 0:
            for a in rooms[room]["items"]:
                for id_index in a["id"]:
                    if id_index in item:
                        for inventory_item in inventory:
                            if "suit" in a["id"] and "suit" in inventory_item["id"]:
                                print("You cannot wear more armor - you have to remove the current one first!")
                                return
                        if a["weight"] + player.weight <= 100:
                            rooms[room]["items"].remove(a)
                            inventory.append(a)
                            print("You have taken " + a["name"] + "!")
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


def command_drop(player_name, room, item, inventory):
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
                        input_combine_commands(item)
                        break
                    else:
                        input_combine_commands(item)
                        break
        elif len(item) > 0:
            if "bass" in item:
                if item_bass in inventory:
                    inventory.remove(item_bass)
                print("You just dropped the bass!")
                return
            for a in inventory:
                for id_index in a["id"]:
                    if id_index in item:
                        inventory.remove(a)
                        rooms[room]["items"].append(a)
                        b = str(a["name"] + " dropped!")
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


def command_stats(room, inventory):
    print()
    print("Name: " + player.player_name)
    print("Health: " + str(player.hp))
    print("Weight: " + str(player.weight) + " space units")
    print("Items: " + str(len(inventory)))
    print("Room: " + room)
    print("Score: " + str(player.score))
    print("Armor: " + str(player.armor))


def item_class(item):
    if item == 0:
        return "Misc"
    if item == 1:
        return "Weapon"
    if item == 2:
        return "Armor"
    if item == 3:
        return "Consumable"
    if item == 4:
        return "Key"
    if item == 5:
        return "Objective Item"


# The main logic through which objects (elements) are inspected.
# If an unknown element is requested to be inspected, the function will return a deny message.
def command_scan(room, element, player_name, container):
    while True:
        if len(element) > 0:
            if "objects" in room:
                pass
            else:
                print("DEBUG_NOTICE: 'objects' dict Key not in " + room["name_ID"])
                break
            if len(element) > 1:
                    element[0] = str(element[0]) + "_" + str(element[1])
                    element = element[:1]
            for item in room["objects"]:
                for id_index in item["id"]:
                    if id_index in element:
                        if "description_scan" not in item:
                            a = random.randint(0, 2)
                            print(scanner_deny[a])
                            return 1
                        print()
                        print(item["description_scan"])
                        return 1
            for item in room["items"]:
                for id_index in item["id"]:
                    if id_index in element:
                        if "description_scan" not in item:
                            a = random.randint(0, 2)
                            print(scanner_deny[a])
                            return 1
                        print()
                        print(item["description_scan"])
                        return 1
            for item in container:
                for id_index in item["id"]:
                    if id_index in element:
                        if "description_scan" not in item:
                            a = random.randint(0, 2)
                            print(scanner_deny[a])
                            return 1
                        print()
                        print(item["description_scan"])
                        return 1
            print("I'm afraid I cannot scan that.")
            break
        elif len(element) == 0:
            if item_scanner in container:
                print("What do you want to scan?")
                while True:
                    element = input(player_name + ": ")
                    if len(element) == 0:
                        pass
                    else:
                        element = normalise_input(element)
                        if "scan" in element:
                            element.remove("scan")
                            input_combine_commands(element)
                            break
                        else:
                            for alpha in commands_aliases:
                                if alpha in element:
                                    element.remove(alpha)
                            input_combine_commands(element)
                            break
            else:
                print("I need something to scan this with!")
                break


def command_inspect(room, element, player_name, container):
    while True:
            if len(element) > 0:
                if "item" in element:
                    element.remove("item")
                if "items" in room:
                    pass
                else:
                    print("DEBUG_NOTICE: 'items' dict Key not in " + room["name_ID"])
                    break
                if "room_items" in element:
                    print_room_items(room)
                    break
                if "room" in element:
                    print("\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n")
                    print_room_items(room)
                    break
                if len(element) > 1:
                    element[0] = str(element[0]) + "_" + str(element[1])
                    element = element[:1]
                if element[0] == "inventory":
                    command_inventory(container)
                    break
                for item in room["objects"]:
                    for id_index in item["id"]:
                        if id_index in element:
                            print(item["name"] + ":")
                            print(item["description"])
                            return
                for alpha in room["items"]:
                    for id_index in alpha["id"]:
                        if id_index in element:
                            print()
                            print("Class: " + item_class(alpha["class"]))
                            print(alpha["description"])
                            return
                for bravo in container:
                    for id_index_1 in bravo["id"]:
                        if id_index_1 == "scanner":
                            print()
                            print("Class: " + item_class(bravo["class"]))
                            print(bravo["description"])
                            print("Power: " + str(bravo["attributes"]["power"]) + "%")
                            return
                        if id_index_1 in element:
                            print()
                            print("Class: " + item_class(bravo["class"]))
                            print(bravo["description"])
                            return
                else:
                    print("I can't inspect this.")
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
                            input_combine_commands(element)
                            break
                        else:
                            for alpha in commands_aliases:
                                if alpha in element:
                                    element.remove(alpha)
                            input_combine_commands(element)
                            break
# Function gets the current state of the room.


def command_inventory(container):
    # This function takes a list of inventory items and displays it nicely, in a
    # manner similar to print_room_items(). The only difference is in formatting:
    if list_of_items(container):
        print("I am carrying " + list_of_items(container) + ".")
    else:
        print("I don't have anything on me at the moment.")


def get_room_state(room):
    n = room["state"]
    return n


def update_player_stats(inventory):
    player.weight = 0
    player.armor = 0
    for item in inventory:
        player.weight = player.weight + item["weight"]
        if item["class"] == 2:
            player.armor = player.armor + item["attributes"]["armor"]


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
    # to produce a comma-separated list of item names."""

    room_items = []
    for item in room["items"]:
        room_items.append(item)
    if room_items:
        print("There is " + list_of_items(room_items) + " here.")
    else:
        print("There is no special item in the room.")


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

# Class that is raised whenever the player is dead.
class GameOver(Exception):
    pass
# Tells player what's next after they died.
def game_over_prompt():
    print()
    print("╔═══════════╗")
    print("╣ GAME OVER ║")
    print("╚═══════════╝")
    print()
    input("Press ENTER to quit the game.")
    quit()
    # user_input = input("Type 'quit' to exit game or 'new' to start a new game: ")
    # while True:
    #     if user_input.strip() == "quit":
    #         return "quit"
    #     elif user_input.strip() == "new":
    #         return "new"
    #     else:
    #         user_input = input("Type 'quit' or 'new': ")
# Write player and room data into save file.
def save():
    data = {
        "player_name": player.player_name,
        "hp": player.hp,
        "weight": player.weight,
        "inventory": player.inventory,
        "score": player.score,
        "armor": player.armor,
        "is_naked": player.is_naked,
        "last_room": player.last_room,
        "current_room": player.current_room,
        "in_room": player.in_room,
        "in_battle_enemy_hp": player.in_battle_enemy_hp
    }
    for key, value in rooms.items():
        data[key] = value
    with open("data.json", "w") as f:
        json.dump(data, f)
# Checks if save file exists in directory. Returns True if it exists.
def save_exists():
    try:
        with open("data.json") as file:
            return True
    except IOError as e:
        return False
# Prompts player if they want to continue from save, start a new game or quit at the beginning.
def continue_from_save():
    print()
    print("Do you want to start a 'New Game' or 'Continue' from save file?")
    print("1. New Game")
    print("2. Continue")
    print("3. Quit")
    while True:
        a = input().strip()
        if a == "1":
            return False
        elif a == "2":
            return True
        elif a == "3":
            quit()
        else:
            print("You need to enter 1 or 2!")
# Loads data from save file.
def load():
    with open("data.json", "r") as f:
        data = json.load(f)
        player.player_name = data["player_name"]
        player.hp = data["hp"]
        player.weight = data["weight"]
        player.inventory = list(data["inventory"])
        for a in player.inventory:
            print(a["name"])
        player.score = data["score"]
        player.armor = data["armor"]
        player.is_naked = data["is_naked"]
        player.last_room = data["last_room"]
        player.current_room = data["current_room"]
        player.in_room = data["in_room"]
        player.in_battle_enemy_hp = data["in_battle_enemy_hp"]
        b = 0
        for key, value in data.items():
            if key in rooms:
                rooms[key] = value
                print("Room " + key + " updated!")