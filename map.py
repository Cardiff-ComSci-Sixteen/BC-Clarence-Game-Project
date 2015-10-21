from items.items import *
from items.objects import *
from collections import OrderedDict

# For our code to work the rooms MUST have an 'objects' and 'items' sub-list/dict, otherwise the functions cannot
# address them and evaluate if there are any items/objects to interact with.
# P.S. Objects are currently intended to be only inspected, items are the "room's inventory".

# Description has to be input in room's room_states

wrecked_ship = {
    "name_ID": "Wrecked Ship",

    "name": "Wrecked Ship",

    "description": "Just the wrecked remains of Sparrow are all that is left"
                   "\nof the ship. The passage to the back is blocked and I cannot"
                   "\naccess the emergency locker anymore. The board AI has malfunctioned"
                   "\nand there are cables sticking out. One of them is a universal charger,"
                   "\nI might find that handy. The ship has some reserve power left as well!",

    "exits": {"hangar_1": "Hangar 1"},

    "objects": [object_board_AI, object_ceiling],

    "items": []

}

hangar_1 = {
    "name_ID": "Hangar 1",

    "name": "Hangar #1",

    "description":  "Stepping foot into Hangar #1, you can see it has been abandoned, silence everywhere."
                    "\nHairs on the back of your neck stand strong as you feel like your not the only one"
                    "\nHere. You shout 'Hello!!', but get no response.",

    "exits": {"crew_quarters": "Crew Quarters", "hangar_2": "Hangar 2", "vehicle_maintenance": "Vehicle Maintenance",
                          "vehicle_storage": "Vehicle Storage", "wrecked_ship": "Wrecked Ship"},

    "items": [],

    "objects": [object_wrecked_ship]
}

hangar_2 = {
    "name_ID": "Hangar 2",
    "name": "Hangar #2",

    "description":  "You walk into Hangar #2, it also to appears to be on emergancy"
                    "\npower, so can't see very much. From what you can see, it is very"
                    "\nsimilar to Hangar #1 except, it is not very badly damaged, the"
                    "\nmain door is also closed and there is a fighter docked here.",

    "exits": {"hangar_1": "Hangar 1", "vehicle_maintenance": "Vehicle Maintenance", "vehicle_storage": "Vehicle Storage"},

    "items": [],

    "objects": [object_xfighter]
}

vehicle_maintenance = {
    "name_ID": "Vehicle Maintenance",
    "name": "Vehicle Maintenance",

    "description":  "When you walk into Vehicle Maintence you immediately notice several"
                    "\nheavly damaged fighters. It is very chaotic, with what appears to be"
                    "\npower lifters smashed together. You also notice a pools of blood near"
                    "\nto where to lifter are, but no bodies.",

    "exits": {"hangar_1": "Hangar 1", "hangar_2": "Hangar 2", "power_generator": "Power Generator",
                          "vehicle_storage": "Vehicle Storage"},

    "objects": [object_powerlifter, object_damagedfighters],

    "items": [weapon_pulse]
}

vehicle_storage = {
    "name_ID": "Vehicle Storage",
    "name": "Vehicle Storage",

    "description":  "You enter the Vehicle Storage, there is not much to see in here"
                    "\nother than some fighters and bombers that kind of look like H's.",

    "exits": {"crew_quarters": "Crew Quarters", "hangar_1": "Hangar 1", "hangar_2": "Hangar 2",
               "vehicle_maintenance": "Vehicle Maintenance"},

    "items": [],

    "objects": [object_oddfighters]
}

crew_quarters = {
    "name_ID": "Crew Quarters",
    "name": "Crew Quarters",

    "description":  "You are in the Crew Quarters, you notice that there is a few empty"
                    "\nvodka bottles on a table with one full one. There is also lots of"
                    "\nbunkbeds.",

    "exits": {"vehicle_storage": "Vehicle Storage", "power_generator": "Power Generator", "room_203": "Room 203", "room_12": "Room 12", "room_139": "Room 139",
              "room_5": "Room 5", "detention_centre": "Detention Centre", "med_bay": "Med Bay", "hangar_1": "Hangar 1"},

    "items": [item_vodka],

    "objects": [object_emptyvodka, object_bunks]
}

power_generator = {
    "name_ID": "Power Generator",
    "name": "Power Generator",

    "description": "As you enter the Power Generator you see a large reactor, and a few radation suits.",

    "exits": {"crew_quarters": "Crew Quarters", "vehicle_maintenance": "Vehicle Maintenance",
              "power_control": "Power Control", "engineering": "Main Engineering"},

    "items": [],

    "objects": [object_mainreactor]
}

power_control = {
    "name_ID": "Power Control",
    "name": "Power Control",

    "description": "You are in Power Control there is a large console in here, and some hard hats.",

    "exits": {"power_generator": "Power Generator"},

    "items": [],

    "objects": [object_powercontrol],

    "requirement": item_keyP
}

