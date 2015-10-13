from objects import *

# For our code to work the rooms MUST have an 'objects' and 'items' sub-list/dict, otherwise the functions cannot
# address them and evaluate if there are any items/objects to interact with.
# P.S. Objects are currently intended to be only inspected, items are the "room's inventory"

player_ship = {
    "name_ID": "Player Ship",

    "name": "Player Ship",

    "description": "The ceiling has a very darkish shade to it, "
                   "\nseemingly because of the moisture."
                   "\nWhen you look at the walls you can see water running down them."
                   "\nThe place looks like it will fall apart at any moment!",

    "exits": {"hangar_1": "Hangar 1"},

    "objects": {"ceiling": ["It looks rather unstable. The material will hardly stay strong forever."
                            "\nI cannot imagine what would happen if it collapsed atop of me!", 0]
                },
    "items": [item_biscuits, item_handbook]

}

hangar_1 = {
    "name_ID": "Hangar 1",

    "name": "Hangar #1",

    "description": """needs description2""",

    "exits": {"player_ship": "Player Ship", "Hangar 2": "hangar_2", "Vehicle Maintence": "Vehicle_Maintence",
    "Vehicle Storage": "Vehicle_Storage"},

    "items": [],

    "objects": {}
}

hangar_2 = {
    "name_ID": "hangar_2",
    "name": "Hangar 2",

    "description": """needs description3""",

    "exits": {"hangar_1": "hangar_1", "Vehicle Maintence": "Vehicle_Maintence",
    "Vehicle Storage": "Vehicle_Storage"},

    "items": []
}

Vehicle_Maintence = {
    "name_ID": "Vehicle_Maintence",
    "name": "Vehicle Maintence",

    "description": """needs description4""",

    "exits": {"Hangar 1": "hangar_1", "Hangar 2": "hangar_2", "Vehicle Storage": "Vehicle_Maintence",
    "Power Generator": "Power_Generator"},

    "items": []
}

Vehicle_Storage = {
    "name_ID": "Vehicle_Storage",
    "name": "Vehicle Storage",

    "description":
    """needs description5""",

    "exits": {"Hangar 1": "hangar_1", "Hangar 2": "hangar_2", "Vehicle Maintence": "Vehicle_Maintence",
    "Crew Quarters": "Crew_Quarters"},

    "items": []
}

Crew_Quarters = {
    "name_ID": "Crew_Quarters",
    "name": "Crew Quarters",

    "description":
    """needs description6""",

    "exits": {"Vehicle_Storage": "Vehicle_Storage", "Power Generator": "Power_Generator", "Room 203": "Room_203", "Room 12": "Room _12", "Room 139": "Room_139",
    "Room 5": "Room_5", "Detention Centre": "Detention_Centre"},

    "items": []
}

Power_Generator = {
    "name_ID": "Power_Generator",
    "name": "Power Generator",

    "description":
    """needs description7""",

    "exits": {"Crew Quarters": "Crew_Quarters", "Vehicle Maintence": "Vehicle_Maintence",
    "Power Control": "Power_Control", "Main Engineering": "Main_Engineering"},

    "items": []
}

Power_Control = {
    "name_ID": "Power_Control",
    "name": "Power Control",

    "description":
    """needs description8""",

    "exits": {"Power Generator": "Power_Generator"},

    "items": []
}

Main_Engineering = {
    "name_ID": "Main_Engineering",
    "name": "Main Engineering",

    "description":
    """needs description9""",

    "exits": {"Power Generator": "Power_Generator", "Engine Room": "Engine_Room",
    "Weapons Control": "Weapons_Control", "Officer Deck": "Officer_Deck"},

    "items": []
}

Engine_Room = {
    "name_ID": "Engine_Room",
    "name": "Engine Room",

    "description":
    """needs description10""",

    "exits": {"Main Engineering": "Main_Engineering"},

    "items": []
}

Weapons_Control = {
    "name_ID": "Weapons_Control",
    "name": "Weapons Control",

    "description":
    """needs description10""",

    "exits": {"Main Engineering": "Main_Engineering", "Main Gun": "Main_Gun",
    "Officer Deck": "Officer_Deck"},

    "items": []
}

Officer_Deck = {
    "name_ID": "Officer_Deck",
    "name": "Officer Deck",

    "description":
    """needs description10""",

    "exits": {"Main Engineering": "Main_Engineering", "Weapons Control": "Weapons_Control",
    "Bridge": "Bridge", "Systems Control": "Systems_Control"},

    "items": []
}

Bridge = {
    "name_ID": "Bridge",
    "name": "Bridge",

    "description":
    """needs description10""",

    "exits": {"Officer Deck": "Officer_Deck", "Systems Control": "Systems_Control"},

    "items": []
}

Systems_Control = {
    "name_ID": "Systems_Control",
    "name": "Systems Control",

    "description":
    """needs description10""",

    "exits": {"Officer Deck": "Officer_Deck", "Bridge": "Bridge"},

    "items": []
}

Main_Gun = {
    "name_ID": "Main_Gun",
    "name": "Main Gun",

    "description":
    """needs description10""",

    "exits": {"Weapons Control": "Weapons_Control"},

    "items": []
}

Med_Bay = {
    "name_ID": "Med_Bay",
    "name": "Med Bay",

    "description":
    """needs description10""",

    "exits": {"Officer Deck": "Officer_Deck", "Crew Quarters": "Crew_Quarters"},

    "items": []
}

Room_5 = {
    "name_ID": "Room_5",
    "name": "Room 5",

    "description":
    """needs description10""",

    "exits": {"Crew Quarters": "Crew_Quarters"},

    "items": []
}

Room_139 = {
    "name_ID": "Room_139",
    "name": "Room 139",

    "description":
    """needs description10""",

    "exits": {"Crew Quarters": "Crew_Quarters"},

    "items": []
}

Room_12 = {
    "name_ID": "Room_12",
    "name": "Room 12",

    "description":
    """needs description10""",

    "exits": {"Crew Quarters": "Crew_Quarters"},

    "items": []
}

Room_203 = {
    "name_ID": "Room_203",
    "name": "Room 203",

    "description":
    """needs description10""",

    "exits": {"Crew Quarters": "Crew_Quarters"},

    "items": []
}

Detention_Centre = {
    "name_ID": "Detention_Centre",
    "name": "Detention Centre",

    "description":
    """needs description10""",

    "exits": {"Crew Quarters": "Crew_Quarters"},

    "items": []
}


# Had to change room names so that they would be addressed as their
# function name and ID. We can alter the names in the room dicts instead.
rooms = {
    "Player Ship": player_ship,
    "Hangar 1": hangar_1,
    "hangar_2": hangar_2,
    "Vehicle_Maintence": Vehicle_Maintence,
    "Vehicle_Storage": Vehicle_Storage,
    "Crew_Quarters": Crew_Quarters,
    "Power_Generator": Power_Generator,
    "Power_Control": Power_Control,
    "Main_Engineering": Main_Engineering,
    "Engine_Room": Engine_Room,
    "Weapons_Control": Weapons_Control,
    "Officer_Deck": Officer_Deck,
    "Bridge": Bridge,
    "Systems_Control": Systems_Control,
    "Main_Gun": Main_Gun,
    "Med_Bay": Med_Bay,
    "Room_5": Room_5,
    "Room_139": Room_139,
    "Room_12": Room_12,
    "Room_203": Room_203,
    "Detention_Centre": Detention_Centre,
}
