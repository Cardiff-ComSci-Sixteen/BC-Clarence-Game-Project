import random
def key_generate():
    key_number = random.randint(0, 9999)
    # print("Key is: " + str(key_number).zfill(4))
    return str(key_number).zfill(4)
key = key_generate()

item_scanner = {
    "id": "scanner",

    "weight": 20,

    "name": "a scanner",

    "description":
    """With this I will finally be able to analyze things around me!"""
}

item_note = {
    "id": "note",

    "weight": 5,

    "name": "Captain's Note",

    "description":
    "The ship we are on has been contaminated!\n"
    "You will most likely need my passcode, \n"
    "to unlock my door, so here it is: " + str(key)
}

item_id = {
    "id": "id",

    "weight": 5,

    "name": "an id card",

    "description":
    """You new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?..."""
}

item_laptop = {
    "id": "laptop",

    "weight": 45,

    "name": "a laptop",

    "description":
    "It has seen better days. At least it has a WiFi card!"
}

item_money = {
    "id": "money",

    "weight": 10,

    "name": "money",

    "description":
    "This wad of cash is barely enough to pay your tuition fees."
}

item_biscuits = {
    "id": "biscuits",

    "weight": 10,

    "name": "a pack of biscuits",

    "description": "A pack of biscuits."
}

item_pen = {
    "id": "pen",

    "weight": 5,

    "name": "a pen",

    "description": "A basic ballpoint pen."
}

item_handbook = {
    "id": "handbook",

    "weight": 30,

    "name": "a student handbook",

    "description": "This student handbook explains everything. Seriously."
}

item_screwdriver = {
    "id": "screwdriver",

    "weight": 10,

    "name": "a screwdriver",

    "description": "I shouldn't poke my out with this."
}

item_rose = {
    "id": "rose",

    "weight": 20,

    "name": "a rose",

    "description": "Just a lovely red, charming rose!"
}


item_bass = {
    "id": "bass",

    "weight": 0,

    "name": "some bass",

    "description": "The low frequency makes your body tremble!"
}