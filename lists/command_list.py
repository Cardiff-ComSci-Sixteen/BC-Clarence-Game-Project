# from room_states import rooms_states
import string
import json
import os
from lists.use import *

# List of directions for the functions to check against.
# Directions such as UP and DOWN could be used later.
dire = ["east", "west", "north", "south"]

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'and', 'another', 'any', 'around', 'at', 'are',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'show', 'small', 'some', 'soon',
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


def exit_leads_to(exits, direction):
    if direction not in exits:
        return 0
    return exits[direction]


def print_menu_line(leads_to):
    if leads_to == 0:
        return 0
    else:
        return leads_to

def display_room(room):
    # CMD Version
    print("\n╗ ┌" + (len(room["name"]) * "─") + "┐")
    print("╠═╣" + room["name"].upper() + "│")
    print("╝ └" + str(len(room["name"]) * "─") + "┘")

    # Normal Version
    # print("\n    ╗┌" + (len(room["name"]) * "-") + "┐╔ ")
    # print("    ╠╣" + room["name"].upper() + "╠╣")
    # print("    ╝└" + str(len(room["name"]) * "-") + "┘╚ ")

    print("\n" + room["description"] + "\n")
    print_room_items(room)


def print_menu(exits):
    print("\n╗ ┌─────┐")
    print("╠═╣EXITS│")
    print("╝ └─────┘")
    exit_list = []
    for ch in sorted(rooms[player.in_room]["exits"]):
        if ch not in exits:
            pass
        else:
            exit_list.append(ch)
            print(print_menu_line(rooms[exit_leads_to(exits, ch)]["name"]))
    return exit_list


# Checks if chosen exit is valid
# (is there an exit to the west or no when you type in 'west')?
def is_valid_exit(exits, user_input):
    if user_input in exits:
        alpha = exits[user_input]
        if "requirement" in rooms[alpha]:
            if len(rooms[alpha]["requirement"]) > 0:
                return 2
            else:
                return 1
        else:
            return 1
    else:
        return 0


# Actually returns the direction.
def command_go(exits, direction):
    global went_back
    went_back = 0
    while True:
        if direction == "back":
            went_back = 1
            if player.last_room:
                direction = player.last_room[len(player.last_room) - 1]
                if len(direction) > 1:
                    cmd_changed = direction[0] + "_" + direction[1]
                    direction = cmd_changed
                else:
                    direction = direction[0]
            else:
                print("There is nowhere to go back!")
                break
        else:
            chosen_exit = is_valid_exit(exits, direction)
            if chosen_exit == 1:
                if went_back == 0:
                    player.last_room.append(normalise_input(player.current_room["name_ID"]))
                else:
                    del player.last_room[len(player.last_room) - 1]
                return direction
            elif chosen_exit == 2:
                if direction == "bridge":
                    print("The doors are jammed. I need something to use to break them apart with!")
                if direction == "armory" or direction == "power_control" or direction == "detention_centre":
                    print("The doors are locked - I need to use a key card to enter the room!")
                break
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
                    break
                elif cmd[0] in rooms[in_room]["exits"] or cmd[0] == "back":
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


def command_objectives():
    if player.objectives_changed == 1:
        print("OBJECTIVES UPDATED:")
        player.objectives_changed = 0
    else:
        print("OBJECTIVES:")
    for key, value in player.objectives.items():
        print(" - " + value)


def use(item):
    if item == item_crowbar and (player.current_room["name_ID"] == "Systems Control" or player.current_room["name_ID"] == "Officer Deck"):
        use_crowbar()
        return True
    elif item == item_keyA and player.current_room["name_ID"] == "Weapons Control":
        use_keyA()
        return True
    elif item == item_keyD and player.current_room["name_ID"] == "Crew Quarters":
        use_keyD()
        return True
    elif item == item_keyP and player.current_room["name_ID"] == "Power Generator":
        use_keyP()
        return True
    elif item == item_medkit:
        use_medkit()
        return True
    elif item == item_biscuits:
        use_biscuits()
        return True
    return False


def command_use(user_input, inventory):
    item = user_input
    while True:
        if len(item) == 0 or (item[0] == "use" and len(item) == 1):
            print("What do you want me to use?")
            while True:
                item = input(player.player_name + ": ")
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
            if "use" in item:
                item.remove("use")
            a = 0
            for inv_item in inventory:
                if item[0] in inv_item["id"]:
                    a = 1
                    if use(inv_item):
                        return
            if a == 1:
                print("I cannot use this item here.")
            else:
                i = random.randint(0, len(use_deny) - 1)
                print(use_deny[i])
            break

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
    print("Score: " + str(player.score) + " bits")
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
                    display_room(room)
                    print_menu(room["exits"])
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
                            print()
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
                            print("Power: " + str(player.scanner_power) + "%")
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


