import random
def key_generate():
    key_number = random.randint(0, 9999)
    # print("Key is: " + str(key_number).zfill(4))
    return str(key_number).zfill(4)
key = key_generate()

# the new "id" of each item is a list as the SCAN and INSPECT commands will not go through it
# and check if a keyword is there. Check biscuits for example - the player can time biscuits, pack or pack_biscuits (pack of biscuits)
# and it will detect it and interact with it, like take, drop, inspect, scan





# the first description is used when INSPECTING the item, the second is when SCANNING it
# if description_scan is omitted, the SCAN command will tell the player that there is nothing special about the item

# name is just what will be printed when player inspects inventory/item or scans it - will probably have to change
# so that when scanning it does not say: "A PACK OF BISCUITS" and says "PACK OF BISCUITS" instead. Could be simply using a new
# dictionary for that. item_<object> goes into either room["items"] or player inventory.

item_powersword = {
    "id": ["power_sword", "power"],

    "weight": 20,

    "name": "Power Sword",

    "description":
    """A unique item that needs description!"""
}

item_laspistol = {
    "id": ["laspistol"],

    "weight": 20,

    "name": "Laspistol",

    "description":
    """An another unique item that needs description!"""
}

item_swordgun = {
    "id": ["swordgun", "sword_gun"],

    "weight": 20,

    "name": "Sword-Gun",

    "description":
    """A third unique item that needs description!"""
}

item_basic_spacesuit = {
    "id": ["spacesuit", "basic_spacesuit", "suit"],

    "weight": 20,

    "name": "a basic spacesuit",

    "description":
    """Just a simple spacesuit to prevent me from dying out in the open and cold space."""
}

item_basic_armor = {
    "id": ["basic_armor"],

    "weight": 20,

    "name": "basic armor",

    "description":
    """This armor is nothing more than a couple of iron plates stuck together.
    It can't hold against the pressure of space vacuum for a long time."""
}

item_biscuits = {
    "id": ["biscuits", "pack_biscuits", "pack"],

    "weight": 10,

    "name": "a pack of biscuits",

    "description": "A pack of biscuits.",

    "description_scan": "The pack is contaminated!"
}

item_coffee = {
    "id": ["coffee"],

    "weight": 10,

    "name": "a cup of coffee",

    "description": "A fine cup of coffee."
}

item_medkit = {
    "id": ["medkit", "med_kit"],

    "weight": 10,

    "name": "a Med-Kit",

    "description": "A kit with medicine inside. Might find it useful if I got hurt!"
}

item_scanner = {
    "id": ["scanner"],

    "weight": 20,

    "name": "a scanner",

    "description":
    """With this I will finally be able to analyze things around me!"""
}

item_note = {
    "id": ["note"],

    "weight": 5,

    "name": "Captain's Note",

    "description":
    "The ship we are on has been contaminated!\n"
    "You will most likely need my passcode, \n"
    "to unlock my door, so here it is: " + str(key)
}

item_id = {
    "id": ["id", "id_card"],

    "weight": 5,

    "name": "id card",

    "description":
    """You new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?...""",

    "description_scan": """There appears to be some sort of a chip inside the id.
The scanner outputs '436f6d536369' after reading it. Strange..."""
}

item_laptop = {
    "id": ["laptop"],

    "weight": 45,

    "name": "a laptop",

    "description":
    "It has seen better days. At least it has a WiFi card!"
}

item_money = {
    "id": ["money"],

    "weight": 10,

    "name": "money",

    "description":
    "This wad of cash is barely enough to pay your tuition fees."
}

item_pen = {
    "id": ["pen"],

    "weight": 5,

    "name": "a pen",

    "description": "A basic ballpoint pen."
}

item_handbook = {
    "id": ["handbook", "student_handbook"],

    "weight": 30,

    "name": "a student handbook",

    "description": "This student handbook explains everything. Seriously."
}

item_screwdriver = {
    "id": ["screwdriver"],

    "weight": 10,

    "name": "a screwdriver",

    "description": "I shouldn't poke my out with this.",

    # "description_inspect": "Banana"
}

item_rose = {
    "id": ["rose"],

    "weight": 20,

    "name": "a rose",

    "description": "Just a lovely red, charming rose!"
}


item_bass = {
    "id": ["bass"],

    "weight": 0,

    "name": "some bass",

    "description": "The low frequency makes your body tremble!"
}