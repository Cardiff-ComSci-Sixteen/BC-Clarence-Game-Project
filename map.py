from room_states import rooms_states
from room_states import change_description



room_reception = {
    "name_ID": "Reception",

    "name": "Reception",

    "description": rooms_states["Reception"]["state_" + str(change_description("Reception"))]["description"],

    #     """You are in a maze of twisty little passages, all alike.
    # Next to you is the School of Computer Science and
    # Informatics reception. The receptionist, Matt Strangis,
    # seems to be playing an old school text-based adventure
    # game on his computer. There are corridors leading to the
    # south and east. The exit is to the west.""",

    "exits": {"south": "Admins"},

    "objects": {"ceiling": "It looks rather unstable. The material will hardly stay strong forever."
                           "\nI cannot imagine what would happen if it collapsed atop of me!"
                }

}

room_admins = {
    "name_ID": "Admins",

    "name": "MJ and Simon's room",

    "description":
    """You are leaning against the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits": {"north": "Reception"},

    # "objects": {"ceiling": "stuff like this"}
    # ADD EXITS HERE!
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    # ADD EXITS HERE!
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
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}