def quit_test(text):
    if "quit" in text:
        quit()

# Class that is raised whenever the player is dead.
class GameOver(Exception):
    pass
# Similar to GameOver
class Victory(Exception):
    pass

# Tells player what's next after they died.
def game_over_prompt():
    print("     _____                                     _____                             ")
    print("  __|___  |__  ____    ____    __  ______   __|__   |__  __    _ ______  _____   ")
    print(" |   ___|    ||    \  |    \  /  ||   ___| /     \     |\  \  //|   ___||     |  ")
    print(" |   |  |    ||     \ |     \/   ||   ___| |     |     | \  \// |   ___||     \  ")
    print(" |______|  __||__|\__\|__/\__/|__||______| \_____/   __|  \__/  |______||__|\__\ ")
    print("    |_____|                                   |_____|                            ")
    print()
    print("You have died... Congratulations!")
    print()
    print("Your score is: " + str(player.score) + " bits!")
    print()
    input("Press ENTER to quit game!")
    quit()
# Similar to game_over_prompt
def victory_prompt():
    print("     _____                                               ")
    print("  __|   _ |__  ____  ______   __    _____  _____ __    _ ")
    print(" \  \  //    ||    ||   ___|_|  |_ /     \|     |\ \  // ")
    print(" |\  \//     ||    ||   |__|_    _||     ||     \ \ \//  ")
    print(" |_\__/    __||____||______| |__|  \_____/|__|\__\/__/   ")
    print("    |_____|                                              ")
    print()
    print("You managed to escape and won! Congratulations!")
    print()
    print("Your score is: " + str(player.score) + " bits!")
    print()
    input("Press ENTER to quit game!")
    print()
    quit()

# Loads data from save file.
def continue_from_save():
    print()
    print("Do you want to start a 'New Game' or 'Continue' from save file?")
    print("0. Quit")
    print("1. New Game (keep saves)")
    print("2. New Game (delete saves)")
    print("3. Continue")
    print()
    a = input("Choose a number from list: ").strip()
    while True:
        if a == "0":
            quit()
        elif a == "1":
            return False
        elif a == "2":
            for file in os.listdir("saves"):
                os.remove(os.path.join("saves", file))
            print("All save data has been deleted! New game will be started.")
            enter()
            return False
        elif a == "3":
            return True
        else:
            a = input("You need to choose a number from the list: ").strip()
# Takes player input and if player loads a file, returns True, else it returns False and returns back to main menu.
def continue_choice(file_list, a):
    print()
    user = input("Choose a number from list: ").strip()
    while True:
        quit_test(user)
        if user == "0":
            return False
        elif user.isdigit():
            if 0 < int(user) <= a:
                file_choice = file_list[int(user) - 1]
                load(file_choice)
                print(file_choice + " loaded!")
                enter()
                return True
            else:
                user = input("You need to type a valid number from the list: ")
        else:
            user = input("You need to type a number from the list: ")
# Prompts player if they want to continue from save, start a new game or quit at the beginning.
def load(file_name):
    file = os.path.join("saves", file_name)
    with open(file, "r") as f:
        data = json.load(f)
        player.player_name = data["player_name"]
        player.hp = data["hp"]
        player.weight = data["weight"]
        player.inventory = list(data["inventory"])
        player.score = data["score"]
        player.armor = data["armor"]
        player.is_naked = data["is_naked"]
        player.last_room = data["last_room"]
        player.current_room = data["current_room"]
        player.in_room = data["in_room"]
        player.in_battle_enemy_hp = data["in_battle_enemy_hp"]
        player.encounters = data["encounters"]
        player.scanner_power = data["scanner_power"]
        player.hangar_2_power = data["hangar_power"]
        player.objectives = data["objectives"]
        for key, value in data.items():
            if key in rooms:
                rooms[key] = value
# Write player and room data into save file.
def save(file_name):
    file = os.path.join("saves", file_name + ".json")
    if save_exists(file) and file_name != "auto_save":
        user = input("Overwrite previous save (yes/no)? ").lower().strip()
        while True:
            quit_test(user)
            if user == "yes":
                break
            elif user == "no":
                return False
            else:
                user = input("You have to type 'yes' or 'no'.")
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
        "in_battle_enemy_hp": player.in_battle_enemy_hp,
        "encounters": player.encounters,
        "scanner_power": player.scanner_power,
        "hangar_power": player.hangar_2_power,
        "objectives": player.objectives
    }
    for key, value in rooms.items():
        data[key] = value
    with open(file, "w") as f:
        json.dump(data, f)
    return True
# Checks if save file exists in directory. Returns True if it exists.
def save_exists(file_name):
    try:
        with open(file_name) as file:
            return True
    except IOError as e:
        return False


def screen_flush():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()