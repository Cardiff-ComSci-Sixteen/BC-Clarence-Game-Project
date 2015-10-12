from room_states import rooms_states
from room_states import change_description



room_1 = {
    "name_ID": "room_1",

    "name": "needs_name1",

    "description": rooms_states["room_1"]["state_" + str(change_description("room_1"))]["description"],

    "exits": {"south": "needs_name2", "west": "needs_name3"},

    "objects": {"ceiling": "It looks rather unstable. The material will hardly stay strong forever."
                           "\nI cannot imagine what would happen if it collapsed atop of me!"
                }

}

room_2 = {
    "name_ID": "room_2",

    "name": "needs_name2",

    "description":
    """Need Discription""",

    "exits": {"north": "needs_name1"},

    # "objects": {"ceiling": "stuff like this"}
    # ADD EXITS HERE!
}

room_3 = {
    "name_ID": "room_3",
    "name": "needs_name3",

    "description":
    """needs description""",

    "exits": {"east": "needs_name1"},
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    # ADD EXITS HERE!
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.
    """,

    "exits": {"south": "Admins", "north": "Mindas"}

    # ADD EXITS HERE!
}



rooms = {
    "needs_name1": room_1,
    "needs_name2": room_2,
    "needs_name3": room_3,
    "Parking": room_parking,
    "Office": room_office
}