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

# Whenever the player moves to a new room, last_room is changed to the previous one so that the player can use "go back" to go back
last_room = "None"

# Updates the room the player is currently in (happens before room is displayed)
current_room = rooms["Wrecked Ship"]

# For certain commands, tells the player in which room he is. Variable is set to room's name_ID value
in_room = "Wrecked Ship"

#Boss enemy, maybe change the variable name to enemy_boss?
#Accuracy is high and medium-high chance to dodge.
enemy = {"name": "Kirill", "hp": 100, "weapon": ["Spoon" , "Rocket Launcher" , "Laptop"] , "damage": [randint(15,20), randint(15,30), 5]}
#3 Various enemies which can be around the map. Need too assign accuracy and dodge still. 
#Accuracy is low for the gun but high for the sword for enemy_1 and low dodge chance
enemy_1 = {"name": "Volderwart", "hp": 20, "weapon": ["Gun", "Sword"] , "damage": [randint(5,10), randint(1,10)]}
#Accuracy is low for enemy_2 and medium dodge chance
enemy_2 = {"name": "Potter", "hp": 40, "weapon": "Mini Pistol", "damage": randint(10,30)}
#Accuracy is medium for enemy_3 and medium dodge chance
enemy_3 = {"name": "Matt", "hp": 50, "weapon": "Battle Axe", "damage": randint(10,20)}