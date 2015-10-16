from items import *
from objects import *

# For our code to work the rooms MUST have an 'objects' and 'items' sub-list/dict, otherwise the functions cannot
# address them and evaluate if there are any items/objects to interact with.
# P.S. Objects are currently intended to be only inspected, items are the "room's inventory".

player_ship = {
    "name_ID": "Player Ship",

    "name": "Player Ship",

    "description": "The ceiling has a very darkish shade to it, "
                   "\nseemingly because of the moisture."
                   "\nWhen you look at the walls you can see water running down them."
                   "\nThe place looks like it will fall apart at any moment!",

    "exits": {"hangar_1": "Hangar 1"},

    "objects": [object_ceiling],

    "items": [item_biscuits, item_handbook, item_scanner]

}

hangar_1 = {
    "name_ID": "Hangar 1",

    "name": "Hangar #1",

    "description": """needs description2""",

    "exits": {"player_ship": "Player Ship", "hangar_2": "Hangar 2", "vehicle_maintenance": "Vehicle Maintenance",
              "vehicle_storage": "Vehicle Storage"},

    "items": [item_screwdriver, item_rose],

    "objects": {}
}

hangar_2 = {
    "name_ID": "Hangar 2",
    "name": "Hangar #2",

    "description": """needs description3""",

    "exits": {"hangar_1": "Hangar 1", "vehicle_maintenance": "Vehicle Maintenance",
              "vehicle_storage": "Vehicle Storage"},

    "items": [],

    "objects": {}
}

vehicle_maintenance = {
    "name_ID": "Vehicle Maintenance",
    "name": "Vehicle Maintenance",

    "description": """needs description4""",

    "exits": {"hangar_1": "Hangar 1", "hangar_2": "Hangar 2", "vehicle_storage": "Vehicle Storage",
              "power_generator": "Power Generator"},

    "objects": {},

    "items": []
}

vehicle_storage = {
    "name_ID": "Vehicle Storage",
    "name": "Vehicle Storage",

    "description":
    """needs description5""",

    "exits": {"hangar_1": "Hangar 1", "hangar_2": "Hangar 2", "vehicle_maintenance": "Vehicle Maintenance",
              "crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

crew_quarters = {
    "name_ID": "Crew Quarters",
    "name": "Crew Quarters",

    "description":
    """needs description6""",

    "exits": {"vehicle_storage": "Vehicle Storage", "power_generator": "Power Generator", "room_203": "Room 203", "room_12": "Room 12", "room_139": "Room 139",
              "room_5": "Room 5", "detention_centre": "Detention Centre"},

    "items": [],

    "objects": {}
}

power_generator = {
    "name_ID": "Power Generator",
    "name": "Power Generator",

    "description":
    """needs description7""",

    "exits": {"crew_quarters": "Crew Quarters", "vehicle_maintenance": "Vehicle Maintenance",
              "power_control": "Power Control", "main_engineering": "Main Engineering"},

    "items": [],

    "objects": {}
}

power_control = {
    "name_ID": "Power Control",
    "name": "Power Control",

    "description":
    """needs description8""",

    "exits": {"power_generator": "Power Generator"},

    "items": [],

    "objects": {}
}

main_engineering = {
    "name_ID": "Main Engineering",
    "name": "Main Engineering",

    "description":
    """needs description9""",

    "exits": {"power_generator": "Power Generator", "engine_room": "Engine Room",
              "weapons_control": "Weapons Control", "officer_deck": "Officer Deck"},

    "items": [],

    "objects": {}
}

engine_room = {
    "name_ID": "Engine Room",
    "name": "Engine Room",

    "description":
    """needs description10""",

    "exits": {"main_engineering": "Main Engineering"},

    "items": [],

    "objects": {}
}

weapons_control = {
    "name_ID": "Weapons Control",
    "name": "Weapons Control",

    "description":
    """needs description10""",

    "exits": {"main_engineering": "Main Engineering", "armory": "Armory",
              "officer_deck": "Officer Deck"},

    "items": [],

    "objects": {}
}

officer_deck = {
    "name_ID": "Officer Deck",
    "name": "Officer Deck",

    "description":
    """needs description10""",

    "exits": {"main_engineering": "Main Engineering", "weapons_control": "Weapons Control",
              "bridge": "Bridge", "systems_control": "Systems Control"},

    "items": [],

    "objects": {}
}

bridge = {
    "name_ID": "Bridge",
    "name": "Bridge",

    "description":
    """needs description10""",

    "exits": {"officer_deck": "Officer Deck", "systems_control": "Systems Control"},

    "items": [],

    "objects": {}
}

systems_control = {
    "name_ID": "Systems Control",
    "name": "Systems Control",

    "description":
    """needs description10""",

    "exits": {"officer_deck": "Officer Deck", "bridge": "Bridge"},

    "items": [],

    "objects": {}
}

armory = {
    "name_ID": "Armory",
    "name": "Armory",

    "description":
    """needs description10""",

    "exits": {"weapons_control": "Weapons Control"},

    "items": [],

    "objects": {}
}

med_bay = {
    "name_ID": "Med Bay",
    "name": "Med Bay",

    "description":
    """needs description10""",

    "exits": {"officer_deck": "Officer Deck", "crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

room_5 = {
    "name_ID": "Room 5",
    "name": "Room 5",

    "description":
    """needs description10""",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

room_139 = {
    "name_ID": "Room 139",
    "name": "Room 139",

    "description":
    """needs description10""",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

room_12 = {
    "name_ID": "Room 12",
    "name": "Room 12",

    "description":
    """needs description10""",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

room_203 = {
    "name_ID": "Room 203",
    "name": "Room 203",

    "description":
    """needs description10""",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}

detention_centre = {
    "name_ID": "Detention Centre",
    "name": "Detention Centre",

    "description":
    """needs description10""",

    "exits": {"crew_quarters": "Crew Quarters"},

    "items": [],

    "objects": {}
}


# Had to change room names so that they would be addressed as their
# function name and ID. We can alter the names in the room dicts instead.
rooms = {
    "Player Ship": player_ship,
    "Hangar 1": hangar_1,
    "Hangar 2": hangar_2,
    "Vehicle Maintenance": vehicle_maintenance,
    "Vehicle Storage": vehicle_storage,
    "Crew Quarters": crew_quarters,
    "Power Generator": power_generator,
    "Power Control": power_control,
    "Main Engineering": main_engineering,
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
