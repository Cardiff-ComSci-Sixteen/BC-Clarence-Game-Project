from lists.command_list import *
import player
from map import rooms
import time
import events
import os

# Variable included as rooms change. Similar to current_room but used a bit differently.
# player.in_room = "Player Ship"


def loading(rate):
    a = 0
    b = random.randint(0, 10)
    rate_ratio = rate/100
    while a < 100:
            if a > (15 - b):
                rate = 80*rate_ratio
                if a > (25 + b):
                    rate = 75*rate_ratio
                    if a > (50 - b):
                        rate = 20*rate_ratio
                        if a > (70 - b/2):
                            rate = 150*rate_ratio
                            if a > (80 - b):
                                rate = 50*rate_ratio
            seconds = random.randint(1, int(rate))
            print("Loading: " + str(a) + "% done", end="\r")
            a += 1
            time.sleep(seconds/1000)


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


def is_valid_command(user_input):
    if user_input in commands:
        return True
    else:
        return False


# Mainly replaces the command_execute function given during Exercise_2
def command_execute(exits):
    user_input = "a"
    while True:
        # time.sleep(3)
        # save()
        # print("Your game has been saved!")
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
                cmd = input_combine(cmd)
                cmdn = cmd[0]
                # Actually checks and executes the requested by the player command.
                if is_valid_command(cmdn) or cmdn in commands_aliases or ((user_input.find("scan") >= 0) and (user_input.find("scanner") < 0)):
                    # Checks if you type "go <dir>", "go" + "<dir>" or just <dir> (dir = direction)
                    if cmdn == "go":
                        valid = command_go_superior(exits, player.in_room, cmd)
                        if valid:
                            return valid
                    if cmdn == "playername":
                        player.player_name = command_name_change()
                    if cmdn == "save":
                        file_name = input("Type the name of your save (use only numbers, letters, spaces, ' and '_'): ")
                        for char in file_name:
                            if char in string.punctuation and char != "_" and char != "'":
                                file_name = file_name.replace(char, "")
                        if file_name.strip() == "":
                            file_name = "save_data"
                        if save(file_name):
                            print("Your game has been saved to '" + file_name + ".json'.")
                        else:
                            print("Save canceled.")
                    if cmdn == "take":
                        command_take(player.player_name, player.in_room, cmd, player.inventory)
                        update_player_stats(player.inventory)
                    if cmdn == "drop":
                        command_drop(player.player_name, player.in_room, cmd, player.inventory)
                        update_player_stats(player.inventory)
                    if cmdn == "stats":
                        command_stats(player.in_room, player.inventory)
                    if cmdn == "exits":
                        print_menu(exits)
                    if cmdn == "help":
                        command_help(user_input)
                    if cmdn == "inspect":
                        user_input = user_input.replace("inspect", "")
                        cmd = normalise_input(user_input)
                        cmd = input_combine_commands(cmd)
                        command_inspect(rooms[player.in_room], cmd, player.player_name, player.inventory)
                        user_input = "a"
                    if cmdn == "quit":
                        quit()
                    if cmdn == "inventory":
                        command_inventory(player.inventory)
                    if (user_input.find("scan") >= 0 or cmdn in commands_aliases) and (user_input.find("take") < 0) and (user_input.find("drop") < 0):
                        user_input = user_input.replace("scan", "")
                        for alpha in commands_aliases:
                            user_input = user_input.replace(alpha, "")
                        cmd = normalise_input(user_input)
                        cmd = input_combine_commands(cmd)
                        power = player.scanner_power
                        if item_scanner in player.inventory:
                            if power >= 1:
                                if command_scan(rooms[player.in_room], cmd, player.player_name, player.inventory):
                                    player.scanner_power -= 1
                                    power -= 1
                                    if power > 10:
                                        print(str(power) + "% Power Left")
                                    elif power > 0:
                                        print("\nWARNING: Power Low!\n" + str(power) + "% Power Left")
                                    else:
                                        print("No Charge Left")
                                user_input = str(cmd)
                            else:
                                print("There is no power in the scanner at the moment. I need to recharge it somehow!")
                        else:
                            print("I need something to scan this with!")
                elif events.input_event_update(cmd, exits, player.inventory):
                    pass
                else:
                    i = random.randint(0, len(command_unknown) - 1)
                    print(command_unknown[i])


def move(exits, direction):
    return rooms[exits[direction]]


def menu(current_room, exits):
    display_room(current_room)
    print_menu(exits)
    print("\nTESTING: Type 'battle' to initiate a test battle with Kirill's Minion!")
    if player.auto_save_count == 5:
        player.auto_save_count = 0
        save("auto_save")
        print("Progress has been auto-saved!")
    command_input = command_execute(exits)
    return move(exits, command_input)


# Called whenever there is a save file. If none - New game is started.
def main_menu():
    if not os.path.isdir("saves"):
        os.makedirs("saves")
    file_list = os.listdir("saves")
    while True:
        if file_list:
            if continue_from_save():
                print()
                print("Your current saves:")
                a = 0
                # Print Continue Menu
                print("0. Return")
                for file in file_list:
                    a += 1
                    print(str(a) + ". " + file)
                if continue_choice(file_list, a):
                    break

            else:
                events.intro_prompt()
                events.post_intro_prompt(player.inventory)
                break
        else:
            events.intro_prompt()
            events.post_intro_prompt(player.inventory)
            break


def main():
    main_menu()
    # Start game at the room_1
    print("Type 'help' to see a list of available commands (or 'help detailed' for more info).")
    print()

    print("""IMPORTANT: Things to remove which are currently put just for testing purposes:"
    - This Message
    - "battle" from events
    - "Type Battle" from menu()
          """)

    print("Hello " + player.player_name + "!")
    # Main game loop
    while True:
        # update_room_state(player.current_room["name_ID"])
        update_player_stats(player.inventory)
        exits = player.current_room["exits"]
        player.current_room = menu(player.current_room, exits)
        player.auto_save_count += 1
        player.in_room = player.current_room["name_ID"]
        events.event_update(exits)

# loading(100)

while True:
    try:
        main()
    except GameOver:
        game_over_prompt()
        # a = game_over_prompt()
        # if a == "quit":
        #     quit()
        # else:
        #     print("\n" * 50)
        #     print("┌──────────────────────┐")
        #     print("│ Starting a new game! │")
        #     print("└──────────────────────┘")
        #     print()
        #     loading(30)