engineering = {
    "name_ID": "Main Engineering",
    "name": "Main Engineering",

    "description":  "When you enter Main Engineering you are greeted by quiet hum, which you"
                    "\nrealise is the warp core for the ship. As you wander further into Main"
                    "\nEngineering you see what appears to be some sort of scanner on a console.",

    "exits": {"power_generator": "Power Generator", "engine_room": "Engine Room",
              "weapons_control": "Weapons Control", "officer_deck": "Officer Deck"},

    "items": [item_scanner],

    "objects": [object_warpcore]
}

engine_room = {
    "name_ID": "Engine Room",
    "name": "Engine Room",

    "description": "You are in the engine room, there is not much in here other than large cooling tanks.",

    "exits": {"engineering": "Main Engineering"},

    "items": [],

    "objects": []
}

weapons_control = {
    "name_ID": "Weapons Control",
    "name": "Weapons Control",

    "description":  "You are in Weapons control, other than the large number of terminals, there is"
                    "\nnot much to see.",

    "exits": {"engineering": "Main Engineering", "armory": "Armory",
              "officer_deck": "Officer Deck"},

    "items": [],

    "objects": [object_weaponcontrol]
}

officer_deck = {
    "name_ID": "Officer Deck",
    "name": "Officer Deck",

    "description":  "You enter the Officers Deck, there is what appears to be a large meeting table and"
                    "\na dead body with keys to the Detention Centre.",

    "exits": {"engineering": "Main Engineering", "weapons_control": "Weapons Control",
              "bridge": "Bridge", "systems_control": "Systems Control", "med_bay": "Med Bay"},

    "items": [armor_heavyarmour2, item_keyD],

    "objects": []
}

bridge = {
    "name_ID": "Bridge",
    "name": "Bridge",

    "description":  "When you walk into the Bridge, you are greeted with a full view of the outside of the ship."
                    "\nThere a large window here and lots of control panels.",

    "exits": {"officer_deck": "Officer Deck", "systems_control": "Systems Control"},

    "items": [item_keyP],

    "objects": [object_bridgecontrols, object_window]
}

systems_control = {
    "name_ID": "Systems Control",
    "name": "Systems Control",

    "description": "You are in life support, there are lots of small consoles with one large one in the middle of the room.",

    "exits": {"officer_deck": "Officer Deck", "bridge": "Bridge"},

    "items": [item_biscuits],

    "objects": [object_lifecontrols]
}

armory = {
    "name_ID": "Armory",

    "name": "Armory",

    "description":  "You are in the armory, there are lots of weapons and armour in here, but only a few catch"
                    "\nyour eye; a phaser, a blaster pistol, a chainsword, power armour, heavy space suit and a"
                    "\ncylindrical object.",

    "exits": {"weapons_control": "Weapons Control"},

    "items": [weapon_phaser, weapon_saber, weapon_blaster, armor_lightarmour3, armor_heavyarmour3],

    "objects": [],

    "requirement": item_keyA
}

med_bay = {
    "name_ID": "Med Bay",
    "name": "Med Bay",

    "description": "You enter the med-bay, there are lots of medical beds. You also notice a pile of what look like med kits.",

    "exits": {"officer_deck": "Officer Deck", "crew_quarters": "Crew Quarters"},

    "items": [item_medkit, item_medkit, item_medkit, weapon_sonicemitter],

    "objects": []
}

room_5 = {
    "name_ID": "Room 5",
    "name": "Room 5",

    "description": "As you enter Room 5 you notice that there is blood everywhere, but no body.",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [armor_lightarmour2],

    "objects": []
}

room_139 = {
    "name_ID": "Room 139",
    "name": "Room 139",

    "description": "Congratulations, you have found a secret, however there is nothing here. -_-",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": []
}

room_12 = {
    "name_ID": "Room 12",
    "name": "Room 12",

    "description": "You enter Room 12, there is a large bed, console, some fish tanks and an offical looking jacket.",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [weapon_energysword],

    "objects": []
}

room_203 = {
    "name_ID": "Room 203",
    "name": "Room 203",

    "description": "You are in Room 203, there are a lot of coffee cups here, chilling on the desk counter,"
                   "\nbut for all intents and purposes I can take only one and no more!",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [item_coffee],

    "objects": []
}

detention_centre = {
    "name_ID": "Detention Centre",
    "name": "Detention Centre",

    "description": "You have entered the Detention Centre, there is a very off putting smell in here and lots of pools of blood.",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [item_keyA],

    "objects": [],

    "requirement": item_keyD
}


# Had to change room names so that they would be addressed as their
# function name and ID. We can alter the names in the room dicts instead.
rooms = {
    "Wrecked Ship": wrecked_ship,
    "Hangar 1": hangar_1,
    "Hangar 2": hangar_2,
    "Vehicle Maintenance": vehicle_maintenance,
    "Vehicle Storage": vehicle_storage,
    "Crew Quarters": crew_quarters,
    "Power Generator": power_generator,
    "Power Control": power_control,
    "Main Engineering": engineering,
    "Engine Room": engine_room,
    "Weapons Control": weapons_control,
    "Officer Deck": officer_deck,
    "Bridge": bridge,
    "Systems Control": systems_control,
    "Armory": armory,
    "Med Bay": med_bay,
    "Room 5": room_5,
    "Room 139": room_139,
    "Room 12": room_12,
    "Room 203": room_203,
    "Detention Centre": detention_centre,
}
