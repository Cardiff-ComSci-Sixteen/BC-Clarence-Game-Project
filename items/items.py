import random
from items.armor import *
from items.weapons import *


def key_generate():
    key_number = random.randint(0, 9999)
    # print("Key is: " + str(key_number).zfill(4))
    return str(key_number).zfill(4)
key = key_generate()

# the new "id" of each item is a list as the SCAN and INSPECT commands will not go through it
# and check if a keyword is there. Check biscuits
# for example - the player can time biscuits, pack or pack_biscuits (pack of biscuits)
# and it will detect it and interact with it, like take, drop, inspect, scan
# the first description is used when INSPECTING the item, the second is when SCANNING it
# if description_scan is omitted, the SCAN command will tell the player that there is nothing special about the item

# name is just what will be printed when player inspects inventory/item or scans it - will probably have to change
# so that when scanning it does not say: "A PACK OF BISCUITS" and says "PACK OF BISCUITS" instead. Could be simply using a new
# dictionary for that. item_<object> goes into either room["items"] or player inventory.

# Type defines whether the item is a consumable, a weapon or armor. That way we can calculate further stats based on the item
# like "damage reduction", "strength", "damage", etc. and get feedback if it's not a weapon, like if you use your ID -> "This is not a weapon!"

# Each item has a class number. Each number corresponds to the following:
# 0 - Misc
# 1 - Weapon
# 2 - Armor
# 3 - Consumable
# 4 - Key
# 5 - Objective Item

item_biscuits = {
    "id": ["biscuits", "pack_biscuits", "pack"],

    "class": 3,

    "weight": 10,

    "name": "a pack of biscuits",

    "description": "A pack of biscuits of delicious-looking biscuits.",

    "description_scan": "The pack is contaminated!"
}

item_coffee = {
    "id": ["coffee"],

    "class": 3,

    "weight": 10,

    "name": "a cup of coffee",

    "description": "A fine cup of coffee."
}

item_medkit = {
    "id": ["medkit", "med_kit"],

    "class": 3,

    "weight": 10,

    "name": "a Med-Kit",

    "description": "A kit with medicine inside. Might find it useful if I got hurt!"
}

item_scanner = {
    "id": ["scanner"],

    "class": 5,

    "weight": 20,

    "name": "a scanner",

    "description":
    """With this I will finally be able to analyze things around me!""",

    "attributes": {"power": 12}
}

item_note = {
    "id": ["note"],

    "class": 0,

    "weight": 5,

    "name": "Captain's Note",

    "description":
    "The ship we are on has been contaminated!\n"
    "You will most likely need my passcode, \n"
    "to unlock my door, so here it is: " + str(key)
}

item_keyA = {
    "id": ["keyA"],

    "class": 4,

    "weight": 0,

    "name": "Armory Key Card",

    "description":
    "This should allow me to access the Armory"
}

item_keyD = {
    "id": ["keyD"],

    "class": 4,

    "weight": 0,

    "name": "Detention Centre Key Card",

    "description":
    "This should allow me to access the Detention Centre"
}

item_keyP = {
    "id": ["keyP"],

    "class": 4,

    "weight": 0,

    "name": "Power Control Key Card",

    "description":
    "This should allow me to access the Power Control"
}


item_vodka = {
    "id": ["vodka"],

    "class": 3,

    "weight": 10,

    "name": "Vodka",

    "description": "If I drink this I will get drunk"
}

item_bass = {
    "id": ["bass"],

    "class": 0,

    "weight": 0,

    "name": "some bass",

    "description": "The low frequency makes your body tremble!"
}