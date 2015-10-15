from command_list import *
from player import inventory
import player
from map import rooms
import time


def loading(rate):
    a = 0
    b = random.randint(0, 10)
    while a < 100:
            if a > (15 - b):
                rate = 80
                if a > (25 + b):
                    rate = 75
                    if a > (50 - b):
                        rate = 20
                        if a > (70 - b/2):
                            rate = 150
                            if a > (80 - b):
                                rate = 50
            seconds = random.randint(1, rate)
            print("Loading: " + str(a) + "% done", end="\r")
            a += 1
            time.sleep(seconds/1000)
# loading(100)

in_room = "Player Ship"
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

def remove_punct(text):
    txt = text
    for punct in string.punctuation:
        txt = txt.replace(punct, "")
    return txt


def remove_spaces(text):
    text = text.strip()
    print(text)


def display_room(room):
    # CMD Version
    # print("\n    ╗ ┌" + (len(room["name"]) * "─") + "┐ ╔ ")
    # print("    ╠═╣" + room["name"].upper() + "╠═╣")
    # print("    ╝ └" + str(len(room["name"]) * "─") + "┘ ╚ ")

    # Normal Version
    print("\n    ╗┌" + (len(room["name"]) * "-") + "┐╔ ")
    print("    ╠╣" + room["name"].upper() + "╠╣")
    print("    ╝└" + str(len(room["name"]) * "-") + "┘╚ ")

    print("\n" + room["description"] + "\n")
    print_room_items(room)


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
    user_input = "a"
    while True:
        if user_input.strip() == "":
            user_input = input(player.player_name + ": ")
        else:
            user_input = input("\n" + player.player_name + ": ")
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
                # Actually checks and executes the requested by the player command.
                if is_valid_command(cmdn) or cmdn in commands_aliases or ((user_input.find("scan") >= 0) and (user_input.find("scanner") < 0)):
                    # Checks if you type "go <dir>", "go" + "<dir>" or just <dir> (dir = direction)
                    if cmdn == "go":
                        valid = command_go_superior(exits, in_room, cmd)
                        if valid:
                            return valid
                    if cmdn == "playername":
                        player.player_name = command_name_change()
                    if cmdn == "take":
                        command_take(player.player_name, in_room, cmd)
                        update_player_stats()
                    if cmdn == "drop":
                        command_drop(player.player_name, in_room, cmd)
                        update_player_stats()
                    if cmdn == "stats":
                        command_stats(in_room)
                    if cmdn == "exits":
                        print_menu(exits)
                    if cmdn == "help":
                        command_help(user_input)
                    if cmdn == "inspect":
                        user_input = user_input.replace("inspect", "")
                        cmd = normalise_input(user_input)
                        command_inspect(rooms[in_room], cmd, player.player_name, inventory)
                        user_input = "a"
                    if cmdn == "quit":
                        quit()
                    if cmdn == "inventory":
                        command_inventory(inventory)
                    if (user_input.find("scan") >= 0 or cmdn in commands_aliases) and (user_input.find("take") < 0) and (user_input.find("drop") < 0):
                        user_input = user_input.replace("scan", "")
                        for alpha in commands_aliases:
                            user_input = user_input.replace(alpha, "")
                        cmd = normalise_input(user_input)
                        scan_element(rooms[in_room], cmd, player.player_name, inventory)
                        user_input = str(cmd)
                else:
                    i = random.randint(0, len(command_unknown) - 1)
                    print(command_unknown[i])


def move(exits, direction):
    return rooms[exits[direction]]


def menu(current_room):
    display_room(current_room)
    exits = current_room["exits"]
    print_menu(exits)
    command_input = command_execute(exits)
    player.last_room = current_room["name_ID"]
    print("DEBUG NOTICE: COMMAND_INPUT " + command_input)
    if command_input == "hangar_1" and get_room_state(rooms_states["Hangar 1"]) == 1:
        rooms_states[current_room["name_ID"]]["state"] = 3
    return move(exits, command_input)


def main():
    # Start game at the room_1
    current_room = rooms["Player Ship"]
    print("Type 'help' to see a list of available commands (or 'help detailed' for more info).")
    print()
    print("Hello " + player.player_name + "!")
    global in_room
    # Main game loop
    while True:
        update_room_state(current_room["name_ID"])
        update_player_stats()
        current_room = menu(current_room)
        in_room = current_room["name_ID"]
main()
