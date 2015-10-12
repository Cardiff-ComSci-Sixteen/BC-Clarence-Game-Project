from room_states import rooms_states
from room_states import change_description



room_1 = {
    "name_ID": "room_1",

    "name": "needs_name1",

    "description": rooms_states["room_1"]["state_" + str(change_description("room_1"))]["description"],

    "exits": {"south": "needs_name2", "east": "needs_name3", "west": "needs_name5"},

    "objects": {"ceiling": "It looks rather unstable. The material will hardly stay strong forever."
                           "\nI cannot imagine what would happen if it collapsed atop of me!"
                }

}

room_2 = {
    "name_ID": "room_2",

    "name": "needs_name2",

    "description":
    """Need Discription2""",

    "exits": {"north": "needs_name1", "east": "needs_name4", "south": "needs_name10"},

    # "objects": {"ceiling": "stuff like this"}
    # ADD EXITS HERE!
}

room_3 = {
    "name_ID": "room_3",
    "name": "needs_name3",

    "description":
    """needs description3""",

    "exits": {"westeast": "needs_name1"},
}

room_4 = {
    "name_ID": "room_4",
    "name": "needs_name4",

    "description":
    """needs description4""",

    "exits": {"west": "needs_name2"},
}

room_5 = {
    "name_ID": "room_5",
    "name": "needs_name5",

    "description":
    """needs description5""",

    "exits": {"east": "needs_name1", "north": "needs_name6"},
}

room_6 = {
    "name_ID": "room_6",
    "name": "needs_name6",

    "description":
    """needs description6""",

    "exits": {"east": "needs_name7"},
}

room_7 = {
    "name_ID": "room_7",
    "name": "needs_name7",

    "description":
    """needs description7""",

    "exits": {"east": "needs_name8", "west": "needs_name6"},
}

room_8 = {
    "name_ID": "room_8",
    "name": "needs_name8",

    "description":
    """needs description8""",

    "exits": {"south": "needs_name3", "west": "needs_name7"},
}

room_9 = {
    "name_ID": "room_9",
    "name": "needs_name9",

    "description":
    """needs description9""",

    "exits": {"east": "needs_name2"},
}

room_10 = {
    "name_ID": "room_10",
    "name": "needs_name10",

    "description":
    """needs description10""",

    "exits": {"south": "You win"},
}


rooms = {
    "needs_name1": room_1,
    "needs_name2": room_2,
    "needs_name3": room_3,
    "needs_name4": room_4,
    "needs_name5": room_5,
    "needs_name6": room_6,
    "needs_name7": room_7,
    "needs_name8": room_8,
    "needs_name9": room_9,
    "needs_name10": room_10,
}