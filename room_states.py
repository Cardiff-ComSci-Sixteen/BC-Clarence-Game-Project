room_1 = {
    "state_1": {"description": "The ceiling has a very darkish shade to it, "
                "\nseemingly because of the moisture."
                "\nWhen you look at the walls you can see water running down them."
                "\nThe place looks like it will fall apart at any moment!",
                "objects": {
                "ceiling": "This is keeping the structure safe from the outside climate."
                           "\nI cannot imagine what would happen if it collapsed on me!"
                }},
    "state_2": "You are not here.",
    "state_3": {"description": "As you return to the room_1 you see that the ceiling,"
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

room_2 = {
    "state_1": "NULL",
    "state": 1,
}

# List of rooms with states
rooms_states = {
    "room_1": room_1,
    "room_2": room_2,
}