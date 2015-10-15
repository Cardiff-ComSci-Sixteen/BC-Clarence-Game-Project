# Each room needs to have at least one state or else the functions will cause a supernova.
player_ship = {
    "state_1": {"description": "The ceiling has a very darkish shade to it, "
                "\nseemingly because of the moisture."
                "\nWhen you look at the walls you can see water running down them."
                "\nThe place looks like it will fall apart at any moment!",
                "objects": {
                "ceiling": "This is keeping the structure safe from the outside climate."
                           "\nI cannot imagine what would happen if it collapsed on me!"
                }},
    "state_2": "You are not here.",
    "state_3": {"description": "As you return to Hangar 1 you see that the ceiling,"
                "\nwhich used to cover the room, has now"
                "\ncompletely been destroyed, most probably due"
                "\nto the material having soaked up too much water.",
                "objects": {
                "ceiling": "Destroyed! The heaviness of the water has torn"
                           "\nthe roof apart, flooding the room with water and debris."
                           "\nThe ceiling has been irreversibly damaged."
                }},
    "state": 1,
}

hangar_1 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

hangar_2 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

vehicle_maintenance = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

vehicle_storage = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

crew_quarters = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

power_generator = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

power_control = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

main_engineering = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

engine_room = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

weapons_control = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

officer_deck = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

bridge = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

systems_control = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
armory = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
med_bay = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
room_5 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
room_139 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
room_12 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
room_203 = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}
detention_centre = {
    "state_1": {"description": "needsdescription2_state_1"},
    "state": 1,
}

# List of rooms with states
armory = {
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
