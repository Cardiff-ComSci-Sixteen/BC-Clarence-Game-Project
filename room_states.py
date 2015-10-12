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
    "solid_state": 0
}

# Function gets the current state of the room.
def get_room_state(room):
    n = room["state"]
    # print("Get Room State = " + str(n))
    return n

# Function changes the room state depending on input
def change_room_state(room, index):
    rooms_states[room]["state"] = index
    a = rooms_states[room]["state"]
    # print("Change Room State to = " + str(a))
    return a

# Function changes elements inside dictionaries AFTER room state is changed
def change_description(room):
    # print("Change Desc to = " + str(get_room_state(rooms_states[room])))
    return get_room_state(rooms_states[room])

# List of rooms with states
rooms_states = {
    "room_1": room_1,
}