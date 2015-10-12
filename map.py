room_1 = {
    "name_ID": "room_1",

    "name": "room_1",

    "description": "The ceiling has a very darkish shade to it, "
                   "\nseemingly because of the moisture."
                   "\nWhen you look at the walls you can see water running down them."
                   "\nThe place looks like it will fall apart at any moment!",

    # "description": rooms_states["room_1"]["state_" + str(change_description("room_1"))]["description"],

    "exits": {"south": "room_2", "east": "room_3", "west": "room_5"},

    "objects": {"ceiling": ["It looks rather unstable. The material will hardly stay strong forever."
                            "\nI cannot imagine what would happen if it collapsed atop of me!", 0]
                }

}

room_2 = {
    "name_ID": "room_2",

    "name": "room_2",

    "description":
    """Need Discription2""",

    "exits": {"north": "room_1", "east": "room_4", "south": "room_10"},

    # "objects": {"ceiling": "stuff like this"}
    # ADD EXITS HERE!
}

room_3 = {
    "name_ID": "room_3",
    "name": "room_3",

    "description":
    """needs description3""",

    "exits": {"westeast": "room_1"},
}

room_4 = {
    "name_ID": "room_4",
    "name": "room_4",

    "description":
    """needs description4""",

    "exits": {"west": "room_2"},
}

room_5 = {
    "name_ID": "room_5",
    "name": "room_5",

    "description":
    """needs description5""",

    "exits": {"east": "room_1", "north": "room_6"},
}

room_6 = {
    "name_ID": "room_6",
    "name": "room_6",

    "description":
    """needs description6""",

    "exits": {"east": "room_7"},
}

room_7 = {
    "name_ID": "room_7",
    "name": "room_7",

    "description":
    """needs description7""",

    "exits": {"east": "room_8", "west": "room_6"},
}

room_8 = {
    "name_ID": "room_8",
    "name": "room_8",

    "description":
    """needs description8""",

    "exits": {"south": "room_3", "west": "room_7"},
}

room_9 = {
    "name_ID": "room_9",
    "name": "room_9",

    "description":
    """needs description9""",

    "exits": {"east": "room_2"},
}

room_10 = {
    "name_ID": "room_10",
    "name": "room_10",

    "description":
    """needs description10""",

    "exits": {"south": "You win"},
}

# Had to change room names so that they would be addressed as their
# function name and ID. We can alter the names in the room dicts instead.
rooms = {
    "room_1": room_1,
    "room_2": room_2,
    "room_3": room_3,
    "room_4": room_4,
    "room_5": room_5,
    "room_6": room_6,
    "room_7": room_7,
    "room_8": room_8,
    "room_9": room_9,
    "room_10": room_10,
} # we need to decide on setting before creating names
