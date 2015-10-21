from items.items import *
from map import rooms
from random import randint 

# Variables are dynamic - they change as the game progresses.
player_name = ""
hp = 100
weight = 0
inventory = []
score = 0
armor = 0

is_naked = 0
scanner_power = 12

# Used to calculate and change current enemy hp instead of the enemy declaration itself
in_battle_enemy_hp = 0
encounters = []
auto_save_count = 0
# Whenever the player moves to a new room, last_room is changed to the previous one so that the player can use "go back" to go back
last_room = []

# Updates the room the player is currently in (happens before room is displayed)
current_room = rooms["Wrecked Ship"]

# For certain commands, tells the player in which room he is. Variable is set to room's name_ID value
in_room = "Wrecked Ship"
#Boss enemy, maybe change the variable name to enemy_boss?
enemy = {"name": "Kirill", "hp": 100, "weapon": "spoon"}