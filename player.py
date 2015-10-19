from items.items import *
from map import rooms

# Variables are dynamic - they change as the game progresses.
player_name = ""
hp = 100
weight = 0
inventory = []
score = 0

is_naked = 0

# Whenever the player moves to a new room, last_room is changed to the previous one so that the player can use "go back" to go back
last_room = "None"

# Updates the room the player is currently in (happens before room is displayed)
current_room = rooms["Wrecked Ship"]

# For certain commands, tells the player in which room he is. Variable is set to room's name_ID value
in_room = "Wrecked Ship"

enemy = {"Name": "Kirill", "HP": 100, "Current Weapon": "spoon"}